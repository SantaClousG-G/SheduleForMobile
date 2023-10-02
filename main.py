# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import platform
import sqlite3

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "90" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        # self.ui = Ui_rasp_widget()
        # self.ui.setupUi(self)
        # widgets1 = self.ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui
        self.counter: int = 0

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Расписание КемГУ"
        description = ""
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        widgets.titleRightInfo.setText("Главная")


        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_groups.clicked.connect(self.buttonClick)
        widgets.btn_schedule.clicked.connect(self.buttonClick)
        widgets.btn_rasp.clicked.connect(self.buttonClick)

        # LOGIN PAGE
        widgets.btn_loginpage.clicked.connect(self.buttonClick)
        widgets.btn_login.clicked.connect(self.buttonClick)

        # LOGOUT MSGBOX
        widgets.btn_logout.clicked.connect(self.buttonClick)
        widgets.btn_LogoutYes.clicked.connect(self.buttonClick)
        widgets.btn_LogoutNo.clicked.connect(self.buttonClick)

        widgets.btn_editsh.clicked.connect(self.buttonClick)
        widgets.btn_delsh.clicked.connect(self.buttonClick)

        # ADMIN BUTTONS
        widgets.btn_save.clicked.connect(self.buttonClick)
        widgets.btn_refresh.clicked.connect(self.buttonClick)
        widgets.btn_delete_updt.clicked.connect(self.buttonClick)
        widgets.btn_refresh_updt.clicked.connect(self.buttonClick)

        widgets.comboBoxGroup_updt.activated.connect(self.hidemsgdel)
        widgets.comboBoxTime_updt.activated.connect(self.hidemsgdel)
        widgets.comboBoxDay_updt.activated.connect(self.hidemsgdel)
        widgets.comboBoxMonth_updt.activated.connect(self.hidemsgdel)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        # widgets.stackedWidget.setCurrentWidget(widgets.page_2)
        # widgets.stackedWidget.setCurrentWidget(widgets.updtsh)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))



