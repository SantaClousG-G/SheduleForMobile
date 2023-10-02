from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
# from PySide6.QtCore import Slot, Signal

import datetime
import sqlite3

from . ui_rasp_item import Ui_rasp_item

from . ui_main3 import Ui_MainWindow


class RaspItem(QWidget):

    def __init__(self, id_widget: int, value: str, wdth: int, date: datetime.datetime, parent=None):
        super(RaspItem, self).__init__(parent)
        # self.ui = Ui_MainWindow()
        # mainwidgets = self.ui
        self.ui = Ui_rasp_item()
        self.ui.setupUi(self)
        self.id_widget = id_widget
        widget = self.ui
# СОЕДИНЕНИЕ С БД
        connection = sqlite3.connect("shedule.sqlite")
        cur = connection.cursor()

        # execute = f"""select * from shedule WHERE ("group" = '{value}' and "day" = '{date.day}' and "mount" = '{date.month}') """
        execute = f"""SELECT * from shedule inner join tabletime where (tabletime.ROWID = shedule.time  and "group" = '{value}' and "day" = '{date.day}' and "mount" = '{date.month}') ORDER BY time """
        cur.execute(execute)
        shedule = cur.fetchall()

        execute = f"""select count(*) from shedule WHERE ("group" = '{value}' and "day" = '{date.day}' and "mount" = '{date.month}')"""
        cur.execute(execute)
        countpar = cur.fetchone()
        sh = shedule[id_widget]
        # print(sh, ' - ', sh[9])
        widget.namofpar.setText(str(sh[3]))
        widget.time.setText(str(sh[9]))
        widget.type.setText(str(sh[5]))
        widget.cabinet.setText(str(sh[6]))
        widget.prepod.setText(str(sh[7]))
        widget.typegrp.setText(str(sh[8]))
        widget.counttask.setText(str(sh[4]))

        # widget.btn_delete.clicked.connect(lambda d:      self.test)

        # self.btn_delete = QtWidgets.QPushButton(self.maininforrasp)
        # self.btn_delete.setGeometry(QtCore.QRect(260, 20, 25, 25))
        # self.btn_delete.setObjectName(f"btn_delete_{id_widget}")
        # widget.btn_delete.setMinimumWidth(wdth)

    def test(self):
        print("test")
