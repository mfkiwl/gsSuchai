#include <stdio.h>
#include <csp/csp.h>
#include <csp/interfaces/csp_if_kiss.h>

#include <csp/drivers/usart.h>
#include <csp/arch/csp_thread.h>

#include <jansson.h>
#include <zmq.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <assert.h>

#include "zhelpers.h"
#include "kiss.h"

#define PORT 10			//TM-TC port
#define DPORT 11		//Debug port
#define CPORT 12        //Commands port

#define S_ADDRESS 10		//source
#define D_ADDRESS 0		    //pic node
#define R_ADDRESS_TNC 9		//tnc node (router)
#define R_ADDRESS_TRX 5		//trx node (router)

#define SERVER_TIDX 0
#define CLIENT_TIDX 1
#define USART_HANDLE 0

#define PACKET_ASCII 1

const char *type_tm = "tm"      //Message is telemetry
const char *type_cmd = "cmd"    //Message is console command
const char *type_tc = "tc"      //Message is telecomand
const char *type_db = "debug"   //Message is debug telecomand
const char *type_tnc = "tnc"    //Message is a tnc command
const char *type_trx = "tnc"    //Message is a trx command

int csp_timeout = 1000          //CSP timeout en ms

/**
 * Server task
 * Reads messages from TNC using libcsp and delivers to remote clients using zmq
 */
CSP_DEFINE_TASK(task_server)
{

    //libcsp init
    int running = 1;
    csp_socket_t *socket = csp_socket(CSP_SO_NONE);
    csp_conn_t *conn;
    csp_packet_t *packet;
    csp_packet_t *response;

    response = csp_buffer_get(sizeof(csp_packet_t) + 2);
    if( response == NULL ) {
        fprintf(stderr, "Could not allocate memory for response packet!\n");
        return CSP_TASK_RETURN;
    }
    response->data[0] = 'O';
    response->data[1] = 'K';
    response->length = 2;

    csp_bind(socket, CSP_ANY);
    csp_listen(socket, 5);

    printf("Server task started\r\n");
    int i;
    int obufflen;

    //ZMQ init
    void *context = zmq_ctx_new();
    void *publisher = zmq_socket(context, ZMQ_PUB);
    int rc = zmq_bind(publisher, "tcp://*:5556");
    assert (rc == 0);
    
    char update [200];
    char bf[200];

    // listen incomming packets
    while(running) {
        if( (conn = csp_accept(socket, 10000)) == NULL ) {
            continue;
        }
        
        while( (packet = csp_read(conn, 100)) != NULL ) {
            switch( csp_conn_dport(conn) ) {
                
                case PORT:
                    printf("task_server: Received CSP packet in address %d (len = %d)\n", D_ADDRESS, packet->length);

                    obufflen = packet->length;
                    if(PACKET_ASCII==1){				
                        for(i=0;i<obufflen;i++){
                            printf("%c", packet->data[i] );
                        }
                        printf("\n");
                    }
                    else{
                        for(i=0;i<obufflen;i++){
                            printf("0x%X", packet->data[i] );
                        }
                        printf("\n");
                    }
                
                    //send to gsRemote
                    printf("task_server: Resending as ZMQ packet\n");

                    for(i=0;i<(packet->length);i++){
                        bf[i] = packet->data[i];
                    }
                    bf[i]='\0';

                    // Send message to all "TM:" subscribers
                    sprintf (update, "TM: %s\n", bf);
                    s_send (publisher, update);

                    // libcsp tasks
                    csp_buffer_free(packet);
                    csp_send(conn, response, 1000);
                    break;

                default:
                    csp_service_handler(conn, packet);
                    break;
            }
        }

        csp_close(conn);
    }

    csp_buffer_free(response);

    zmq_close (publisher);
    zmq_ctx_destroy (context);

    return CSP_TASK_RETURN;
}


/**
 * Task clients
 * Read messages from remote clients using zmq and delivers to TNC using libcsp
 */
