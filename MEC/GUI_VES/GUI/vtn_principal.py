# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vtn_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_vtn_principal(object):
    def setupUi(self, vtn_principal):
        if not vtn_principal.objectName():
            vtn_principal.setObjectName(u"vtn_principal")
        vtn_principal.resize(707, 448)
        self.centralwidget = QWidget(vtn_principal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbl_nombre = QLabel(self.centralwidget)
        self.lbl_nombre.setObjectName(u"lbl_nombre")
        self.lbl_nombre.setGeometry(QRect(110, 30, 81, 16))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lbl_nombre.setFont(font)
        self.lbl_apellido = QLabel(self.centralwidget)
        self.lbl_apellido.setObjectName(u"lbl_apellido")
        self.lbl_apellido.setGeometry(QRect(110, 60, 91, 21))
        self.lbl_apellido.setFont(font)
        self.txt_nombre = QLineEdit(self.centralwidget)
        self.txt_nombre.setObjectName(u"txt_nombre")
        self.txt_nombre.setGeometry(QRect(270, 30, 181, 20))
        self.txt_apellido = QLineEdit(self.centralwidget)
        self.txt_apellido.setObjectName(u"txt_apellido")
        self.txt_apellido.setGeometry(QRect(270, 60, 181, 20))
        self.lbl_descrip = QLabel(self.centralwidget)
        self.lbl_descrip.setObjectName(u"lbl_descrip")
        self.lbl_descrip.setGeometry(QRect(110, 90, 131, 21))
        self.lbl_descrip.setFont(font)
        self.txt_descrip = QLineEdit(self.centralwidget)
        self.txt_descrip.setObjectName(u"txt_descrip")
        self.txt_descrip.setGeometry(QRect(270, 90, 181, 20))
        self.lbl_precio = QLabel(self.centralwidget)
        self.lbl_precio.setObjectName(u"lbl_precio")
        self.lbl_precio.setGeometry(QRect(110, 120, 71, 21))
        self.lbl_precio.setFont(font)
        self.txt_precio = QLineEdit(self.centralwidget)
        self.txt_precio.setObjectName(u"txt_precio")
        self.txt_precio.setGeometry(QRect(270, 120, 181, 20))
        self.btn_limpiar = QPushButton(self.centralwidget)
        self.btn_limpiar.setObjectName(u"btn_limpiar")
        self.btn_limpiar.setGeometry(QRect(390, 300, 75, 23))
        self.btn_guardar = QPushButton(self.centralwidget)
        self.btn_guardar.setObjectName(u"btn_guardar")
        self.btn_guardar.setGeometry(QRect(190, 300, 75, 23))
        self.lbl_email = QLabel(self.centralwidget)
        self.lbl_email.setObjectName(u"lbl_email")
        self.lbl_email.setGeometry(QRect(110, 150, 61, 21))
        self.lbl_email.setFont(font)
        self.txt_email = QLineEdit(self.centralwidget)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(QRect(270, 150, 181, 20))
        vtn_principal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(vtn_principal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 707, 18))
        vtn_principal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(vtn_principal)
        self.statusbar.setObjectName(u"statusbar")
        vtn_principal.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.txt_nombre, self.txt_apellido)
        QWidget.setTabOrder(self.txt_apellido, self.txt_descrip)
        QWidget.setTabOrder(self.txt_descrip, self.txt_precio)
        QWidget.setTabOrder(self.txt_precio, self.btn_guardar)
        QWidget.setTabOrder(self.btn_guardar, self.btn_limpiar)

        self.retranslateUi(vtn_principal)

        QMetaObject.connectSlotsByName(vtn_principal)
    # setupUi

    def retranslateUi(self, vtn_principal):
        vtn_principal.setWindowTitle(QCoreApplication.translate("vtn_principal", u"MainWindow", None))
        self.lbl_nombre.setText(QCoreApplication.translate("vtn_principal", u"NOMBRE:", None))
        self.lbl_apellido.setText(QCoreApplication.translate("vtn_principal", u"APELLIDO:", None))
        self.lbl_descrip.setText(QCoreApplication.translate("vtn_principal", u"DESCRIPCION:", None))
        self.lbl_precio.setText(QCoreApplication.translate("vtn_principal", u"PRECIO:", None))
#if QT_CONFIG(tooltip)
        self.btn_limpiar.setToolTip(QCoreApplication.translate("vtn_principal", u"borrar el formulario", None))
#endif // QT_CONFIG(tooltip)
        self.btn_limpiar.setText(QCoreApplication.translate("vtn_principal", u"Limpiar", None))
#if QT_CONFIG(tooltip)
        self.btn_guardar.setToolTip(QCoreApplication.translate("vtn_principal", u"guardar datos del usuario", None))
#endif // QT_CONFIG(tooltip)
        self.btn_guardar.setText(QCoreApplication.translate("vtn_principal", u"Guardar", None))
        self.lbl_email.setText(QCoreApplication.translate("vtn_principal", u"EMAIL:", None))
    # retranslateUi

