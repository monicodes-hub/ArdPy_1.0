# use firmata standard

from pyfirmata2 import Arduino
import time
import tkinter as tk

# CREAMOS LA PANTALLA
tela = tk.Tk()                                      # creamos el objeto, es decir, la pantalla (tela) que se abre al ejecutar el programa
# tela.config(width=380, height=200)                  # si queremos definir alto y ancho de la pantalla
tela.state('zoomed')                                # si queremos que abra pantalla completa
tela.config(background='black')                     # color de fondo de la pantalla
tela.title("LED's CONTROL")                         # le damos un nombre a la pantalla (si no lo cambiamos, sale como "tk" por defecto)

# seleccionar placa y su puerto
board = Arduino('com3')

#definir los pins en los que están los leds conectados como outputs 
blue_pin = board.get_pin('d:10:o')
green_pin = board.get_pin('d:11:o')
yellow_pin = board.get_pin('d:12:o')
red_pin = board.get_pin('d:13:o')

def blue_on():
    blue_pin.write(1)
def green_on():
    green_pin.write(1)
def yellow_on():
    yellow_pin.write(1)
def red_on():
    red_pin.write(1)
    
def blue_off():
    blue_pin.write(0)
def green_off():
    green_pin.write(0)
def yellow_off():
    yellow_pin.write(0)
def red_off():
    red_pin.write(0)

# CREAR LOS BOTONES
# le damos un nombre a cada botón + definimos su ancho (width) + programamos su acción previamente definidas (command)
b1 = tk.Button(tela, text="ACENDER AZUL", width=20, font=('arial', 12), command=lambda:blue_on())
b1.place(x=50,y=50)                                 # ubicamos el botón en la pantalla

b2 = tk.Button(tela, text="APAGAR AZUL", width=20, font=('arial', 12), command=lambda:blue_off())
b2.place(x=350,y=50)                                 # ubicamos el botón en la pantalla

b3 = tk.Button(tela, text="ACENDER VERDE", width=20, font=('arial', 12), command=lambda:green_on())
b3.place(x=50,y=150)                                 # ubicamos el botón en la pantalla

b4 = tk.Button(tela, text="APAGAR VERDE", width=20, font=('arial', 12), command=lambda:green_off())
b4.place(x=350,y=150)                                 # ubicamos el botón en la pantalla

b5 = tk.Button(tela, text="ACENDER AMARELO", width=20, font=('arial', 12), command=lambda:yellow_on())
b5.place(x=50,y=250)                                 # ubicamos el botón en la pantalla

b6 = tk.Button(tela, text="APAGAR AMARELO", width=20, font=('arial', 12), command=lambda:yellow_off())
b6.place(x=350,y=250)                                 # ubicamos el botón en la pantalla

b7 = tk.Button(tela, text="ACENDER VERMELHO", width=20, font=('arial', 12), command=lambda:red_on())
b7.place(x=50,y=350)                                 # ubicamos el botón en la pantalla

b8 = tk.Button(tela, text="APAGAR VERMELHO", width=20, font=('arial', 12), command=lambda:red_off())
b8.place(x=350,y=350)                                 # ubicamos el botón en la pantalla

# BUCLE DE LA PANTALLA
tela.mainloop()