# КОРРЕКТНЫЙ ВЫВОД ТАБЛИЦЫ

        widgets.tableView.clicked.connect(self.addwidgetrasp)
        connection = sqlite3.connect("shedule.sqlite")
        cur = connection.cursor()
        execute = "select * from groups order by gruop"
        cur.execute(execute)
        groups = cur.fetchall()
        model = QStandardItemModel(len(groups), 1)
        for row, group in enumerate(groups):
            item = QStandardItem(group[0])
            model.setItem(row, 0, item)

        filtermode = QSortFilterProxyModel()
        filtermode.setSourceModel(model)
        filtermode.setFilterCaseSensitivity(Qt.CaseInsensitive)
        filtermode.setFilterKeyColumn(0)
        widgets.lineEdit.textChanged.connect(filtermode.setFilterRegularExpression)
        widgets.tableView.setModel(filtermode)
        widgets.tableView.setShowGrid(False)
        # print(widgets.tableView.showGrid())


    # BUTTONS CLICK
    # Post here your functions for clicked buttons

    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            widgets.titleRightInfo.setText("Главная")

        # SHOW WIDGETS PAGE
        if btnName == "btn_groups":
            widgets.stackedWidget.setCurrentWidget(widgets.groups)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            widgets.titleRightInfo.setText("Группы")


        # SHOW NEW PAGE
        if btnName == "btn_schedule":
            widgets.stackedWidget.setCurrentWidget(widgets.page) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU
            widgets.titleRightInfo.setText("Расписание")



        if btnName == "btn_rasp":
            widgets.stackedWidget.setCurrentWidget(widgets.login)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU
            widgets.titleRightInfo.setText("Вход")

        if btnName == "btn_loginpage":
            UIFunctions.toggleLeftBox(self, True)
            UIFunctions.resetStyle(self, btnName)
            widgets.stackedWidget.setCurrentWidget(widgets.login)
            widgets.titleRightInfo.setText("Вход")


        if btnName == "btn_login":
            try:
                login = widgets.lineLogin.text()
                passw = widgets.linePass.text()
                connection = sqlite3.connect("shedule.sqlite")
                cur = connection.cursor()
                execute = f"""select * from admins where ("login" = '{login}' and "pass" = '{passw}')"""
                cur.execute(execute)
                admin = cur.fetchone()
                # print(widgets.lineEdit_3.text())
                # print(widgets.lineEdit_2.text())
                # print('Здравствуйте ' + admin[3] + ' ' + admin[2])
                widgets.themeText.setText(f"Здравствуйте {admin[2]}")
                widgets.themeText.setWordWrap(True)
                print('Здравствуйте ' + admin[2])
                widgets.settingsTopBtn.setEnabled(True)
                widgets.settingsTopBtn.setMaximumSize(28, 28)
                widgets.settingsTopBtn.setMinimumSize(28, 28)

                widgets.stackedWidget.setCurrentWidget(widgets.home)
                UIFunctions.resetStyle(self, btnName)
                widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))
                widgets.titleRightInfo.setText("Главная")
                widgets.btn_rasp.setEnabled(False)
                widgets.btn_rasp.setMaximumSize(0, 45)
                widgets.btn_loginpage.setEnabled(False)
                widgets.btn_loginpage.setMaximumSize(0, 45)
                widgets.label_loginError.setMaximumSize(0, 25)


            except:
                widgets.label_loginError.setMaximumSize(16777215, 25)
                # login = "qwerty"
                # passw = "123"
                # connection = sqlite3.connect("shedule.sqlite")
                # cur = connection.cursor()
                # execute = f"""select * from admins where ("login" = '{login}' and "pass" = '{passw}')"""
                # cur.execute(execute)
                # admin = cur.fetchone()
                # # print(widgets.lineEdit_3.text())
                # # print(widgets.lineEdit_2.text())
                # # print('Здравствуйте ' + admin[3] + ' ' + admin[2])
                # widgets.themeText.setText(f"Здравствуйте {admin[2]}")
                # print('Здравствуйте ' + admin[2])
                # widgets.settingsTopBtn.setEnabled(True)
                # widgets.settingsTopBtn.setMaximumSize(28, 28)
                # widgets.settingsTopBtn.setMinimumSize(28, 28)


        def openCloseRightBox1():
            UIFunctions.toggleRightBox(self, True)

        if btnName == "btn_logout":
            widgets.topMenuMessageBox.setMaximumSize(200, 80)

        if btnName == "btn_LogoutYes":
            widgets.settingsTopBtn.setEnabled(False)
            widgets.settingsTopBtn.setMaximumSize(0, 0)
            widgets.settingsTopBtn.setMinimumSize(0, 0)
            widgets.topMenuMessageBox.setMaximumSize(19846, 0)
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            widgets.titleRightInfo.setText("Главная")
            UIFunctions.resetStyle(self, "btn_home")
            widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))
            openCloseRightBox1()
            widgets.btn_rasp.setEnabled(True)
            widgets.btn_rasp.setMaximumSize(16777215, 16777215)
            widgets.btn_loginpage.setEnabled(True)
            widgets.btn_loginpage.setMaximumSize(16777215, 16777215)

        if btnName == "btn_LogoutNo":
            widgets.topMenuMessageBox.setMaximumSize(19846, 0)

        if btnName =="btn_editsh":
            widgets.stackedWidget.setCurrentWidget(widgets.page_2)
            widgets.titleRightInfo.setText("Добавить расписание")
            openCloseRightBox1()
            UIFunctions.resetStyle(self, "btn_loginpage")
            self.comboboxes()

        if btnName == "btn_delsh":
            widgets.stackedWidget.setCurrentWidget(widgets.updtsh)
            widgets.titleRightInfo.setText("Удалить расписание")
            openCloseRightBox1()
            UIFunctions.resetStyle(self, "btn_loginpage")
            self.combodel()

        if btnName == "btn_refresh":
            self.comboboxes()

        if btnName == "btn_save":
            self.onActive()

        if btnName == "btn_refresh_updt":
            self.combodel()

        if btnName == "btn_delete_updt":
            self.deletesh()



        # PRINT BTN NAME
        print(f'Вы нажали кнопку:  "{btnName}" !!')


    def combodel(self):
        widgets.comboBoxGroup_updt.clear()
        widgets.comboBoxMonth_updt.clear()
        widgets.comboBoxDay_updt.clear()
        widgets.comboBoxTime_updt.clear()

        # COMBOBOXGROUP
        connection = sqlite3.connect("shedule.sqlite")
        cur = connection.cursor()
        execute = f"""select count(*) from groups"""
        cur.execute(execute)
        countgroups = cur.fetchone()
        execute = f"""select * from groups order by gruop"""
        cur.execute(execute)
        groups1 = cur.fetchall()
        groups = []
        c = 0
        while c < countgroups[0]:
            groupss1 = groups1[c]
            groups.append(groupss1[0])
            c = c + 1
        widgets.comboBoxGroup_updt.addItems(groups)

        # COMBOBOXMONTH
        month = []
        c = 1
        while c <= 12:
            month.append(str(c))
            c = c + 1
        widgets.comboBoxMonth_updt.addItems(month)

        # COMBOBOXMONTHDAY
        day = []
        c = 1
        while c <= 31:
            day.append(str(c))
            c = c + 1
        widgets.comboBoxDay_updt.addItems(day)

        # comboBoxTime
        time = []
        c = 1
        while c <= 7:
            time.append(str(c))
            c = c + 1
        widgets.comboBoxTime_updt.addItems(time)

        # dateEdit
        now = datetime.datetime.now()
        widgets.dateEdit_updt.setDate(now)

        cur.close()


    def deletesh(self):
        state = widgets.checkBox_updt.isChecked()
        if state == True:
            datee = widgets.dateEdit_updt.date()
            days = datee.day()
            months = datee.month()
        else:
            months = widgets.comboBoxMonth_updt.currentText()
            days = widgets.comboBoxDay_updt.currentText()
        groups = widgets.comboBoxGroup_updt.currentText()
        times = widgets.comboBoxTime_updt.currentText()

        connection = sqlite3.connect("shedule.sqlite")
        cur = connection.cursor()
        state = widgets.checkBox_updt_2.isChecked()
        if state == True:
            cur.execute(
                f"""delete from shedule WHERE "group" = '{groups}' and day = '{days}' and mount = '{months}' """)
            connection.commit()
        else:
            cur.execute(f"""delete from shedule WHERE "group" = '{groups}' and day = '{days}' and mount = '{months}' and time = '{times}'""")
            connection.commit()

        widgets.label_del_updt.setMaximumSize(19846, 15)

        connection.close()

    def hidemsgdel(self):
        widgets.label_del_updt.setMaximumSize(19846, 0)




    def comboboxes(self):
        #CLEAR COMBOBOXES
        widgets.comboBoxGroup.clear()
        widgets.comboBoxMonth.clear()
        widgets.comboBoxDay.clear()
        widgets.comboBoxItem.clear()
        widgets.comboBoxTime.clear()
        widgets.comboBoxTypeItem.clear()
        widgets.comboBoxCab.clear()
        widgets.comboBoxTypeGroup.clear()

        #COMBOBOXGROUP
        connection = sqlite3.connect("shedule.sqlite")
        cur = connection.cursor()
        execute = f"""select count(*) from groups"""
        cur.execute(execute)
        countgroups = cur.fetchone()
        execute = f"""select * from groups order by gruop"""
        cur.execute(execute)
        groups1 = cur.fetchall()
        groups = []
        c = 0
        while c < countgroups[0]:
            groupss1 = groups1[c]
            groups.append(groupss1[0])
            c = c + 1
        widgets.comboBoxGroup.addItems(groups)


        #COMBOBOXMONTH
        month = []
        c = 1
        while c <= 12:
            month.append(str(c))
            c = c + 1
        widgets.comboBoxMonth.addItems(month)

        #COMBOBOXMONTHDAY
        day = []
        c = 1
        while c <= 31:
            day.append(str(c))
            c = c + 1
        widgets.comboBoxDay.addItems(day)

        #comboBoxItem
        cur = connection.cursor()
        execute = f"""select count(*) from academicsubjects"""
        cur.execute(execute)
        countrow = cur.fetchone()
        execute = f"""select * from academicsubjects"""
        cur.execute(execute)
        subjects = cur.fetchall()
        item = []
        c = 0
        while c < countrow[0]:
            subject = subjects[c]
            item.append(subject[0])
            c = c + 1
        widgets.comboBoxItem.addItems(item)


        #comboBoxTime
        time = []
        c = 1
        while c <= 7:
            time.append(str(c))
            c = c + 1
        widgets.comboBoxTime.addItems(time)

        #comboBoxTypeItem
        TypeItem = ['Лекция', 'Практика']
        widgets.comboBoxTypeItem.addItems(TypeItem)

        #comboBoxCab
        cab = []
        c = 101
        while c <= 321:
            if c == 150:
                c = 201
            if c == 232:
                c = 301
            cab.append(str(c))
            c = c + 1
        widgets.comboBoxCab.addItems(cab)

        #comboBoxTypeGroup
        TypeGroup = ["Общая", "1-пр.", "2-пр."]
        widgets.comboBoxTypeGroup.addItems(TypeGroup)

        #dateEdit
        now = datetime.datetime.now()
        widgets.dateEdit.setDate(now)

        cur.close()


    def passs(self):
        print('Done')

    # COMMIT v Bazy
    def onActive(self):
        state = widgets.checkBox.isChecked()
        if state == True:
            datee = widgets.dateEdit.date()
            days = datee.day()
            months = datee.month()
        else:
            months = widgets.comboBoxMonth.currentText()
            days = widgets.comboBoxDay.currentText()
        groups = widgets.comboBoxGroup.currentText()
        item = widgets.comboBoxItem.currentText()
        times = widgets.comboBoxTime.currentText()
        typeitem = widgets.comboBoxTypeItem.currentText()
        cab = widgets.comboBoxCab.currentText()
        typegroup = widgets.comboBoxTypeGroup.currentText()
        # print(groups, months, days, item, times, typeitem, cab, typegroup)

        connection = sqlite3.connect("shedule.sqlite")
        cur = connection.cursor()
        cur.execute(f"""SELECT teacher from academicsubjects where academicsubject = '{item}'""")
        teacher = cur.fetchone()
        # print(item)
        # print(teacher[0])

        cur.execute(f"""SELECT * from shedule WHERE "group" = '{groups}' and day = '{days}' and mount = '{months}' and time = '{times}'""")
        Valid = cur.fetchall()
        if Valid == []:
            # print("insert")
            cur.execute(f"""INSERT INTO shedule('group','day','mount','para','time','type','cabinet', 'prepod', 'typegrp') VALUES("{groups}","{days}","{months}","{item}","{times}","{typeitem}","{cab}", "{teacher[0]}","{typegroup}")""")
            connection.commit()

        else:
            # print("update")
            cur.execute(f"""UPDATE shedule SET para = '{item}', type = '{typeitem}', cabinet = '{cab}', prepod = '{teacher[0]}', typegrp = '{typegroup}' WHERE "group" = '{groups}' and day = '{days}' and mount = '{months}' and time = '{times}' """)
            connection.commit()

        connection.close()


        #
        # item = 'test'
        # typeitem = 'kek2131'
        # cab = 201
        # teacher = 'ШИР'
        # typegroup = 'Общ'
        # groups = 'КС-981'
        # days = 30
        # months = 5
        # times = 4
        #
        # cur.execute(f"""UPDATE shedule SET 'group' = "{groups}",'day' = "{days}",'mount' = "{months}",'para' = "{item}",'time' = "{times}",'type' = "{typeitem}",'cabinet' = "{cab}", 'prepod' = "{teacher[0]}", 'typegrp' = "{typegroup}" """)
        # cur.execute(f"""UPDATE shedule SET para = '{item}', type = '{typeitem}', cabinet = '{cab}', prepod = '{teacher}', typegrp = '{typegroup}' WHERE "group" = '{groups}' and day = '{days}' and mount = '{months}' and time = '{times}' """)
        # connection.commit()
        # cur.execute(f"""INSERT INTO shedule('group','day','mount','para','time','type','cabinet', 'prepod', 'typegrp') VALUES("{groups}","{days}","{months}","{item}","{times}","{typeitem}","{cab}", "{teacher[0]}","{typegroup}")""")
        # connection.commit()



