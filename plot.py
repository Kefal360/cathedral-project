from PyQt5.QtWidgets import QGridLayout

import pyqtgraph as pg



class Plot():

    """
    QT bar plot drawing class
    """

    def __init__(self, widget, arr_len = 20, default_val = 20, initial_array = []):
        if initial_array:
            self.__arr_vals = initial_array
            arr_len = len(initial_array)
        else:
            self.__arr_vals = [default_val] * arr_len

        self.__x = list(range(1, arr_len + 1))

        self.__plot = pg.plot() #создает объект PlotWidget из библиотеки PyqtGraph
        #PlotWidget — это один из базовых конструктовров класса pyqtgraph, отвечающий за работу с 
        #виджетами, то есть элементами интерфейса, выводящими небольшую информацию

        self.__redraw_plot()
        
        # Создаём grid layout, который отвечает за положение элемента
        layout = QGridLayout()
        layout.addWidget(self.__plot, 0,0)
        widget.setLayout(layout)


    def update(self, newVal: int):
        arr_vals = self.__arr_vals

        arr_vals.pop(0)
        arr_vals.append(newVal)

        self.__redraw_plot()


    def __redraw_plot(self):
        plot = self.__plot

        bargraph = pg.BarGraphItem(x = self.__x, height = self.__arr_vals, width = 0.6, brush ='g')
        plot.clear()
        plot.addItem(bargraph)