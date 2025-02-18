# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Lab2.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(822, 709)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.EntryLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EntryLabel.sizePolicy().hasHeightForWidth())
        self.EntryLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EntryLabel.setFont(font)
        self.EntryLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.EntryLabel.setObjectName("EntryLabel")
        self.verticalLayout_4.addWidget(self.EntryLabel)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.distLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.distLabel.setFont(font)
        self.distLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.distLabel.setObjectName("distLabel")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.distLabel)
        self.distComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.distComboBox.setObjectName("distComboBox")
        self.distComboBox.addItem("")
        self.distComboBox.addItem("")
        self.distComboBox.addItem("")
        self.distComboBox.addItem("")
        self.distComboBox.addItem("")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.distComboBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_4.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.LowerBoundLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LowerBoundLabel.setFont(font)
        self.LowerBoundLabel.setObjectName("LowerBoundLabel")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.LowerBoundLabel)
        self.LowerBoundLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.LowerBoundLineEdit.setObjectName("LowerBoundLineEdit")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.LowerBoundLineEdit)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_4.setItem(3, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        self.UpperBoundLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.UpperBoundLabel.setFont(font)
        self.UpperBoundLabel.setObjectName("UpperBoundLabel")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.UpperBoundLabel)
        self.UpperBoundLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.UpperBoundLineEdit.setObjectName("UpperBoundLineEdit")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.UpperBoundLineEdit)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_4.setItem(5, QtWidgets.QFormLayout.LabelRole, spacerItem2)
        self.NLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.NLabel.setFont(font)
        self.NLabel.setObjectName("NLabel")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.NLabel)
        self.NLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.NLineEdit.setObjectName("NLineEdit")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.NLineEdit)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_4.setItem(7, QtWidgets.QFormLayout.LabelRole, spacerItem3)
        self.BandwidthLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BandwidthLabel.setFont(font)
        self.BandwidthLabel.setObjectName("BandwithLabel")
        self.formLayout_4.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.BandwidthLabel)
        self.BandwidthLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.BandwidthLineEdit.setInputMask("")
        self.BandwidthLineEdit.setObjectName("BandwithLineEdit")
        self.formLayout_4.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.BandwidthLineEdit)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_4.setItem(9, QtWidgets.QFormLayout.LabelRole, spacerItem4)
        self.bandwidthRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.bandwidthRadioButton.setObjectName("bandwidthRadioButton")
        self.formLayout_4.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.bandwidthRadioButton)
        self.MLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MLabel.sizePolicy().hasHeightForWidth())
        self.MLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MLabel.setFont(font)
        self.MLabel.setObjectName("MLabel")
        self.formLayout_4.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.MLabel)
        self.MLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.MLineEdit.setObjectName("MLineEdit")
        self.formLayout_4.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.MLineEdit)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_4.setItem(11, QtWidgets.QFormLayout.LabelRole, spacerItem5)
        self.verticalLayout_4.addLayout(self.formLayout_4)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_4.addWidget(self.line_5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem6)
        self.calcButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calcButton.sizePolicy().hasHeightForWidth())
        self.calcButton.setSizePolicy(sizePolicy)
        self.calcButton.setObjectName("calcButton")
        self.verticalLayout_4.addWidget(self.calcButton)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem7)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.FirstGraphLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FirstGraphLabel.setFont(font)
        self.FirstGraphLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.FirstGraphLabel.setObjectName("FirstGraphLabel")
        self.verticalLayout.addWidget(self.FirstGraphLabel)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.firstGraphWidget = PlotWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.firstGraphWidget.sizePolicy().hasHeightForWidth())
        self.firstGraphWidget.setSizePolicy(sizePolicy)
        self.firstGraphWidget.setObjectName("firstGraphWidget")
        self.firstGraphWidget.setBackground('w')
        self.verticalLayout.addWidget(self.firstGraphWidget)
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout.addWidget(self.line_6)
        self.SecondGraphLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SecondGraphLabel.setFont(font)
        self.SecondGraphLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SecondGraphLabel.setObjectName("SecondGraphLabel")
        self.verticalLayout.addWidget(self.SecondGraphLabel)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.secondGraphWidget = PlotWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.secondGraphWidget.sizePolicy().hasHeightForWidth())
        self.secondGraphWidget.setSizePolicy(sizePolicy)
        self.secondGraphWidget.setObjectName("secondGraphWidget")
        self.secondGraphWidget.setBackground('w')
        self.verticalLayout.addWidget(self.secondGraphWidget)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 822, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.EntryLabel.setText(_translate("MainWindow", "Параметры распределения"))
        self.distLabel.setText(_translate("MainWindow", "Распределение:"))
        self.distComboBox.setItemText(0, _translate("MainWindow", "Нормальное распределение"))
        self.distComboBox.setItemText(1, _translate("MainWindow", "Равномерное распределение"))
        self.distComboBox.setItemText(2, _translate("MainWindow", "Экспоненциальное распределение"))
        self.distComboBox.setItemText(3, _translate("MainWindow", "Распределение Лапласа"))
        self.distComboBox.setItemText(4, _translate("MainWindow", "Распределение Коши"))
        self.LowerBoundLabel.setText(_translate("MainWindow", "Нижняя граница:"))
        self.LowerBoundLineEdit.setText(_translate("MainWindow", "0"))
        self.UpperBoundLabel.setText(_translate("MainWindow", "Верхняя граница:"))
        self.UpperBoundLineEdit.setText(_translate("MainWindow", "1"))
        self.NLabel.setText(_translate("MainWindow", "Объём выборки:"))
        self.NLineEdit.setText(_translate("MainWindow", "100"))
        self.BandwidthLabel.setText(_translate("MainWindow", "Размытость:"))
        self.BandwidthLineEdit.setText(_translate("MainWindow", "0.5"))
        self.MLabel.setText(_translate("MainWindow", "Кол-во интервалов:"))
        self.MLineEdit.setText(_translate("MainWindow", "20"))
        self.bandwidthRadioButton.setText(_translate("MainWindow", "Подобрать оптимальный параметр"))
        self.calcButton.setText(_translate("MainWindow", "Провести оценку"))
        self.FirstGraphLabel.setText(_translate("MainWindow", "Функция распределения"))
        self.SecondGraphLabel.setText(_translate("MainWindow", "Плотность распределения"))
from pyqtgraph import PlotWidget
