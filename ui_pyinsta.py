# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pyinstaZXZLSZ.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import Resource_rc
import Resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(870, 579)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget_5 = QWidget(self.centralwidget)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(20, 10, 81, 561))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.accountspage1 = QPushButton(self.widget_5)
        self.accountspage1.setObjectName(u"accountspage1")
        icon = QIcon()
        icon.addFile(u":/icons/Icons/user (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.accountspage1.setIcon(icon)
        self.accountspage1.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.accountspage1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout)

        self.widget_6 = QWidget(self.centralwidget)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(120, 110, 571, 461))
        self.horizontalLayout_7 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.Addaccount = QStackedWidget(self.widget_6)
        self.Addaccount.setObjectName(u"Addaccount")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.Addaccount.setFont(font)
        self.Addaccount.setLayoutDirection(Qt.LeftToRight)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_15 = QHBoxLayout(self.page)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.widget_12 = QWidget(self.page)
        self.widget_12.setObjectName(u"widget_12")
        self.verticalLayout_24 = QVBoxLayout(self.widget_12)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.widget_20 = QWidget(self.widget_12)
        self.widget_20.setObjectName(u"widget_20")
        self.verticalLayout_19 = QVBoxLayout(self.widget_20)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_17 = QLabel(self.widget_20)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_17)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_9 = QSpacerItem(20, 48, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_9)

        self.widget_11 = QWidget(self.widget_20)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_6 = QVBoxLayout(self.widget_11)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_6 = QLabel(self.widget_11)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_6)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_6)

        self.label = QLabel(self.widget_11)
        self.label.setObjectName(u"label")

        self.horizontalLayout_13.addWidget(self.label)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_7)

        self.lineEdit = QLineEdit(self.widget_11)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_13.addWidget(self.lineEdit)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_8)

        self.label_2 = QLabel(self.widget_11)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_13.addWidget(self.label_2)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_9)

        self.lineEdit_2 = QLineEdit(self.widget_11)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_13.addWidget(self.lineEdit_2)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_10)

        self.pushButton_2 = QPushButton(self.widget_11)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_13.addWidget(self.pushButton_2)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_11)


        self.verticalLayout_6.addLayout(self.horizontalLayout_13)


        self.verticalLayout_7.addWidget(self.widget_11)

        self.verticalSpacer_10 = QSpacerItem(20, 58, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_10)


        self.verticalLayout_19.addLayout(self.verticalLayout_7)


        self.verticalLayout_23.addWidget(self.widget_20)

        self.widget_21 = QWidget(self.widget_12)
        self.widget_21.setObjectName(u"widget_21")
        self.verticalLayout_20 = QVBoxLayout(self.widget_21)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.widget_28 = QWidget(self.widget_21)
        self.widget_28.setObjectName(u"widget_28")
        self.verticalLayout_33 = QVBoxLayout(self.widget_28)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.label_23 = QLabel(self.widget_28)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.label_23)

        self.widget_29 = QWidget(self.widget_28)
        self.widget_29.setObjectName(u"widget_29")
        self.widget_29.setMinimumSize(QSize(0, 200))
        self.horizontalLayout_27 = QHBoxLayout(self.widget_29)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.tableWidget = QTableWidget(self.widget_29)
        self.tableWidget.setObjectName(u"tableWidget")

        self.horizontalLayout_27.addWidget(self.tableWidget)


        self.verticalLayout_34.addWidget(self.widget_29)


        self.verticalLayout_33.addLayout(self.verticalLayout_34)


        self.verticalLayout_21.addWidget(self.widget_28)

        self.verticalSpacer_11 = QSpacerItem(20, 48, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_11)

        self.verticalSpacer_12 = QSpacerItem(20, 58, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_12)


        self.verticalLayout_20.addLayout(self.verticalLayout_21)


        self.verticalLayout_23.addWidget(self.widget_21)


        self.verticalLayout_24.addLayout(self.verticalLayout_23)


        self.horizontalLayout_15.addWidget(self.widget_12)

        self.Addaccount.addWidget(self.page)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_31 = QVBoxLayout(self.page_4)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.widget_26 = QWidget(self.page_4)
        self.widget_26.setObjectName(u"widget_26")
        self.verticalLayout_35 = QVBoxLayout(self.widget_26)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.scrollArea = QScrollArea(self.widget_26)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, -471, 498, 876))
        self.verticalLayout_30 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.widget_27 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_27.setObjectName(u"widget_27")
        self.verticalLayout_32 = QVBoxLayout(self.widget_27)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_21 = QLabel(self.widget_27)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_21)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_27)

        self.label_22 = QLabel(self.widget_27)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_26.addWidget(self.label_22)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_28)

        self.lineEdit_4 = QLineEdit(self.widget_27)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_26.addWidget(self.lineEdit_4)

        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_33)

        self.pushButton_4 = QPushButton(self.widget_27)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_26.addWidget(self.pushButton_4)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_37)


        self.verticalLayout_32.addLayout(self.horizontalLayout_26)


        self.verticalLayout_26.addWidget(self.widget_27)

        self.widget_23 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_23.setObjectName(u"widget_23")
        self.verticalLayout_25 = QVBoxLayout(self.widget_23)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_19 = QLabel(self.widget_23)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_19)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_34)

        self.label_24 = QLabel(self.widget_23)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_28.addWidget(self.label_24)

        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_36)

        self.lineEdit_6 = QLineEdit(self.widget_23)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.horizontalLayout_28.addWidget(self.lineEdit_6)

        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_40)

        self.pushButton_6 = QPushButton(self.widget_23)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_28.addWidget(self.pushButton_6)

        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_41)


        self.verticalLayout_25.addLayout(self.horizontalLayout_28)


        self.verticalLayout_26.addWidget(self.widget_23)

        self.widget_32 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_32.setObjectName(u"widget_32")
        self.verticalLayout_38 = QVBoxLayout(self.widget_32)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_26 = QLabel(self.widget_32)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.verticalLayout_38.addWidget(self.label_26)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_38)

        self.label_27 = QLabel(self.widget_32)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_30.addWidget(self.label_27)

        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_39)

        self.lineEdit_7 = QLineEdit(self.widget_32)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.horizontalLayout_30.addWidget(self.lineEdit_7)

        self.horizontalSpacer_42 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_42)

        self.pushButton_7 = QPushButton(self.widget_32)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_30.addWidget(self.pushButton_7)

        self.horizontalSpacer_43 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_43)


        self.verticalLayout_38.addLayout(self.horizontalLayout_30)


        self.verticalLayout_26.addWidget(self.widget_32)

        self.widget_22 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_22.setObjectName(u"widget_22")
        self.verticalLayout_22 = QVBoxLayout(self.widget_22)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_15 = QLabel(self.widget_22)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_15)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_24)

        self.label_16 = QLabel(self.widget_22)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_14.addWidget(self.label_16)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_25)

        self.lineEdit_3 = QLineEdit(self.widget_22)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_14.addWidget(self.lineEdit_3)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_26)

        self.folowlimit = QPushButton(self.widget_22)
        self.folowlimit.setObjectName(u"folowlimit")

        self.horizontalLayout_14.addWidget(self.folowlimit)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_29)


        self.verticalLayout_22.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_30)

        self.label_18 = QLabel(self.widget_22)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_24.addWidget(self.label_18)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_31)

        self.lineEdit_5 = QLineEdit(self.widget_22)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout_24.addWidget(self.lineEdit_5)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_32)

        self.Change = QPushButton(self.widget_22)
        self.Change.setObjectName(u"Change")

        self.horizontalLayout_24.addWidget(self.Change)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_35)


        self.verticalLayout_22.addLayout(self.horizontalLayout_24)


        self.verticalLayout_26.addWidget(self.widget_22)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.widget_24 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_24.setObjectName(u"widget_24")
        self.verticalLayout_27 = QVBoxLayout(self.widget_24)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_20 = QLabel(self.widget_24)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.label_20)

        self.widget_25 = QWidget(self.widget_24)
        self.widget_25.setObjectName(u"widget_25")
        self.widget_25.setMinimumSize(QSize(0, 200))
        self.horizontalLayout_25 = QHBoxLayout(self.widget_25)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.tableWidget_2 = QTableWidget(self.widget_25)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.horizontalLayout_25.addWidget(self.tableWidget_2)


        self.verticalLayout_28.addWidget(self.widget_25)


        self.verticalLayout_27.addLayout(self.verticalLayout_28)


        self.verticalLayout_29.addWidget(self.widget_24)


        self.verticalLayout_26.addLayout(self.verticalLayout_29)

        self.widget_30 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_30.setObjectName(u"widget_30")
        self.verticalLayout_36 = QVBoxLayout(self.widget_30)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.label_25 = QLabel(self.widget_30)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.verticalLayout_37.addWidget(self.label_25)

        self.widget_31 = QWidget(self.widget_30)
        self.widget_31.setObjectName(u"widget_31")
        self.widget_31.setMinimumSize(QSize(0, 200))
        self.horizontalLayout_29 = QHBoxLayout(self.widget_31)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.tableWidget_3 = QTableWidget(self.widget_31)
        self.tableWidget_3.setObjectName(u"tableWidget_3")

        self.horizontalLayout_29.addWidget(self.tableWidget_3)


        self.verticalLayout_37.addWidget(self.widget_31)


        self.verticalLayout_36.addLayout(self.verticalLayout_37)


        self.verticalLayout_26.addWidget(self.widget_30)


        self.verticalLayout_30.addLayout(self.verticalLayout_26)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_35.addWidget(self.scrollArea)


        self.verticalLayout_31.addWidget(self.widget_26)

        self.Addaccount.addWidget(self.page_4)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_18 = QVBoxLayout(self.page_3)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.widget_19 = QWidget(self.page_3)
        self.widget_19.setObjectName(u"widget_19")
        self.verticalLayout_17 = QVBoxLayout(self.widget_19)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.activate_unfollow_2 = QPushButton(self.widget_19)
        self.activate_unfollow_2.setObjectName(u"activate_unfollow_2")

        self.verticalLayout_17.addWidget(self.activate_unfollow_2)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.widget_16 = QWidget(self.widget_19)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_18)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.widget_17 = QWidget(self.widget_16)
        self.widget_17.setObjectName(u"widget_17")
        self.verticalLayout_12 = QVBoxLayout(self.widget_17)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_11 = QLabel(self.widget_17)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setPixmap(QPixmap(u":/icons/Icons/image_fx_follow_sign_held_by_a_robot.png"))
        self.label_11.setScaledContents(True)

        self.verticalLayout_13.addWidget(self.label_11)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_12 = QLabel(self.widget_17)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_12)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_19)

        self.poststatus_3 = QLabel(self.widget_17)
        self.poststatus_3.setObjectName(u"poststatus_3")
        self.poststatus_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.poststatus_3)


        self.verticalLayout_13.addLayout(self.horizontalLayout_22)

        self.activate_follow = QPushButton(self.widget_17)
        self.activate_follow.setObjectName(u"activate_follow")

        self.verticalLayout_13.addWidget(self.activate_follow)


        self.verticalLayout_12.addLayout(self.verticalLayout_13)


        self.horizontalLayout_21.addWidget(self.widget_17)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_20)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_21)

        self.widget_18 = QWidget(self.widget_16)
        self.widget_18.setObjectName(u"widget_18")
        self.verticalLayout_14 = QVBoxLayout(self.widget_18)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_13 = QLabel(self.widget_18)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setPixmap(QPixmap(u":/icons/Icons/image_fx_un_follow_sign_held_by_a_robot.png"))
        self.label_13.setScaledContents(True)

        self.verticalLayout_15.addWidget(self.label_13)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_14 = QLabel(self.widget_18)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_14)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_22)

        self.poststatus_4 = QLabel(self.widget_18)
        self.poststatus_4.setObjectName(u"poststatus_4")
        self.poststatus_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.poststatus_4)


        self.verticalLayout_15.addLayout(self.horizontalLayout_23)

        self.activate_unfollow = QPushButton(self.widget_18)
        self.activate_unfollow.setObjectName(u"activate_unfollow")

        self.verticalLayout_15.addWidget(self.activate_unfollow)


        self.verticalLayout_14.addLayout(self.verticalLayout_15)


        self.horizontalLayout_21.addWidget(self.widget_18)


        self.horizontalLayout_19.addLayout(self.horizontalLayout_21)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_23)


        self.verticalLayout_16.addWidget(self.widget_16)

        self.widget_15 = QWidget(self.widget_19)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_16)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.widget_13 = QWidget(self.widget_15)
        self.widget_13.setObjectName(u"widget_13")
        self.verticalLayout_9 = QVBoxLayout(self.widget_13)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_7 = QLabel(self.widget_13)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setPixmap(QPixmap(u":/icons/Icons/image_fx_robot_holding_a_sign_with_the_words_post_writ.png"))
        self.label_7.setScaledContents(True)

        self.verticalLayout_8.addWidget(self.label_7)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_8 = QLabel(self.widget_13)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_8)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_12)

        self.poststatus = QLabel(self.widget_13)
        self.poststatus.setObjectName(u"poststatus")
        self.poststatus.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.poststatus)


        self.verticalLayout_8.addLayout(self.horizontalLayout_16)

        self.activate_post = QPushButton(self.widget_13)
        self.activate_post.setObjectName(u"activate_post")

        self.verticalLayout_8.addWidget(self.activate_post)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)


        self.horizontalLayout_20.addWidget(self.widget_13)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_15)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_14)

        self.widget_14 = QWidget(self.widget_15)
        self.widget_14.setObjectName(u"widget_14")
        self.verticalLayout_10 = QVBoxLayout(self.widget_14)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_9 = QLabel(self.widget_14)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setPixmap(QPixmap(u":/icons/Icons/image_fx_robot_holding_a_sign_with_the_words_story_wri.png"))
        self.label_9.setScaledContents(True)

        self.verticalLayout_11.addWidget(self.label_9)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_10 = QLabel(self.widget_14)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_10)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_13)

        self.poststatus_2 = QLabel(self.widget_14)
        self.poststatus_2.setObjectName(u"poststatus_2")
        self.poststatus_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.poststatus_2)


        self.verticalLayout_11.addLayout(self.horizontalLayout_17)

        self.activate_story = QPushButton(self.widget_14)
        self.activate_story.setObjectName(u"activate_story")

        self.verticalLayout_11.addWidget(self.activate_story)


        self.verticalLayout_10.addLayout(self.verticalLayout_11)


        self.horizontalLayout_20.addWidget(self.widget_14)


        self.horizontalLayout_18.addLayout(self.horizontalLayout_20)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_17)


        self.verticalLayout_16.addWidget(self.widget_15)


        self.verticalLayout_17.addLayout(self.verticalLayout_16)


        self.verticalLayout_18.addWidget(self.widget_19)

        self.Addaccount.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_11 = QHBoxLayout(self.page_2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.widget_9 = QWidget(self.page_2)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_2 = QVBoxLayout(self.widget_9)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.widget_10 = QWidget(self.widget_9)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.widget_10)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setPixmap(QPixmap(u":/icons/Icons/image_fx_accounts_icon_with_tiny_robots.png"))
        self.label_5.setScaledContents(True)

        self.verticalLayout_5.addWidget(self.label_5)

        self.accountspage = QPushButton(self.widget_10)
        self.accountspage.setObjectName(u"accountspage")

        self.verticalLayout_5.addWidget(self.accountspage)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)


        self.horizontalLayout_10.addLayout(self.verticalLayout_5)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_3)


        self.horizontalLayout_8.addWidget(self.widget_10)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_8)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_7)


        self.horizontalLayout_11.addWidget(self.widget_9)

        self.Addaccount.addWidget(self.page_2)

        self.horizontalLayout_7.addWidget(self.Addaccount)

        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(111, 11, 581, 91))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget_3 = QWidget(self.widget_4)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton = QPushButton(self.widget_3)
        self.pushButton.setObjectName(u"pushButton")
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/menu-bar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.pushButton)


        self.horizontalLayout_4.addWidget(self.widget_3)

        self.horizontalSpacer = QSpacerItem(108, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.widget = QWidget(self.widget_4)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.deco = QLabel(self.widget)
        self.deco.setObjectName(u"deco")
        self.deco.setPixmap(QPixmap(u":/icons/Icons/image_fx_cool_robot_from_mad_max_road_of_holding_a_hug (1).png"))
        self.deco.setScaledContents(True)

        self.horizontalLayout.addWidget(self.deco)


        self.horizontalLayout_4.addWidget(self.widget)

        self.horizontalSpacer_2 = QSpacerItem(238, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.widget_2 = QWidget(self.widget_4)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.deco_2 = QLabel(self.widget_2)
        self.deco_2.setObjectName(u"deco_2")
        self.deco_2.setPixmap(QPixmap(u":/icons/Icons/image_fx_cool_robot_from_mad_max_road_of_holding_a_hug (1).png"))
        self.deco_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.deco_2)


        self.horizontalLayout_4.addWidget(self.widget_2)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.toggled.connect(self.widget_5.setHidden)
        self.pushButton.toggled.connect(self.widget_5.setVisible)
        self.pushButton_4.clicked["bool"].connect(self.lineEdit_4.clear)
        self.pushButton_6.clicked["bool"].connect(self.lineEdit_6.clear)
        self.folowlimit.clicked["bool"].connect(self.lineEdit_3.clear)
        self.Change.clicked["bool"].connect(self.lineEdit_5.clear)
        self.pushButton_2.clicked["bool"].connect(self.lineEdit_2.clear)
        self.pushButton_2.clicked["bool"].connect(self.lineEdit.clear)
        self.pushButton_7.clicked["bool"].connect(self.lineEdit_7.clear)

        self.Addaccount.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.accountspage1.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Accounts", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Add Account Details ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"User Name", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Growing accounts ", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Add Follow account", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"User Name", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Link setting", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Image Folder", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Captions", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Add caption", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Adjust limits ", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Follow limit ", None))
        self.folowlimit.setText(QCoreApplication.translate("MainWindow", u"Change", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Unfollow Limit", None))
        self.Change.setText(QCoreApplication.translate("MainWindow", u"Change", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Follow Accounts", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Captions", None))
        self.activate_unfollow_2.setText(QCoreApplication.translate("MainWindow", u"Activate All", None))
        self.label_11.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.poststatus_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.activate_follow.setText(QCoreApplication.translate("MainWindow", u"Activate", None))
        self.label_13.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.poststatus_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.activate_unfollow.setText(QCoreApplication.translate("MainWindow", u"Activate", None))
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.poststatus.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.activate_post.setText(QCoreApplication.translate("MainWindow", u"Activate", None))
        self.label_9.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.poststatus_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.activate_story.setText(QCoreApplication.translate("MainWindow", u"Activate", None))
        self.label_5.setText("")
        self.accountspage.setText(QCoreApplication.translate("MainWindow", u"Account Management", None))
        self.pushButton.setText("")
        self.deco.setText("")
        self.deco_2.setText("")
    # retranslateUi