CSP_DEFINE_TASK(task_client)
{

    //ZMQ
    //Socket to receive messages on
    void *context = zmq_ctx_new();
    void *receiver = zmq_socket(context, ZMQ_PULL);
    zmq_bind(receiver, "tcp://*:5557");
    
    int i;
    char *message
    json_t *root;
    json_t *data;
    json_t *type;
    json_error_t error;

    //Process tasks forever
    while(1)
    {

        message = s_recv(receiver);   
        if(!message) continue;
        
        printf("[Client] Received message: %s", message);
        
        root = json_loads(message, 0, &error);
        if(!root) continue;
        
        //Check message type and perform corresponding action
        type = json_object_get(root, "type"); 
        if(!type)
        {
            printf("[Client] Malformed message\n");
        }
        //TC message
        else if(strcmp(json_string_value(type), type_tc) == 0)
        {
            data = json_object_get(root, "data");
            
            csp_transaction(0, D_ADDRESS, PORT, csp_timeout, obuff, obufflen, NULL, 0);
        }
        //Console command message
        else if(strcmp(json_string_value(type), type_cmd) == 0)
        {
            data = json_object_get(root, "data");
            int len = json_array_size(data);
            uint16_t buffer[len];
            json_t *num;
            
            for(i = 0; i < json_array_size(data); i++)
            {
                num = json_array_get(data, i);
                buffer[i] = (uint16_t)json_integer_value(num);
            }
            
            //TODO: Check this
            csp_transaction(0, D_ADDRESS, CPORT, csp_timeout, buffer, len*sizeof(uint16_t), NULL, 0);
        }
        //Debug message
        else if(strcmp(json_string_value(type), type_db) == 0)
        {
            data = json_object_get(root, "data");
            char *data_buff = json_string_value(data);
            int len = strlen(data_buff);
            
            csp_transaction(0, D_ADDRESS, DPORT, csp_timeout, data_buff, len, NULL, 0);
        }
        //Not implemented message type
        else
        {
            printf("[Client] Invalid message\n");
        }
        
        json_decref(root);
        free(message);
    }
    
    zmq_close (receiver);
    zmq_ctx_destroy (context);

    return CSP_TASK_RETURN;
}

/**
 * Main function, initializes libcsp, serial kiss interface, task client and
 * task server.
 */
int main(int argc, char **argv) {

    csp_debug_toggle_level(CSP_PACKET);
    csp_debug_toggle_level(CSP_INFO);

    csp_buffer_init(10, 300);
    csp_init(S_ADDRESS);

    struct usart_conf conf;

#if defined(CSP_WINDOWS)
    conf.device = argc != 2 ? "COM4" : argv[1];
    conf.baudrate = CBR_9600;
    conf.databits = 8;
    conf.paritysetting = NOPARITY;
    conf.stopbits = ONESTOPBIT;
    conf.checkparity = FALSE;
#elif defined(CSP_POSIX)
    conf.device = argc != 2 ? "/dev/ttyUSB0" : argv[1];
    conf.baudrate = 500000;
#elif defined(CSP_MACOSX)
    conf.device = argc != 2 ? "/dev/tty.usbserial-FTSM9EGE" : argv[1];
    conf.baudrate = 115200;
#endif

    usart_init(&conf);
    csp_kiss_init(usart_putstr, usart_insert);
    usart_set_callback(csp_kiss_rx);

    csp_route_set(R_ADDRESS_TNC, &csp_if_kiss, CSP_NODE_MAC);
    csp_route_set(D_ADDRESS, &csp_if_kiss, CSP_NODE_MAC);
    csp_route_set(R_ADDRESS_TRX, &csp_if_kiss, CSP_NODE_MAC);

    csp_route_start_task(0, 0);

    csp_conn_print_table();
    csp_route_print_table();
    csp_route_print_interfaces();


    csp_thread_handle_t handle_server;
    csp_thread_create(task_server, (signed char *) "SERVER", 1000, NULL, 0, &handle_server);
    csp_sleep_ms(100);

    csp_thread_handle_t handle_client;
    csp_thread_create(task_client, (signed char *) "CLIENT", 1000, NULL, 0, &handle_client);

    /* Wait for program to terminate (ctrl + c) */
    while(1) {
        csp_sleep_ms(5000);
    }

    return 0;

}
