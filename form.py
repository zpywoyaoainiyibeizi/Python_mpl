# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
import os
import pandas as pd


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)


class Dialog2(QDialog):
    # 定义界面---------数据处理界面按钮格式和槽函数连接
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(520, 412)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(30, 40, 161, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(210, 40, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(30, 120, 261, 251))
        self.textEdit.setObjectName("textEdit")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(330, 120, 101, 20))
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 340, 81, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 340, 81, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.retranslateUi(Dialog)
        self.pushButton_3.clicked.connect(Dialog.close)
        self.pushButton.clicked.connect(self.daoru)
        self.pushButton_2.clicked.connect(self.split)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # 定义界面---------数据处理界面槽函数名称
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "实物验收统计"))
        self.pushButton.setText(_translate("Dialog", "导入文件"))

        self.pushButton_2.setText(_translate("Dialog", "计算"))
        self.pushButton_3.setText(_translate("Dialog", "关闭"))


        # 定义槽函数---------火车同行
    # 定义槽函数---------火车同行
    def daoru(self):
        openfile_name = QFileDialog.getOpenFileName(self, '选择文件', '', '')
        path_t = openfile_name[0]
        self.lineEdit.setText(path_t)
        val_huoche=path_t.split('/')[-1]
        self.textEdit.append("选中了:" + val_huoche)
    def split(self):
        if self.lineEdit.text().strip():
            name_list = []
            res_list = []

            xls_name = self.lineEdit.text().split('/')[-1]
            csv_name = 'pandas_csv.csv'
            csv_txt_name = 'pandas_csv_txt.txt'
            start = xls_name.split('.')[0]
            end = xls_name.split('.')[-1]

            csv_res_name = start
            # 读取excel文件前四列
            df = pd.read_excel(xls_name, usecols=[0, 1, 2, 3])
            # 生成csv文件(为了清洗)
            df.to_csv(csv_name)

            df_1 = pd.DataFrame(pd.read_csv(csv_name, header=1))
            # 去除空值列
            df_1.dropna(axis=0).to_csv(csv_txt_name, sep='\t')
            # 清洗数据
            with open(csv_txt_name, 'r', encoding='utf-8') as qingxi:
                with open(csv_res_name + '.txt', 'w', encoding='utf-8') as write_file:
                    for line in qingxi:
                        print(line)
                        row = line.split('\t')
                        index2 = row[2]
                        index3 = row[3]
                        index4 = row[4]
                        index5 = row[5]
                        if index2 == '品名':
                            continue
                        else:
                            write_line = index2 + '\t' + index3 + '\t' + index4 + '\t' + index5
                            write_file.write(write_line)
            # 菜品去重 添加进name_list
            with open(csv_res_name + '.txt', 'r', encoding='utf-8') as De_weighting:
                for line in De_weighting:
                    real_line = line.strip()
                    row = real_line.split('\t')
                    index0 = row[0]
                    if index0 not in name_list:
                        name_list.append(index0)
            # 将文件拆分为 每个菜品一个的小文件
            for name in name_list:
                with open(csv_res_name + '.txt', 'r', encoding='utf-8') as file:
                    with open(name + '.txt', 'w', encoding='utf-8') as write_file:
                        for line in file:
                            real_line = line.strip()
                            row = real_line.split('\t')
                            index0 = row[0]
                            if index0 == name:
                                write_file.write(line)
                            else:
                                continue
            shuliang_float = 0
            zongjia_float = 0
            # 统计菜品的数量和总价，求出均价
            for name in name_list:
                with open(name + '.txt', 'r', encoding='utf-8') as read_file:
                    for line in read_file:
                        real_line = line.strip()
                        row = real_line.split('\t')
                        index0 = row[0]
                        index1 = float(row[1])
                        index2 = float(row[2])
                        index3 = float(row[3])

                        shuliang_float = shuliang_float + index1
                        zongjia_float = zongjia_float + index3
                junjia = zongjia_float / shuliang_float
                Quantity = float('%.2f' % shuliang_float)
                Total_price = float('%.2f' % zongjia_float)
                Average_price = float('%.2f' % junjia)
                write_line = name + '\t' + str(Quantity) + '\t' + str(Average_price) + '\t' + str(Total_price)
                res_list.append(write_line)
                shuliang_float = 0
                zongjia_float = 0
                os.remove(name + '.txt')
            # 打印结果
            with open(csv_res_name + '_res.txt', 'w', encoding='utf-8') as write_file:
                for line in res_list:
                    write_file.write(line + '\n')
                os.remove(csv_name)
                os.remove(csv_txt_name)
                os.remove(csv_res_name + '.txt')

            self.textEdit.append("计算完毕！")
        else:
            self.textEdit.append("请选中文件！")
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Dialog2()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
