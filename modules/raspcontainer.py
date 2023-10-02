import time

from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import QSignalMapper, QSize

import datetime
import sqlite3



from . ui_rasp_widget3 import Ui_rasp_widget
from . raspitem import *


class RaspWidget(QWidget):
    # delete = Sender(int)

    def __init__(self, id_widget: int, value: str, wdth: int, parent=None):
        super(RaspWidget, self).__init__(parent)
        self.ui = Ui_rasp_widget()
        self.ui.setupUi(self)
        self.id_widget = id_widget

        self.mainminsize = 90

        self.setMinimumSize(QSize(0, self.mainminsize))

#Текст "Занятий нет"

        self.nonerasp = QLabel()
        self.nonerasp.setText("Нет занятий")


# Соединение с БД

        connection = sqlite3.connect("shedule.sqlite")
        cur = connection.cursor()

        month = ['неизвестно', 'Января', 'Февраля', 'Марта', 'Апреля', 'Мая', 'Июня', 'Июля', 'Августа', 'Сентября',
                  'Октября', 'Ноября', 'Декабря']

        day = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Выходной']


        # print(id_widget)
        # print(day[id_widget])

        now = datetime.datetime.today()
        daystd = now.weekday()
        # nowmonth = now.month
        # nowyear = now.year

        if daystd == 6:
            dayd = now.day + 1
            dayy = dayd + id_widget
            v = 1
            date = now + datetime.timedelta(days=1 + id_widget)
        else:
            dayy = now.day - daystd + id_widget
            n = daystd - id_widget
            v = 1
            date = now + datetime.timedelta(days=-daystd + id_widget)

        # print(type(date))
        # print("weekday: ", month[date.month])

        datt = f"{date.day} {month[int(date.month)]}"
        self.ui.date.setText(datt)
        self.ui.day.setText(day[date.weekday()])



        # execute = f"""select * from shedule WHERE ("group" = '{value}' and "day" = '{date.day}' and "mount" = '{date.month}') """
        # cur.execute(execute)
        # shedule = cur.fetchall()

        execute = f"""select count(*) from shedule WHERE ("group" = '{value}' and "day" = '{date.day}' and "mount" = '{date.month}')"""
        cur.execute(execute)
        countpar = cur.fetchone()

        if countpar[0] == 0:
            self.ui.raspitemcontainer.addWidget(self.nonerasp)



# ВЫВОД ДАННЫХ О ПАРАХ В ЭТОТ ДЕНЬ
        self.c = 0
        while countpar[0] > self.c:
            self.mainminsize = self.mainminsize + 140
            raspitem = RaspItem(self.c, value, wdth, date)
            self.ui.raspitemcontainer.addWidget(raspitem)

            self.setMinimumSize(QSize(0, self.mainminsize))
            self.c += 1




    # self.ui.infotimerasp.setMinimumSize(QSize(0, self.mainminsize))

