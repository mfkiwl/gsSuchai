# SUCHAI Ground Station Software

The Ground Station software is divided in two: a **remote** side and an 
**antenna** side

The **Antenna Side Software** drives the Radio (TNC-ICOM) to sending/receiving 
frames to/from the satellite.

The **Remote Side Software** drives the Antenna Side Software sending and 
receving telecommands/telemetry  to/from the satellite with a GUI.

## SUCHAI Ground Station Messages

Messages shared between gsAntenna and gsRemote are JSON documents with the
following keys:

* type: type of message as string
* data: data of the message. Type depend of the message

### Telecomand

Message that represent SUCHAI telecomands in the format [cmd, value, ...]

* type: "tc"
* data: Array of chars with the format [CMD-H,CMD-L,VAL-H,VAL-L, ...]

### Console command

Message that represent a command for SUCHAI console. Data is a string.

* type: "cmd"
* data: String, ex. "exe_cmd 0x3001 0"

### Debug telecomand

Message that represent a debug string to show in SUCHAI console.

* type: "debug"
* data: String, ex "hola mundo"

### Telemetry

Message that represent telemetry downloaded from SUCHAI satellite. Data is an
array of values.

* type: "tm"
* data: Array of chars in the format [VALUE-H, VALUE-L, ...]


# Antenna Side Software (ASS):
licsp is the library from Gomspace (to interface with the NanoCom and TNC1), 
it is available on github, the version used here is checkout *10c3151ba619d9e0c8affe0b49abd854e4159074* 

## Modification to the libcsp
**examples/kiss.c** 
Starting point we took to develop the ASS. Running this modified examples create 
the threads to send/receive the frames and retransmit them to the RSS

**wscript**
We modify the lib to compile examples/kiss.c against, in order to add *LIB=-lzmq* 
flag to the compiler

## ZMQ Node
The Antenna Side Software is connect to remote clients using ZMQ as a *Publisher*
to send telemtry downloaded from satellite. Telecomands are read from a *PUSH-PULL*
socket.

* PUBLISHER-SUBSCRIBER socket in **port 5556** over tcp to read messages from ASS
* PUSH_PULL socket in **port 5557** over tcp to send messages to ASS


# Remote Side Software (RSS):
Based in @carlgonz [SerialCommander](https://github.com/carlgonz/SerialCommander) 
project using ZMQ sockets to interface with the Antenna Side Software in a 
Publisher-Subscriber topology.

