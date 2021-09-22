import os
import ctypes
from PyQt5.uic import loadUi

import weather_API_script
from operate_on_db import weatherGUI_database

# Third part imports
from PyQt5.QtGui import QStandardItemModel, QPixmap, QIcon, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import \
    QDialog, QMessageBox, QMainWindow, QApplication, \
    QTreeView, QTableWidget, QTableWidgetItem,\
    QWidget, QPushButton, QInputDialog




class WeatherGUI(QDialog):

    def __init__(self):
        QMainWindow.__init__(self)
        loadUi("WeatherGUI.ui", self)

        self.API_KEY = None
        self.city_id = None
        self.country = None
        self.city = None

        self.comboBox.clear()

        #load database
        self.db = weatherGUI_database("dev\city_database\data.db", "city_list")

        #add countries to comboBox
        self.comboBox.clear()       # delete all items from comboBox
        self.comboBox.addItems(self.db.load_countries()) # add the actual content of self.comboData
        self.comboBox.setEnabled(True)
        self.comboBox.currentTextChanged.connect(self.__get_country)

        self.comboBox_2.currentTextChanged.connect(self.__get_city)


        self.pushButton.setEnabled(False)
        self.pushButton.clicked.connect(self.__load_weather)


    def __update_interface(self):
        self.label_11.setText(weather_API_script.weather.sky_description)
        # self.label_11.setText(weather_API_script.weather.sky_description)
    
    def __load_weather(self):
        self.API_KEY = self.textEdit_6.toPlainText()
        self.city_id = self.db.load_city_id(self.city, self.country)
        # print(self.API_KEY, self.city_id)
        weather_API_script.get_weather(self.API_KEY, int(float(self.city_id)))
        self.__update_interface()

    def __get_city(self, city):

        self.city = city

    def __get_country(self, country):

        self.country = country
        self.comboBox_2.clear()
        self.comboBox_2.addItems(self.db.load_cities(self.country))
        self.comboBox_2.setEnabled(True)

        self.pushButton.setEnabled(True)



        



    def keyPressEvent(self, e):
        if e.key() == Qt.Key_F11:
            if self.isMaximized():
                self.showNormal()
                
                # self.mdiArea.resize(self.size())
            else:
                self.showMaximized()
                # self.mdiArea.resize(self.size())


if __name__ == "main":
    pass