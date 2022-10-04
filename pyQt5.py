#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import datetime

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.content_save_location = './本文/'
        self.abstract_save_location = './摘要/'
        self.file_save_name = str(datetime.date.today())
        self.initUI()

    def initUI(self):
        self.setWindowTitle('馬董早')
        self.setGeometry(50, 50, 400, 400)
        self.setFixedSize(400, 400)

        layout = QGridLayout()
        self.setLayout(layout)

        self.text_label = QLabel('請貼上文字', self)
        self.text_label.setStyleSheet("color:blue")
        self.text_label.setFont(QFont('Arial', 12))
        # self.text_label.setFixedSize()

        # 題目貼上位置
        self.text_input = QTextEdit()

        self.content_label = QLabel('內文：', self)
        self.content_label.setFont(QFont('Arial', 12))

        self.abstract_label = QLabel('摘要：', self)
        self.abstract_label.setFont(QFont('Arial', 12))

        self.content_folder_label = QLabel(self.content_save_location, self)
        self.content_folder_label.setStyleSheet("color:gray")
        self.content_folder_label.setFont(QFont('Arial', 12))
        self.content_folder_label.setFixedWidth(100)

        self.abstract_folder_label = QLabel(self.abstract_save_location, self)
        self.abstract_folder_label.setStyleSheet("color:gray")
        self.abstract_folder_label.setFont(QFont('Arial', 12))
        self.abstract_folder_label.setFixedWidth(100)

        self.output_file = QLabel('檔名：', self)
        self.output_file.setFont(QFont('Arial', 12))

        self.file_name = QLineEdit(self)
        self.file_name.setText(self.file_save_name)
        self.file_name.setAlignment(Qt.AlignCenter)


        self.content_output_btn = QPushButton('本文儲存位置', self)
        self.content_output_btn.clicked.connect(self.ContentButtonClick)

        self.abstract_output_btn = QPushButton('摘要儲存位置', self)
        self.abstract_output_btn.clicked.connect(self.AbstractButtonClick)

        self.scrawler_btn = QPushButton('擷取全文', self)
        self.scrawler_btn.clicked.connect(self.scratchButtonClick)

        self.abstract_btn = QPushButton('擷取摘要', self)
        self.abstract_btn.clicked.connect(self.abstractButtonClick)

        self.reset_btn = QPushButton('返回預設值', self)
        self.reset_btn.clicked.connect(self.resetButtonClick)

        self.AllLayout(layout)

    def ContentButtonClick(self):
        folderPath = QtWidgets.QFileDialog.getExistingDirectory()  # 選取特定資料夾
        self.content_save_location = folderPath
        folder_split = folderPath.split('/')
        new_folder = folder_split[-2] + '/' + folder_split[-1]
        self.content_folder_label.setText(new_folder)
        print(folderPath)

    def AbstractButtonClick(self):
        folderPath = QtWidgets.QFileDialog.getExistingDirectory()  # 選取特定資料夾
        self.abstract_save_location = folderPath
        folder_split = folderPath.split('/')
        new_folder = folder_split[-2] + '/' + folder_split[-1]
        self.abstract_folder_label.setText(new_folder)
        print(folderPath)

    def scratchButtonClick(self):
        self.scrawler_btn.setText('文章擷取中...')
        self.scrawler_btn.setStyleSheet("background-color: silver")

    def abstractButtonClick(self):
        self.abstract_btn.setText('摘要擷取中...')
        self.abstract_btn.setStyleSheet("background-color: silver")

    def resetButtonClick(self):
        self.content_save_location = './本文/'
        self.content_folder_label.setText(self.content_save_location)
        self.abstract_save_location = './摘要/'
        self.abstract_folder_label.setText(self.abstract_save_location)
        self.file_save_name = str(datetime.date.today())
        self.file_name.setText(self.file_save_name)


    def openFolder(self):
        folderPath = QtWidgets.QFileDialog.getExistingDirectory()  # 選取特定資料夾
        print(folderPath)

    def AllLayout(self, layout):
        layout.addWidget(self.text_label, 1, 0, 1, 2)
        layout.addWidget(self.content_label, 0, 3, 1, 2)
        layout.addWidget(self.abstract_label, 1, 3, 1, 2)
        layout.addWidget(self.content_folder_label, 0, 5, 1, 4)
        layout.addWidget(self.abstract_folder_label, 1, 5, 1, 4)
        layout.addWidget(self.content_output_btn, 0, 10, 1, 2)
        layout.addWidget(self.abstract_output_btn, 1, 10, 1, 2)
        layout.addWidget(self.text_input, 2, 0, 10, 8)
        layout.addWidget(self.output_file, 2, 8, 1, 2)
        layout.addWidget(self.file_name, 2, 10, 1, 2)
        layout.addWidget(self.scrawler_btn, 10, 8, 1, 4)
        layout.addWidget(self.abstract_btn, 11, 8, 1, 4)
        layout.addWidget(self.reset_btn, 0, 0, 1, 2)

        # layout.addWidget()
        # layout.addWidget(self.mybutton, 50, 50, 1, 1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec_())