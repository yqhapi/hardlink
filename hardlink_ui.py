# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hardlink.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QHBoxLayout, QLineEdit, QPlainTextEdit,
    QProgressBar, QPushButton, QRadioButton, QVBoxLayout)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 400)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(100, -1, -1, -1)
        self.select_file_button = QRadioButton(Form)
        self.select_file_button.setObjectName(u"select_file_button")
        font = QFont()
        font.setPointSize(12)
        self.select_file_button.setFont(font)
        self.select_file_button.setChecked(False)
        self.select_file_button.setAutoRepeat(False)

        self.horizontalLayout_4.addWidget(self.select_file_button)

        self.select_dir_button = QRadioButton(Form)
        self.select_dir_button.setObjectName(u"select_dir_button")
        self.select_dir_button.setEnabled(True)
        self.select_dir_button.setFont(font)
        self.select_dir_button.setTabletTracking(False)
        self.select_dir_button.setChecked(True)

        self.horizontalLayout_4.addWidget(self.select_dir_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.select_source_dir = QPushButton(Form)
        self.select_source_dir.setObjectName(u"select_source_dir")
        self.select_source_dir.setMinimumSize(QSize(100, 30))

        self.horizontalLayout.addWidget(self.select_source_dir)

        self.source_dir_line = QLineEdit(Form)
        self.source_dir_line.setObjectName(u"source_dir_line")
        self.source_dir_line.setMinimumSize(QSize(200, 30))
        self.source_dir_line.setReadOnly(True)

        self.horizontalLayout.addWidget(self.source_dir_line)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.select_target_dir = QPushButton(Form)
        self.select_target_dir.setObjectName(u"select_target_dir")
        self.select_target_dir.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_2.addWidget(self.select_target_dir)

        self.target_dir_line = QLineEdit(Form)
        self.target_dir_line.setObjectName(u"target_dir_line")
        self.target_dir_line.setMinimumSize(QSize(200, 30))
        self.target_dir_line.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.target_dir_line)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.progress_bar = QProgressBar(Form)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setValue(24)

        self.horizontalLayout_3.addWidget(self.progress_bar)

        self.excute = QPushButton(Form)
        self.excute.setObjectName(u"excute")
        self.excute.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_3.addWidget(self.excute)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.progress_info_text = QPlainTextEdit(Form)
        self.progress_info_text.setObjectName(u"progress_info_text")
        self.progress_info_text.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.progress_info_text)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"hardlink", None))
        self.select_file_button.setText(QCoreApplication.translate("Form", u"\u5355\u6587\u4ef6", None))
        self.select_dir_button.setText(QCoreApplication.translate("Form", u"\u76ee\u5f55", None))
        self.select_source_dir.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6e90\u76ee\u5f55", None))
        self.select_target_dir.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u76ee\u6807\u76ee\u5f55", None))
        self.excute.setText(QCoreApplication.translate("Form", u"\u6267\u884c", None))
    # retranslateUi

