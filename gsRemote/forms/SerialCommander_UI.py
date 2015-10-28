# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Console.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 521)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../../../../../home/carlos/Eléctrica/CubeSat/PIC24FJ256GA110_EXT/TRANSCEIVER/branches/trx-v3/GUI/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.textEditTerminal = QtGui.QTextEdit(self.tab)
        self.textEditTerminal.setAutoFormatting(QtGui.QTextEdit.AutoAll)
        self.textEditTerminal.setTabChangesFocus(True)
        self.textEditTerminal.setUndoRedoEnabled(False)
        self.textEditTerminal.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.textEditTerminal.setLineWrapColumnOrWidth(0)
        self.textEditTerminal.setReadOnly(True)
        self.textEditTerminal.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.textEditTerminal.setObjectName(_fromUtf8("textEditTerminal"))
        self.gridLayout_4.addWidget(self.textEditTerminal, 2, 0, 1, 8)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBoxCommand = QtGui.QGroupBox(self.tab)
        self.groupBoxCommand.setObjectName(_fromUtf8("groupBoxCommand"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBoxCommand)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.listWidgetCommand = QtGui.QListWidget(self.groupBoxCommand)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidgetCommand.sizePolicy().hasHeightForWidth())
        self.listWidgetCommand.setSizePolicy(sizePolicy)
        self.listWidgetCommand.setDragEnabled(True)
        self.listWidgetCommand.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.listWidgetCommand.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.listWidgetCommand.setAlternatingRowColors(True)
        self.listWidgetCommand.setObjectName(_fromUtf8("listWidgetCommand"))
        self.verticalLayout.addWidget(self.listWidgetCommand)
        self.horizontalLayout.addWidget(self.groupBoxCommand)
        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 1, 1, 7)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBoxRepetir = QtGui.QGroupBox(self.tab)
        self.groupBoxRepetir.setTitle(_fromUtf8(""))
        self.groupBoxRepetir.setObjectName(_fromUtf8("groupBoxRepetir"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBoxRepetir)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.labelPeriod = QtGui.QLabel(self.groupBoxRepetir)
        self.labelPeriod.setEnabled(False)
        self.labelPeriod.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPeriod.setObjectName(_fromUtf8("labelPeriod"))
        self.gridLayout_3.addWidget(self.labelPeriod, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBoxRepetir)
        self.groupConexion = QtGui.QGroupBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupConexion.sizePolicy().hasHeightForWidth())
        self.groupConexion.setSizePolicy(sizePolicy)
        self.groupConexion.setObjectName(_fromUtf8("groupConexion"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupConexion)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.labelPortSend = QtGui.QLabel(self.groupConexion)
        self.labelPortSend.setObjectName(_fromUtf8("labelPortSend"))
        self.gridLayout_2.addWidget(self.labelPortSend, 3, 0, 1, 1)
        self.pushButtonOpenPort = QtGui.QPushButton(self.groupConexion)
        self.pushButtonOpenPort.setObjectName(_fromUtf8("pushButtonOpenPort"))
        self.gridLayout_2.addWidget(self.pushButtonOpenPort, 4, 0, 1, 1)
        self.comboBoxPortRecv = QtGui.QComboBox(self.groupConexion)
        self.comboBoxPortRecv.setEditable(True)
        self.comboBoxPortRecv.setObjectName(_fromUtf8("comboBoxPortRecv"))
        self.gridLayout_2.addWidget(self.comboBoxPortRecv, 2, 1, 1, 1)
        self.pushButtonClosePort = QtGui.QPushButton(self.groupConexion)
        self.pushButtonClosePort.setEnabled(False)
        self.pushButtonClosePort.setObjectName(_fromUtf8("pushButtonClosePort"))
        self.gridLayout_2.addWidget(self.pushButtonClosePort, 4, 1, 1, 1)
        self.labePortRecv = QtGui.QLabel(self.groupConexion)
        self.labePortRecv.setObjectName(_fromUtf8("labePortRecv"))
        self.gridLayout_2.addWidget(self.labePortRecv, 2, 0, 1, 1)
        self.comboBoxPortSend = QtGui.QComboBox(self.groupConexion)
        self.comboBoxPortSend.setEditable(True)
        self.comboBoxPortSend.setObjectName(_fromUtf8("comboBoxPortSend"))
        self.gridLayout_2.addWidget(self.comboBoxPortSend, 3, 1, 1, 1)
        self.labelURL = QtGui.QLabel(self.groupConexion)
        self.labelURL.setObjectName(_fromUtf8("labelURL"))
        self.gridLayout_2.addWidget(self.labelURL, 1, 0, 1, 1)
        self.lineEditURL = QtGui.QLineEdit(self.groupConexion)
        self.lineEditURL.setObjectName(_fromUtf8("lineEditURL"))
        self.gridLayout_2.addWidget(self.lineEditURL, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupConexion)
        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.checkBoxCR = QtGui.QCheckBox(self.tab)
        self.checkBoxCR.setObjectName(_fromUtf8("checkBoxCR"))
        self.gridLayout_4.addWidget(self.checkBoxCR, 1, 6, 1, 1)
        self.pushButton = QtGui.QPushButton(self.tab)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("edit-clear"))
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_4.addWidget(self.pushButton, 3, 7, 1, 1)
        self.pushButtonSend = QtGui.QPushButton(self.tab)
        self.pushButtonSend.setEnabled(False)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("go-next"))
        self.pushButtonSend.setIcon(icon)
        self.pushButtonSend.setAutoDefault(True)
        self.pushButtonSend.setObjectName(_fromUtf8("pushButtonSend"))
        self.gridLayout_4.addWidget(self.pushButtonSend, 1, 7, 1, 1)
        self.checkBoxLF = QtGui.QCheckBox(self.tab)
        self.checkBoxLF.setChecked(True)
        self.checkBoxLF.setObjectName(_fromUtf8("checkBoxLF"))
        self.gridLayout_4.addWidget(self.checkBoxLF, 1, 5, 1, 1)
        self.lineEditSend = QtGui.QLineEdit(self.tab)
        self.lineEditSend.setObjectName(_fromUtf8("lineEditSend"))
        self.gridLayout_4.addWidget(self.lineEditSend, 1, 0, 1, 5)
        self.textEditTerminal.raise_()
        self.lineEditSend.raise_()
        self.pushButtonSend.raise_()
        self.pushButton.raise_()
        self.checkBoxCR.raise_()
        self.checkBoxLF.raise_()
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.lineEdit_tcfilter = QtGui.QLineEdit(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_tcfilter.sizePolicy().hasHeightForWidth())
        self.lineEdit_tcfilter.setSizePolicy(sizePolicy)
        self.lineEdit_tcfilter.setText(_fromUtf8(""))
        self.lineEdit_tcfilter.setDragEnabled(False)
        self.lineEdit_tcfilter.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_tcfilter.setObjectName(_fromUtf8("lineEdit_tcfilter"))
        self.gridLayout_5.addWidget(self.lineEdit_tcfilter, 0, 0, 1, 1)
        self.label_tchistory = QtGui.QLabel(self.tab_2)
        self.label_tchistory.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_tchistory.setObjectName(_fromUtf8("label_tchistory"))
        self.gridLayout_5.addWidget(self.label_tchistory, 0, 1, 1, 1)
        self.comboBox_tchistory = QtGui.QComboBox(self.tab_2)
        self.comboBox_tchistory.setEditable(True)
        self.comboBox_tchistory.setObjectName(_fromUtf8("comboBox_tchistory"))
        self.gridLayout_5.addWidget(self.comboBox_tchistory, 0, 2, 1, 1)
        self.listWidget_cmd = QtGui.QListWidget(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_cmd.sizePolicy().hasHeightForWidth())
        self.listWidget_cmd.setSizePolicy(sizePolicy)
        self.listWidget_cmd.setObjectName(_fromUtf8("listWidget_cmd"))
        self.gridLayout_5.addWidget(self.listWidget_cmd, 1, 0, 1, 1)
        self.tableWidget_tcframe = QtGui.QTableWidget(self.tab_2)
        self.tableWidget_tcframe.setDragEnabled(True)
        self.tableWidget_tcframe.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.tableWidget_tcframe.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.tableWidget_tcframe.setAlternatingRowColors(True)
        self.tableWidget_tcframe.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidget_tcframe.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget_tcframe.setObjectName(_fromUtf8("tableWidget_tcframe"))
        self.tableWidget_tcframe.setColumnCount(3)
        self.tableWidget_tcframe.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_tcframe.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_tcframe.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_tcframe.setHorizontalHeaderItem(2, item)
        self.tableWidget_tcframe.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_tcframe.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_tcframe.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_5.addWidget(self.tableWidget_tcframe, 1, 1, 1, 3)
        self.pushButton_tcclear = QtGui.QPushButton(self.tab_2)
        self.pushButton_tcclear.setObjectName(_fromUtf8("pushButton_tcclear"))
        self.gridLayout_5.addWidget(self.pushButton_tcclear, 2, 1, 1, 1)
        self.pushButton_tcsave = QtGui.QPushButton(self.tab_2)
        self.pushButton_tcsave.setObjectName(_fromUtf8("pushButton_tcsave"))
        self.gridLayout_5.addWidget(self.pushButton_tcsave, 2, 2, 1, 1)
        self.pushButton_tcsend = QtGui.QPushButton(self.tab_2)
        self.pushButton_tcsend.setObjectName(_fromUtf8("pushButton_tcsend"))
        self.gridLayout_5.addWidget(self.pushButton_tcsend, 2, 3, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_6 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.textEditTelemetry = QtGui.QPlainTextEdit(self.tab_3)
        self.textEditTelemetry.setObjectName(_fromUtf8("textEditTelemetry"))
        self.gridLayout_6.addWidget(self.textEditTelemetry, 2, 0, 1, 1)
        self.tableWidgetTelemetry = QtGui.QTableWidget(self.tab_3)
        self.tableWidgetTelemetry.setObjectName(_fromUtf8("tableWidgetTelemetry"))
        self.tableWidgetTelemetry.setColumnCount(3)
        self.tableWidgetTelemetry.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetTelemetry.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetTelemetry.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetTelemetry.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetTelemetry.setHorizontalHeaderItem(2, item)
        self.gridLayout_6.addWidget(self.tableWidgetTelemetry, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuArchivo = QtGui.QMenu(self.menubar)
        self.menuArchivo.setObjectName(_fromUtf8("menuArchivo"))
        self.menuHerramientas = QtGui.QMenu(self.menubar)
        self.menuHerramientas.setObjectName(_fromUtf8("menuHerramientas"))
        self.menuAyuda = QtGui.QMenu(self.menubar)
        self.menuAyuda.setObjectName(_fromUtf8("menuAyuda"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionGuardar = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("document-save"))
        self.actionGuardar.setIcon(icon)
        self.actionGuardar.setObjectName(_fromUtf8("actionGuardar"))
        self.actionSalir = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("application-exit"))
        self.actionSalir.setIcon(icon)
        self.actionSalir.setObjectName(_fromUtf8("actionSalir"))
        self.actionAgregar_comando = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("list-add"))
        self.actionAgregar_comando.setIcon(icon)
        self.actionAgregar_comando.setObjectName(_fromUtf8("actionAgregar_comando"))
        self.actionAcerca_de = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("help-about"))
        self.actionAcerca_de.setIcon(icon)
        self.actionAcerca_de.setObjectName(_fromUtf8("actionAcerca_de"))
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionSalir)
        self.menuHerramientas.addAction(self.actionAgregar_comando)
        self.menuAyuda.addAction(self.actionAcerca_de)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuHerramientas.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.labelPortSend.setBuddy(self.comboBoxPortSend)
        self.labePortRecv.setBuddy(self.comboBoxPortRecv)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.actionSalir, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.textEditTerminal.clear)
        QtCore.QObject.connect(self.lineEditSend, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.pushButtonSend.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.lineEditURL)
        MainWindow.setTabOrder(self.lineEditURL, self.comboBoxPortRecv)
        MainWindow.setTabOrder(self.comboBoxPortRecv, self.comboBoxPortSend)
        MainWindow.setTabOrder(self.comboBoxPortSend, self.pushButtonClosePort)
        MainWindow.setTabOrder(self.pushButtonClosePort, self.pushButtonOpenPort)
        MainWindow.setTabOrder(self.pushButtonOpenPort, self.listWidgetCommand)
        MainWindow.setTabOrder(self.listWidgetCommand, self.lineEditSend)
        MainWindow.setTabOrder(self.lineEditSend, self.pushButtonSend)
        MainWindow.setTabOrder(self.pushButtonSend, self.checkBoxLF)
        MainWindow.setTabOrder(self.checkBoxLF, self.checkBoxCR)
        MainWindow.setTabOrder(self.checkBoxCR, self.textEditTerminal)
        MainWindow.setTabOrder(self.textEditTerminal, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.lineEdit_tcfilter)
        MainWindow.setTabOrder(self.lineEdit_tcfilter, self.listWidget_cmd)
        MainWindow.setTabOrder(self.listWidget_cmd, self.comboBox_tchistory)
        MainWindow.setTabOrder(self.comboBox_tchistory, self.tableWidget_tcframe)
        MainWindow.setTabOrder(self.tableWidget_tcframe, self.pushButton_tcclear)
        MainWindow.setTabOrder(self.pushButton_tcclear, self.pushButton_tcsave)
        MainWindow.setTabOrder(self.pushButton_tcsave, self.pushButton_tcsend)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "SUCHAI Remote Ground Station", None))
        self.textEditTerminal.setDocumentTitle(_translate("MainWindow", "Log", None))
        self.groupBoxCommand.setTitle(_translate("MainWindow", "Lista de comandos", None))
        self.labelPeriod.setText(_translate("MainWindow", "LOGO", None))
        self.groupConexion.setTitle(_translate("MainWindow", "Conexión", None))
        self.labelPortSend.setText(_translate("MainWindow", "Puerto escritura", None))
        self.pushButtonOpenPort.setText(_translate("MainWindow", "Abrir", None))
        self.pushButtonClosePort.setText(_translate("MainWindow", "Cerrar", None))
        self.labePortRecv.setText(_translate("MainWindow", "Puerto lectura", None))
        self.labelURL.setText(_translate("MainWindow", "URL Servidor", None))
        self.checkBoxCR.setText(_translate("MainWindow", "CR", None))
        self.pushButton.setText(_translate("MainWindow", "Limpiar", None))
        self.pushButtonSend.setText(_translate("MainWindow", "Enviar", None))
        self.checkBoxLF.setText(_translate("MainWindow", "LF", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Consola", None))
        self.lineEdit_tcfilter.setPlaceholderText(_translate("MainWindow", "Filtrar", None))
        self.label_tchistory.setText(_translate("MainWindow", "Historial", None))
        item = self.tableWidget_tcframe.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nombre", None))
        item = self.tableWidget_tcframe.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Comando", None))
        item = self.tableWidget_tcframe.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Parámetro", None))
        self.pushButton_tcclear.setText(_translate("MainWindow", "Clear", None))
        self.pushButton_tcsave.setText(_translate("MainWindow", "Save", None))
        self.pushButton_tcsend.setText(_translate("MainWindow", "Send", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Telecomandos", None))
        item = self.tableWidgetTelemetry.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "0", None))
        item = self.tableWidgetTelemetry.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Status", None))
        item = self.tableWidgetTelemetry.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Payload", None))
        item = self.tableWidgetTelemetry.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Data", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Telemetría", None))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo", None))
        self.menuHerramientas.setTitle(_translate("MainWindow", "Herramientas", None))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda", None))
        self.actionGuardar.setText(_translate("MainWindow", "Guardar", None))
        self.actionGuardar.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.actionSalir.setText(_translate("MainWindow", "Salir", None))
        self.actionSalir.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionAgregar_comando.setText(_translate("MainWindow", "Agregar comando", None))
        self.actionAgregar_comando.setShortcut(_translate("MainWindow", "Ctrl+Shift+A", None))
        self.actionAcerca_de.setText(_translate("MainWindow", "Acerca de", None))

