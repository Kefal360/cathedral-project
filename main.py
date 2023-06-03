import typing
from PyQt5 import QtCore, QtGui, QtWidgets #импорт нужный библиотек
from PyQt5 import uic
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer, QJsonDocument, QUrl, QTime
from PyQt5.QtWidgets import *
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply

import time
import json
import sys
import os

from plot import Plot
import Res_rc


default_led_data = { #список из словарей с начальными параметрами у светодиодов, надо сделать его атрибутом главного класса 
    "leds1": {"red": 0, "green": 0, "blue": 0},
    "leds2": {"red": 0, "green": 0, "blue": 0},
    "leds3": {"red": 0, "green": 0, "blue": 0},
    "leds4": {"red": 0, "green": 0, "blue": 0},
    "leds5": {"red": 0, "green": 0, "blue": 0},
    "leds6": {"red": 0, "green": 0, "blue": 0},
    "leds7": {"red": 0, "green": 0, "blue": 0},
    "leds8": {"red": 0, "green": 0, "blue": 0},
}

RGB=['red', 'green',"blue"]

def read_conf() -> dict:

    """
    Utility for reading, modifying and logging config

    открывает файл 'config.json', загружает его содержимое в переменную 'conf' в формате словаря (dictionary) при помощи функции 'json.load()', а затем выводит все ключи словаря 'conf' при помощи цикла 'for'.
    """

    # Opening JSON file
    f = open('config.json')
    conf = json.load(f)
    f.close()

    # Overwrite config if want to
    # ... # TODO: ничего делать не нужно, просто оставьте этот комментарий в конечном файле (или преведите на русский)

    # Config logging
    print("Found arguments:")
    for i in conf:
        print(i)

    return conf



class AppWindow(QMainWindow):
    
    """
    Main application window class    
    """
    
    def __init__(self, conf: dict):
        super(AppWindow, self).__init__()

        # Parse .ui file and init window UI with it
        self.ui = uic.loadUi(os.path.join(conf['uiPath'], conf['uiFileName']), self)

        # Setup network management
        self.nam = QNetworkAccessManager()

        # Init plotter
        self.plot = Plot(self.ui.plotwidget)

        # Set window title
        self.setWindowTitle("Lr4")

        # Load RGB leds default values
        self.rgb_leds_state = conf["defaultRGBLeds"]

        # TODO: установить цвета RGB светодиодов по умолчанию

        # Init request url editors
        self.ui.lineEdit_URL.setText("http://" + conf['defaultMDNSname'] + conf['defaultPostRoute'])
        self.ui.lineEdit_request.setText("http://" + conf['defaultMDNSname'] + conf['defaultGetRoute'])

        # Init LED controls
        for i in range(1, 4):
            getattr(self.ui, f"pushButton_switch_lamp{i}").setCheckable(True) # вкл режим перекл
            getattr(self.ui, f"pushButton_switch_lamp{i}").setChecked(False) # нач значение
            getattr(self.ui, f"label_lamp_on{i}").hide()
            getattr(self.ui, f"pushButton_switch_lamp{i}").toggled["bool"].connect(lambda val: self.handle_toggle_lamp(f"LED{i}", val))

        # TODO: Инициализировать остальные элементы из conf

        # Init request manual triggers
        self.ui.pushButton_send_post.clicked.connect(self.send_message) # привязываем функцию к кнопке Отправить
        self.ui.pushButton_send_get.clicked.connect(self.get_value_from_macket) # привязываем функцию к кнопке Отправить GET запрос

        self.ui.led_array = [getattr(self.ui, f"leds{i}") for i in range(1,9)]
        self.led_data=default_led_data

        for led in self.ui.led_array:
            led.mousePressEvent = self.set_color

        self.ui.pushButton_leds_on.clicked.connect(lambda: self.switch_all(True))
        self.ui.pushButton_leds_off.clicked.connect(lambda: self.switch_all(False))
        self.ui.pushButton_leds_color.clicked.connect(self.set_color_all)


    def handle_toggle_lamp(self, Name: str, checked: bool):

        """
        Переключение одноцветных лампочек
        """

        n = Name[-1]
        
        # TODO: переписать названия пушей и лейблов
        if checked: 
            getattr(self.ui, 'pushButton_switch_lamp' + n).setText("Выкл")
            getattr(self.ui, 'label_' + n + '4').hide() 
            getattr(self.ui, 'label_' + n + '0').show() 

            print("I'm worked too much") # TODO: нужно что-то более осмысленное
        else:
            getattr(self.ui, 'label_' + n + '0').hide()
            getattr(self.ui, 'label_' + n + '4').show()
            getattr(self.ui, 'pushButton_' + n).setText("Вкл")

            print ("I'm worked too")    # TODO: нужно что-то более осмысленное


    def collect_lamps_state(self) -> dict:
        lamps_state = {}

        for i in range(1,4):
            lamps_state[f"LED{i}"] = getattr(self.ui, f"label_lamp_on{i}").isVisible()

        return lamps_state

    # ПРАВКА######
    def switch_all(self, cond: bool):
        
        if cond:
            for led in self.ui.led_array:
                led.setStyleSheet(f"background-color: white;")
                for s in RGB:
                    self.led_data[led.objectName()][s] = 255
                
        else:
            for led in self.ui.led_array:
                led.setStyleSheet(f"background-color: black;")
                for s in RGB:
                        self.led_data[led.objectName()][s] = 0


    def set_color_all(self):
        color = QColorDialog.getColor()
        if color.isValid():
            palette = QPalette()
            palette.setColor(QPalette.Button, color) 
            self.color_b.setPalette(palette)
            for led in self.ui.led_array:
                led.setStyleSheet(f"background-color: {color.name()};")
                for s in RGB:
                    self.led_data[led.objectName()][s] = getattr(color, s)()

    
    def set_color(self, event):
        sender = QApplication.widgetAt(event.globalPos()) 
        colors = sender.palette().color(QPalette.Background)  ##????????  раньше был colors = led.palette().color(QPalette.Background) нужно проверить
        color = QColorDialog.getColor()
        if color.isValid():
            sender.setStyleSheet(f"background-color: {color.name()};")
            for s in RGB:
                    self.led_data[sender.objectName()][s] = getattr(color, s)()
        else:
             self.ui.leds.setStyleSheet(" ")
