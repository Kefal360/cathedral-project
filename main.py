import typing
from PyQt5 import QtCore, QtGui, QtWidgets #импорт нужный библиотек
from PyQt5 import uic
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtGui import QPixmap, QMouseEvent
from PyQt5.QtCore import QTimer, QJsonDocument, QUrl, QTime
from PyQt5.QtWidgets import *
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply

import time
import json
import sys
import os

from plot import Plot
import Res_rc

RGB = ['red', 'green',"blue"]

def read_conf() -> dict:
    """
    Utility for reading, modifying and logging config

    открывает файл 'config.json',
    загружает его содержимое в переменную 'conf' в формате словаря (dictionary) при помощи функции 'json.load()',
    а затем выводит все ключи словаря 'conf' при помощи цикла 'for'.
    """

    # Opening JSON file
    f = open('config.json')
    conf = json.load(f)
    f.close()

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
        self.plot = Plot(self.ui.plotwidget, initial_array=conf["temperature"])

        # Set window title
        self.setWindowTitle("Lr4")

        # Init request url editors
        self.ui.lineEdit_POST_URL.setText("http://" + conf['defaultMDNSname'] + conf['defaultPostRoute'])
        self.ui.lineEdit_GET_URL.setText("http://" + conf['defaultMDNSname'] + conf['defaultGetRoute'])

        # Init LED controls
        for i in range(1, 4):
            getattr(self.ui, f"pushButton_switch_lamp{i}").setCheckable(True) # вкл режим перекл
            self.handle_toggle_lamp(i, conf[f"LED{i}"])
            getattr(self.ui, f"pushButton_switch_lamp{i}").toggled["bool"].connect(lambda val, i=i: self.handle_toggle_lamp(i, val))

        # Setup request manual triggers
        self.ui.pushButton_send_post.clicked.connect(self.send_message) # привязываем функцию к кнопке Отправить
        self.ui.pushButton_send_get.clicked.connect(self.get_value_from_macket) # привязываем функцию к кнопке Отправить GET запрос

        # For convinience store RGB LED strip in list 
        self.ui.led_array = [getattr(self.ui, f"leds{i}") for i in range(1,9)]

        # Store RGB LEDs default values
        self.rgb_leds_state = conf["defaultRGBLeds"]

        self.update_colors(self.rgb_leds_state)

        self.update_buttons(self.convert_buttons_state(conf))

        # Init LCDs values
        self.update_lcds(conf)
        self.ui.lcd_temperature.display(conf["temperature"][-1])

        # Setup RGB LED stip click handlers
        for led in self.ui.led_array:
            led.mousePressEvent = self.set_color

        # Setup handlers for packet RGB LED changing  
        self.ui.pushButton_leds_on.clicked.connect(lambda: self.switch_all(True)) # обработка кнопк включения индикаторов
        self.ui.pushButton_leds_off.clicked.connect(lambda: self.switch_all(False)) # обработка кнопки выключения индикаторов
        self.ui.pushButton_leds_color.clicked.connect(lambda: self.set_color_all()) # обработка кнопки изменения цвета индикаторов 

        # Init timer and connect data fetching with interval from defaults
        self.timer = QTimer(self)
        self.timer.setInterval(conf["defaultUpdateInterval"])
        self.timer.timeout.connect(self.get_value_from_macket)

        # Init autoupdate interval input
        self.ui.spinBox_autoupdate.setValue(conf["defaultUpdateInterval"] // 1000)

        # Setup autoupdate interval updating on input change
        self.ui.spinBox_autoupdate.valueChanged.connect(lambda i: self.timer.setInterval(i * 1000))

        # Setup autoupdate toggler
        self.ui.checkBox_autoupdate.stateChanged.connect(self.handle_toggle_autoupdate)

        self.ui.checkBox_autoupdate.setChecked(conf["startWithAutoupdate"])


    def handle_toggle_autoupdate(self):
        """
        Toggles timer
        """

        if self.ui.checkBox_autoupdate.isChecked():
            interval_s = self.ui.spinBox_autoupdate.value()
            self.timer.start(interval_s * 1000)

            self.timer.timeout.emit() # Trigger timer event immediately
        else:
            self.timer.stop()

    def with_autosend(func):
        """
        Decorator for doing automatic post request after function invocation
        """

        def wrapper(self, *args, **kwargs): # the fuction that will be called as handler args - positional arguments, kwargs - named arguments
            func(self, *args, **kwargs) # calling actual handler

            if self.ui.checkBox_autoupdate.isChecked():
                self.send_message()

        return wrapper


    @with_autosend
    def handle_toggle_lamp(self, n: int, checked: bool):
        """
        Toggles lamps in interface
        """

        pushButton_switch_lamp = getattr(self.ui, f'pushButton_switch_lamp{n}')
        label_lamp_on = getattr(self.ui, f'label_lamp_on{n}')
        label_lamp_off = getattr(self.ui, f'label_lamp_off{n}')
        
        if checked: 
            pushButton_switch_lamp.setText("Выкл")
            pushButton_switch_lamp.setChecked(True)
            label_lamp_on.show() 
            label_lamp_off.hide()
        else:
            pushButton_switch_lamp.setText("Вкл")
            pushButton_switch_lamp.setChecked(False)
            label_lamp_on.hide()
            label_lamp_off.show()


    @with_autosend
    def switch_all(self, on: bool):
        """
        Switches all RGB LEDs in strip on or off
        """

        if on:
            for led in self.ui.led_array:
                self.paint_led_color(led, QColor(255, 255, 255))
        else:
            for led in self.ui.led_array:
                self.paint_led_color(led, QColor(0, 0, 0))


    @with_autosend
    def set_color_all(self):
        """
        Sets color using dialog for all RGB LEDs in strip
        """

        color = QColorDialog.getColor()

        if color.isValid():
            palette = QPalette()
            palette.setColor(QPalette.Button, color)
            self.ui.pushButton_leds_color.setPalette(palette)

            for led in self.ui.led_array:
                self.paint_led_color(led, color)


    @with_autosend
    def set_color(self, event: QMouseEvent):
        """
        Asks in dialog and updates color of single RGB LED
        """

        sender = QApplication.widgetAt(event.globalPos()) 
        colors = sender.palette().color(QPalette.Background)
        color = QColorDialog.getColor()
        if color.isValid():
            self.paint_led_color(sender, color)
        else:
            self.paint_led_color(sender, QColor(0, 0, 0))

    def paint_led_color(self, led: QLabel, color: QColor):
        """
        Actually sets RGB LED color in interface and state storage
        """

        led.setStyleSheet(f"background-color: rgb({','.join(map(lambda c: str(getattr(color, c)()), RGB))})")

        for c in RGB:
            self.rgb_leds_state[led.objectName()][c] = getattr(color, c)()


    def collect_lamps_state(self) -> dict[str, bool]:
        """
        Composes proper object structure with lamps state 
        """

        lamps_state = {}

        for i in range(1,4):
            lamps_state[f"LED{i}"] = getattr(self.ui, f"label_lamp_on{i}").isVisible()

        return lamps_state


    def compose_post_json_data(self) -> dict:        
        json_data = {}

        json_data.update(self.rgb_leds_state)
        json_data.update(self.collect_lamps_state())
        
        return json_data


    def log_post_request(self, url: str, json_data: dict):
        json_str = json.dumps(json_data, separators=(',', ':'))

        data_str = 'Я отправляю текст на: ' + url + '\n'+ json_str

        self.ui.textEdit_message.append(data_str)
    

    def with_cancel(reply_name: str): # retuns decorator with argument enclosed
        """
        Decorator for cancelling previous request of same type
        """
        def inner(func): # function decorator
            def wrapper(self): # the fuction that will be called as handler
                if hasattr(self, reply_name):
                    getattr(self, reply_name).abort() # abort currently pending request
                
                func(self) # calling actual handler
                
            return wrapper

        return inner

    @with_cancel('POST_reply')
    def send_message(self):
        """
        POST запрос
        """

        # Get inputed url
        url = self.ui.lineEdit_POST_URL.text()  

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
        self.POST_reply = self.nam.post(request, data.toJson())

        # Set callback for request finishing signal
        self.POST_reply.finished.connect(self.handle_post_reply)


    @with_cancel('GET_reply')
    def get_value_from_macket(self):
        """
        GET запрос
        """
        
        url = self.ui.lineEdit_GET_URL.text()

        request = QNetworkRequest(QUrl(url))

        self.GET_reply = self.nam.get(request)

        # Set callback for request finishing signal
        self.GET_reply.finished.connect(self.handle_get_reply)


    # TODO: если кто хочет поупражняться в понимании, что здесь происходит, напишите аннотацию для всех аргументов функции, используя typing.Callable (just google it)
    def with_err_handling(reply_name: str): # retuns decorator with argument enclosed
        """
        Decorator for error and cancellation of request handling
        """
        
        operation = reply_name.split('_')[0]
        def inner(func): # function decorator
            def wrapper(self): # the fuction that will be called as handler
                reply = getattr(self, reply_name) # gets actual reply by its name (ex: self.GET_reply)
                
                err = reply.error()

                if err == QNetworkReply.NetworkError.NoError:
                    self.ui.textEdit_message.append(f'О, {operation} запрос прошёл успешно!')
                    func(self) # calling actual handler
                elif err == QNetworkReply.NetworkError.OperationCanceledError:
                    self.ui.textEdit_message.append(f"{operation} запрос был отменён, так как не успел выполниться до нового вызова")
                elif err == QNetworkReply.NetworkError.TemporaryNetworkFailureError:
                    self.ui.textEdit_message.append(f"Произошла временная ошибка при {operation} запросе, повторите запрос ещё раз")
                else:
                    msg = f"Ошибка при {operation} запросе: "
                    if (err == QNetworkReply.NetworkError.ConnectionRefusedError 
                        or err == QNetworkReply.NetworkError.RemoteHostClosedError
                        or err == QNetworkReply.NetworkError.HostNotFoundError
                        or err == QNetworkReply.NetworkError.TimeoutError
                        or err == QNetworkReply.NetworkError.SslHandshakeFailedError
                        or err == QNetworkReply.NetworkError.NetworkSessionFailedError
                        or err == QNetworkReply.NetworkError.BackgroundRequestNotAllowedError
                        or err == QNetworkReply.NetworkError.TooManyRedirectsError
                        or err == QNetworkReply.NetworkError.InsecureRedirectError):
                        self.ui.textEdit_message.append(msg + 'не удалось установить подключение к серверу')
                    else:
                        status_code = reply.attribute(QNetworkRequest.Attribute.HttpStatusCodeAttribute)
                        self.ui.textEdit_message.append(msg + f'сервер вернул статус код {status_code}')

            return wrapper

        return inner #это не игрок в hearthstone


    @with_err_handling('POST_reply')
    def handle_post_reply(self):
        res = self.POST_reply.readAll().data()

        self.ui.textEdit_message.append(res.decode())


    @with_err_handling('GET_reply')
    def handle_get_reply(self):
        res = self.GET_reply.readAll().data()

        data = json.loads(res) #функция преобразования данных в объект питон
        
        self.ui.textEdit_message.append(json.dumps(data, separators=(',', ':'))) #выводим значение в line_edit

        # Update lamps
        for i in range(1,4):
            self.handle_toggle_lamp(i, data[f"LED{i}"])
        
        self.update_buttons(self.convert_buttons_state(data))
        
        # Update LCDs
        self.update_lcds(data)

        # Append dot to plot and set corresponding LCD
        self.plot.update(data["temperature"])
        self.ui.lcd_temperature.display(data["temperature"])

        self.update_colors(data)

    
    def convert_buttons_state(self, data: dict[str, bool]) -> list[bool]:
        buttons_status = list()
        for i in range(1, 4):
            buttons_status.append(data[f"button{i}State"])

        return buttons_status


    def update_lcds(self, data: dict):
        color_l=("ambient_light", "red_light", "green_light", "blue_light", "lightness", "acceleration_x", "acceleration_y", "acceleration_z", "pressure")

        for s in color_l:
            getattr(self.ui, "lcd_" + s).display(data[s])

    def update_buttons(self, bs: list[bool]):
        for i in range(1, 4):
            button_on = bs[i-1]

            label_tumbler_on = getattr(self.ui, f'label_tumbler_on{i}')
            label_tumbler_off = getattr(self.ui, f'label_tumbler_off{i}')
            
            if button_on:
                label_tumbler_on.show()
                label_tumbler_off.hide()
            else:
                label_tumbler_on.hide()
                label_tumbler_off.show()


    def update_colors(self, new_state: dict[str, dict[int]]):
        for name in self.rgb_leds_state.keys():
            self.rgb_leds_state[name] = new_state[name]
            self.paint_led_color(
                getattr(self.ui, name),
                QColor(*list(map(lambda c: new_state[name][c], RGB)))
            )



if __name__ == "__main__":
    app = QApplication(sys.argv)

    conf = read_conf()
    
    win = AppWindow(conf)
    win.show()

    sys.exit(app.exec())
