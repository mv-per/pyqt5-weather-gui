from PyQt5.uic import loadUi

# import threading
import weather_API_script, mydata
from operate_on_db import weatherGUI_database

# Third part imports
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import \
    QDialog, QMainWindow



### 

class WeatherGUI(QDialog):
    # global mydata
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi("WeatherGUI.ui", self)

        try:
            self.API_KEY = mydata.api
        except:
            self.API_KEY = None

        self.city_id = None
        self.country = None
        self.city = None

        #connects
        self.comboBox.currentTextChanged.connect(self.__get_country)
        self.comboBox_2.currentTextChanged.connect(self.__get_city)
        
        #load database
        self.db = weatherGUI_database("dev\city_database\data.db", "city_list")

        #add countries to comboBox
        self.comboBox.clear()       # delete all items from comboBox
        self.comboBox.addItems(self.db.load_countries()) # add the actual content of self.comboData
        self.comboBox.setEnabled(True)



        self.pushButton.setEnabled(False)
        self.pushButton.clicked.connect(self.__load_weather)


    def __update_interface(self, data):


        # self.label_11.setText(weather_API_script.weather.sky_description)
        # print(weather_API_script.weather.sky_description)
        self.label_11.setText(data['weather'][0]['description'] + " with feeling temp of {} °C".format(round(data["main"]["feels_like"]-273.15,2)))
        self.textEdit.setPlainText(str(round(data["main"]["temp"] - 273.15,2)))
        self.textEdit_2.setPlainText(str(data["main"]["pressure"]))
        self.textEdit_3.setPlainText(str(data["main"]["humidity"]))
        self.textEdit_4.setPlainText(str(data["wind"]["speed"]))
        # self.textEdit_5.setPlainText(str(data["main"]["humidity"]))

    
    def __load_weather(self):
        if self.textEdit_6.toPlainText() == "":
            print("API KEY NOT DEFINED, USING STORED API on mydata.py")
        else:
            self.API_KEY = self.textEdit_6.toPlainText()
        self.city_id = self.db.load_city_id(self.city, self.country)


        data = weather_API_script.get_weather(self.API_KEY, int(float(self.city_id)))

        cod = int(data['cod'])
        if cod == 401 or cod == 429 or cod == 404:
            print(f"ERROR: {data['cod']} - {data['message']}")
        else:
            # print(data)
            self.__update_interface(data)


        # print(self.API_KEY, self.city_id)
        # data = threading.Thread(target=weather_API_script.get_weather(self.API_KEY, int(float(self.city_id))))
        # data.start()
        # while True:
        #     if not data.is_alive():
        #         print(data)
        #         cod = int(data['cod'])
        #         if cod == 401 or cod == 429 or cod == 404:
        #             print(f"ERROR: {data['cod']} - {data['message']}")
        #         else:
        #             # print(data)
        #             self.__update_interface(data)
        #         break


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