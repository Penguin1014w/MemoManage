# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\tasks\managememo\memo.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(370, 317)
        MainWindow.setStyleSheet("background-color:transparent")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 0, 350, 300))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.bgframe = QtWidgets.QFrame(self.widget)
        self.bgframe.setGeometry(QtCore.QRect(0, 0, 350, 300))
        self.bgframe.setStyleSheet("background-color:rgb(236, 236, 236);\n"
"border-radius:30px;")
        self.bgframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bgframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bgframe.setObjectName("bgframe")
        self.top = QtWidgets.QFrame(self.bgframe)
        self.top.setGeometry(QtCore.QRect(0, 0, 351, 41))
        self.top.setStyleSheet("background-color: rgb(182, 182, 182);\n"
"border-bottom-left-radius: 6px;\n"
"border-bottom-right-radius: 6px;\n"
"\n"
"")
        self.top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top.setObjectName("top")
        self.closebutton = QtWidgets.QPushButton(self.top)
        self.closebutton.setGeometry(QtCore.QRect(300, 8, 31, 28))
        self.closebutton.setStyleSheet("QPushButton {\n"
"    background-color: transparent;  /* 默认背景透明 */\n"
"    border: none;                   /* 去除边框 */\n"
"    padding: 8px;                   /* 给按钮一点内边距 */\n"
"}\n"
"\n"
"QPushButton:clicked {\n"
"    background-color: rgb(150, 150, 150);  /* 点击时的背景色 */\n"
"    border-radius: 8px;         /* 圆角效果 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(150, 150, 150);  /* 悬停时的背景色 */\n"
"    border-radius: 8px;         /* 圆角效果 */\n"
"}")
        self.closebutton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d:\\tasks\\managememo\\icon/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closebutton.setIcon(icon)
        self.closebutton.setObjectName("closebutton")
        self.smallbutton = QtWidgets.QPushButton(self.top)
        self.smallbutton.setGeometry(QtCore.QRect(270, 8, 31, 28))
        self.smallbutton.setStyleSheet("QPushButton {\n"
"    background-color: transparent;  /* 默认背景透明 */\n"
"    border: none;                   /* 去除边框 */\n"
"    padding: 8px;                   /* 给按钮一点内边距 */\n"
"}\n"
"\n"
"QPushButton:clicked {\n"
"    background-color: rgb(150, 150, 150);  /* 点击时的背景色 */\n"
"    border-radius: 8px;         /* 圆角效果 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(150, 150, 150);  /* 悬停时的背景色 */\n"
"    border-radius: 8px;         /* 圆角效果 */\n"
"}")
        self.smallbutton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("d:\\tasks\\managememo\\icon/small.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.smallbutton.setIcon(icon1)
        self.smallbutton.setObjectName("smallbutton")
        self.morebutton = QtWidgets.QPushButton(self.top)
        self.morebutton.setGeometry(QtCore.QRect(240, 8, 31, 28))
        self.morebutton.setStyleSheet("QPushButton {\n"
"    background-color: transparent;  /* 默认背景透明 */\n"
"    border: none;                   /* 去除边框 */\n"
"    padding: 8px;                   /* 给按钮一点内边距 */\n"
"}\n"
"QPushButton:clicked {\n"
"    background-color: rgb(150, 150, 150);  /* 点击时的背景色 */\n"
"    border-radius: 8px;         /* 圆角效果 */\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: rgb(150, 150, 150);  /* 选中状态时的背景色 */\n"
"    border-radius: 8px;         /* 圆角效果 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(150, 150, 150);  /* 悬停时的背景色 */\n"
"    border-radius: 8px;         /* 圆角效果 */\n"
"}")
        self.morebutton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("d:\\tasks\\managememo\\icon/more.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.morebutton.setIcon(icon2)
        self.morebutton.setObjectName("morebutton")
        self.addbutton = QtWidgets.QPushButton(self.top)
        self.addbutton.setGeometry(QtCore.QRect(20, 8, 31, 28))
        self.addbutton.setStyleSheet("QPushButton {\n"
"    background-color: transparent;  /* 默认背景透明 */\n"
"    border: none;                   /* 去除边框 */\n"
"    padding: 8px;                   /* 给按钮一点内边距 */\n"
"}\n"
"\n"
"QPushButton:clicked {\n"
"    background-color: rgb(150, 150, 150);  /* 点击时的背景色 */\n"
"    border-radius: 8px;         /* 圆角效果 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(150, 150, 150);  /* 悬停时的背景色 */\n"
"    border-radius: 8px;         /* 圆角效果 */\n"
"}")
        self.addbutton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("d:\\tasks\\managememo\\icon/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addbutton.setIcon(icon3)
        self.addbutton.setObjectName("addbutton")
        self.bottom = QtWidgets.QFrame(self.bgframe)
        self.bottom.setGeometry(QtCore.QRect(0, 260, 351, 41))
        self.bottom.setStyleSheet("background-color: rgb(182, 182, 182);\n"
"border-top-left-radius: 6px;\n"
"border-top-right-radius: 6px;\n"
"\n"
"")
        self.bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom.setObjectName("bottom")
        self.boldbutton = QtWidgets.QPushButton(self.bottom)
        self.boldbutton.setGeometry(QtCore.QRect(30, 0, 41, 41))
        self.boldbutton.setStyleSheet("QPushButton {\n"
"    background-color: transparent;  /* 默认背景透明 */\n"
"    border: none;                   /* 去除边框 */\n"
"    padding: 8px;                   /* 给按钮一点内边距 */\n"
"}\n"
"QPushButton:clicked {\n"
"    background-color: rgb(150, 150, 150);  /* 点击时的背景色 */\n"
"    border-radius: 8px;         /* 圆角效果 */\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: rgb(150, 150, 150);  /* 选中状态时的背景色 */\n"
"    border-radius: 8px;         /* 圆角效果 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(150, 150, 150);  /* 悬停时的背景色 */\n"
"    border-radius: 8px;         /* 圆角效果 */\n"
"}")
        self.boldbutton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("d:\\tasks\\managememo\\icon/bold.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boldbutton.setIcon(icon4)
        self.boldbutton.setObjectName("boldbutton")
        self.dialogsbutton = QtWidgets.QPushButton(self.bottom)
        self.dialogsbutton.setGeometry(QtCore.QRect(70, 0, 41, 41))
        self.dialogsbutton.setStyleSheet("QPushButton {\n"
"    background-color: transparent;  /* 默认背景透明 */\n"
"    border: none;                   /* 去除边框 */\n"
"    padding: 8px;                   /* 给按钮一点内边距 */\n"
"}\n"
"\n"
"QPushButton:clicked {\n"
"    background-color: rgb(150, 150, 150);  /* 点击时的背景色 */\n"
"    border-radius: 8px;         /* 圆角效果 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(150, 150, 150);  /* 悬停时的背景色 */\n"
"    border-radius: 8px;         /* 圆角效果 */\n"
"}")
        self.dialogsbutton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("d:\\tasks\\managememo\\icon/dialogs.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dialogsbutton.setIcon(icon5)
        self.dialogsbutton.setObjectName("dialogsbutton")
        self.eyebutton = QtWidgets.QPushButton(self.bottom)
        self.eyebutton.setGeometry(QtCore.QRect(110, 0, 41, 41))
        self.eyebutton.setStyleSheet("QPushButton {\n"
"    background-color: transparent;  /* 默认背景透明 */\n"
"    border: none;                   /* 去除边框 */\n"
"    padding: 8px;                   /* 给按钮一点内边距 */\n"
"}\n"
"\n"
"QPushButton:clicked {\n"
"    background-color: rgb(150, 150, 150);  /* 点击时的背景色 */\n"
"    border-radius: 8px;         /* 圆角效果 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(150, 150, 150);  /* 悬停时的背景色 */\n"
"    border-radius: 8px;         /* 圆角效果 */\n"
"}")
        self.eyebutton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("d:\\tasks\\managememo\\icon/visibilityon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.eyebutton.setIcon(icon6)
        self.eyebutton.setObjectName("eyebutton")
        self.linkbutton = QtWidgets.QPushButton(self.bottom)
        self.linkbutton.setGeometry(QtCore.QRect(150, 0, 41, 41))
        self.linkbutton.setStyleSheet("QPushButton {\n"
"    background-color: transparent;  /* 默认背景透明 */\n"
"    border: none;                   /* 去除边框 */\n"
"    padding: 8px;                   /* 给按钮一点内边距 */\n"
"}\n"
"\n"
"QPushButton:clicked {\n"
"    background-color: rgb(150, 150, 150);  /* 点击时的背景色 */\n"
"    border-radius: 8px;         /* 圆角效果 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(150, 150, 150);  /* 悬停时的背景色 */\n"
"    border-radius: 8px;         /* 圆角效果 */\n"
"}")
        self.linkbutton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("d:\\tasks\\managememo\\icon/addlink.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.linkbutton.setIcon(icon7)
        self.linkbutton.setObjectName("linkbutton")
        self.textEdit = QtWidgets.QTextEdit(self.bgframe)
        self.textEdit.setGeometry(QtCore.QRect(0, 40, 351, 221))
        self.textEdit.setStyleSheet("#textEdit {\n"
"    background-color: transparent;\n"
"    font: 12pt \"Arial\"; /* 英文字体 */\n"
"    font: 12pt \"Yu Mincho\"; /* 日文字体 */\n"
"    font: 12pt \"新宋体\"; /* 中文字体 */\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
import resources_rc