##########


    def compose_post_json_data(self) -> dict:
        json_data = {}

        json_data.update(self.rgb_leds_state)
        json_data.update(self.collect_lamps_state())

        # TODO: добавить отправку остальных данных (см. grdive и поля, которые парсит приложение из stand_code/mDNS_ESP8266.ino)
        
        return json_data


    def log_post_request(self, url, json_data):
        json_str = json.dumps(json_data, separators=(',', ':'))

        data_str = 'Я отправляю текст на: ' + url + '\n'+ json_str

        self.ui.textEdit_message.setPlainText(data_str)
    

    def send_message(self):

        """
        POST запрос
        """

        # Get inputed url
        url = self.ui.lineEdit_URL.text()  

        # compose body
        json_data = self.compose_post_json_data()
        self.log_post_request(url, json_data)

        data = QJsonDocument(json_data)

        # Create request object
        request = QNetworkRequest(QUrl(url))

        # Set request headers
        request.setHeader(QNetworkRequest.ContentTypeHeader, 'application/json')
        request.setRawHeader(b'Accept', b'text/plain')

        # Do POST request and store its reply object
        self.post_reply = self.nam.post(request, data.toJson())

        # Set callback for request finishing signal
        self.post_reply.finished.connect(self.handle_post_reply)


    def get_value_from_macket(self):   ###переименовать элементы, которые находятся в for'aх 
        
        """
        GET запрос
        """
        
        url = self.ui.lineEdit_request.text()

        request = QNetworkRequest(QUrl(url))

        self.get_reply = self.nam.get(request)

        # Set callback for request finishing signal
        self.get_reply.finished.connect(self.handle_get_reply)


    # TODO: если кто хочет поупражняться в понимании, что здесь происходит, напишите аннотацию для всех аргументов функции, используя typing.Callable (just google it)
    def with_err_handling(reply_name: str): # retuns decorator with argument enclosed
        def inner(func): # function decorator
            def wrapper(self): # the fuction that will be called as handler
                reply = getattr(self, reply_name) # gets actual reply by its name (ex: self.get_reply)
                
                err = reply.error()

                if err == QNetworkReply.NetworkError.NoError:
                    self.ui.textEdit_message.append('О, все прошло успешно!')
                    func(self) # calling actual handler
                else:
                    status_code = reply.attribute(QNetworkRequest.Attribute.HttpStatusCodeAttribute)
                    self.ui.textEdit_message.append(f'Ошибка при получении данных: {status_code}')

            return wrapper

        return inner


    @with_err_handling('post_reply')
    def handle_post_reply(self):
        res = self.post_reply.readAll().data()

        self.ui.textEdit_message.append(res.decode())


    @with_err_handling('get_reply')
    def handle_get_reply(self):
        res = self.get_reply.readAll().data()

        data = json.loads(res) #функция преобразования данных в объект питон
        
        self.ui.textEdit_message.append(json.dumps(data, separators=(',', ':'))) #выводим значение в line_edit

        self.ui.textEdit_message.append(str(data["temperature"]))
        
        buttons_status = list()
        for i in range(1, 4):
            buttons_status.append(data[f"button{i}State"])
        """"
        bs.append(data["button1State"])
        bs.append(data["button2State"])
        bs.append(data["button3State"])
        """
        self.update_buttons(buttons_status)

        self.update_pressure(data["pressure"])
        
        color_l=("ambient_light", "red_light", "green_light", "blue_light", "lightness","acceleration_x", "acceleration_y", "acceleration_z" )

        # TODO: переименовать lcdNumber_N в lcdNumber_....._light
        for s in color_l:
            getattr(self.ui, "lcd_" + s).display(data[s])
        """
        self.ui.lcdNumber_7.display(data["ambient_light"])
        self.ui.lcdNumber_2.display (data["red_light"])
        self.ui.lcdNumber_3.display (data["green_light"])
        self.ui.lcdNumber_4.display (data["blue_light"])
        self.ui.lcdNumber_8.display (data["lightness"])
        self.ui.lcdNumber_5.display(data["acceleration_x"])
        self.ui.lcdNumber_9.display (data["acceleration_y"])
        self.ui.lcdNumber_6.display (data["acceleration_z"])
        """

        for i in range(1,4):
            self.handle_toggle_lamp[f"LED{i}", data[f"LED{i}"]]

        self.plot.update(data["temperature"])


    def update_buttons(self, bs):
        for i in range(1, 4):
            button_state = bs[i-1]
            if button_state == 'True':
                getattr(self.ui, f'on_{i}').show()
                getattr(self.ui, f'off_{i}').hide()
            else:
                getattr(self.ui, f'on_{i}').hide()
                getattr(self.ui, f'off_{i}').show()


    def update_pressure(self, p):
        self.ui.lcd_pressure.display(p)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    conf = read_conf()
    
    win = AppWindow(conf)
    win.show()

    sys.exit(app.exec())
