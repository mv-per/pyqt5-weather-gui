import requests, json

import mydata
import weatherDialog

# System imports
import sys


from PyQt5.QtWidgets import  QApplication




if __name__ == '__main__':
    app = QApplication(sys.argv)
    Interface = weatherDialog.WeatherGUI()
    Interface.show()
    sys.exit(app.exec_())

