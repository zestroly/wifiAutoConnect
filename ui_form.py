# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formZDjidj.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextBrowser, QWidget)

class Ui_Home(object):
    def setupUi(self, Home):
        if not Home.objectName():
            Home.setObjectName(u"Home")
        Home.resize(381, 191)
        self.gridLayout = QGridLayout(Home)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Home)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.ssid = QLineEdit(Home)
        self.ssid.setObjectName(u"ssid")

        self.gridLayout.addWidget(self.ssid, 0, 1, 1, 1)

        self.label_2 = QLabel(Home)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.password = QLineEdit(Home)
        self.password.setObjectName(u"password")

        self.gridLayout.addWidget(self.password, 1, 1, 1, 1)

        self.Log = QTextBrowser(Home)
        self.Log.setObjectName(u"Log")

        self.gridLayout.addWidget(self.Log, 2, 0, 1, 3)

        self.connect = QPushButton(Home)
        self.connect.setCheckable(True)
        self.connect.setObjectName(u"connect")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connect.sizePolicy().hasHeightForWidth())
        self.connect.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.connect, 0, 2, 2, 1)


        self.retranslateUi(Home)

        QMetaObject.connectSlotsByName(Home)
    # setupUi

    def retranslateUi(self, Home):
        Home.setWindowTitle(QCoreApplication.translate("Home", u"Home", None))
        self.label.setText(QCoreApplication.translate("Home", u"\u65e0\u7ebf", None))
        self.label_2.setText(QCoreApplication.translate("Home", u"\u5bc6\u7801", None))
        self.connect.setText(QCoreApplication.translate("Home", u"\u8fde\u63a5", None))
    # retranslateUi