# ФУНКЦИЯ ВЫВОДА РАСПИСАНИЯ НА НОВОЙ СТРАНИЦЕ
# ///////////////////////////////////////////////////////////////

    def addwidgetrasp(self):
        btnName = "btn_schedule"
        widgets.stackedWidget.setCurrentWidget(widgets.page)
        UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
        widgets.btn_schedule.setStyleSheet(UIFunctions.selectMenu(widgets.btn_schedule.styleSheet()))  # SELECT MENU

        # BAD IDEA
        width = 0
        # if(widgets.settingsTopBtn.width() == 28):
        #     width = 25

        self.counter = 0
        #Удаление уже готовых виджетов
        while widgets.raspcontainer.count() > 0:
            item = widgets.raspcontainer.takeAt(0)
            item.widget().deleteLater()

        #Узнать группу на которую нажали
        index = (widgets.tableView.selectionModel().currentIndex())
        value = index.sibling(index.row(), index.column()).data()
        widgets.titleRightInfo.setText(value)

        #Вывод виджетов на страницу
        #ВЫВОД ВИДЖЕТОВ ДНЕЙ В ПРИЛОЖЕНИЕ

        while self.counter < 6:
            raspwidget = RaspWidget(self.counter, value, width)
            widgets.raspcontainer.addWidget(raspwidget)
            self.counter += 1


        # print('done')

# Функции чтобы проверить сигнал
# ///////////////////////////////////////////////////////////////
    def test(self):
        print("Done")


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Мышка: Левая кнопка')
        if event.buttons() == Qt.RightButton:
            print('Мышка: Правая кнопка')





# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     app.setWindowIcon(QIcon("icon.ico"))
#     window = MainWindow()
#     sys.exit(app.exec())


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    # MainWindow = QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    window = MainWindow()
    window.show()
    # MainWindow.show()
    sys.exit(app.exec())
