# USAR CON FIRMATA STANDARD CARGADO EN ARDUINO

#IMPORTAR LIBRERÍAS NECESARIAS
from pyfirmata2 import Arduino, util
import time
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

# CONECTAR CON LA PLACA ARDUINO INDICANDO EL PUERTO AL QUE ESTÁ CONECTADA
board = Arduino("COM3")

# -- Config Leds and Bottons --
# definir los pins en los que están los leds conectados como outputs (LEDS INDIVIDUALES)
blue_pin = board.get_pin('d:10:o')
green_pin = board.get_pin('d:11:o')
yellow_pin = board.get_pin('d:12:o')
red_pin = board.get_pin('d:13:o')

# Diccionario para almacenar el estado de cada LED
led_states = {"blue": False, "green": False, "yellow": False, "red": False}

# Función para alternar LEDs individuales
def toggle_led(color, pin, button):
    if led_states[color]:
        pin.write(0)  # Apagar LED
        button.config(bg="gray")  # Cambiar color del botón a apagado
        led_states[color] = False
    else:
        pin.write(1)  # Encender LED
        button.config(bg=color)  # Cambiar color del botón al color del LED
        led_states[color] = True

# Definir pines del LED RGB (PWM)
red_pwm = board.get_pin('d:3:p')
green_pwm = board.get_pin('d:5:p')
blue_pwm = board.get_pin('d:6:p')

# Función para cambiar el color del LED RGB
def set_color():
    r = red_slider.get() / 255  # Convertir a rango 0-1
    g = green_slider.get() / 255
    b = blue_slider.get() / 255
    red_pwm.write(r)
    green_pwm.write(g)
    blue_pwm.write(b)

# CREAR PANTALLA CON TKINTER
pantalla = tk.Tk()
pantalla.state("zoomed")
pantalla.title("LED's Control")
pantalla.config(background="black")

# Cargar y redimensionar la imagen
imagen_original = Image.open("C:/Users/Mónica/Documents/ArdPy/ArdPy_1.0/resources/images/background.png")
imagen_redimensionada = imagen_original.resize((1550, 800))  # Ajustamos al tamaño deseado
fondo = ImageTk.PhotoImage(imagen_redimensionada)  # Convertimos para Tkinter

# Crear el Label con la imagen de fondo
label_fondo = tk.Label(pantalla, image=fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)  # Ajusta la imagen a la ventana

# Cargar el archivo de imagen desde el disco.
icono = tk.PhotoImage(file="C:/Users/Mónica/Documents/ArdPy/ArdPy_1.0/resources/images/background.png")

# Establecerlo como ícono de la ventana.
pantalla.iconphoto(True, icono)

#CREAR BOTONES & SLIDERS

#LEDs individuales:

# Crear un Frame negro en la parte superior
header_frame = tk.Frame(pantalla, bg="black", width=175, height=270)
header_frame.place(x=30, y=30)

# Agregar el título dentro del Frame
titulo_leds = tk.Label(
    header_frame, 
    text="LED's", 
    font=("Arial", 14, "bold", "underline"),  # Fuente negrita y subrayada
    bg="black", 
    fg="white"
)
titulo_leds.place(x=60, y=10)

boton_blue = tk.Button(pantalla, text="BLUE", font=("Arial", 12), bg="gray",
                        width=12, command=lambda: toggle_led("blue", blue_pin, boton_blue))
boton_blue.place(x=60, y=90)

boton_green = tk.Button(pantalla, text="GREEN", font=("Arial", 12), bg="gray",
                         width=12, command=lambda: toggle_led("green", green_pin, boton_green))
boton_green.place(x=60, y=140)

boton_yellow = tk.Button(pantalla, text="YELLOW", font=("Arial", 12), bg="gray",
                          width=12, command=lambda: toggle_led("yellow", yellow_pin, boton_yellow))
boton_yellow.place(x=60, y=190)

boton_red = tk.Button(pantalla, text="RED", font=("Arial", 12), bg="gray",
                       width=12, command=lambda: toggle_led("red", red_pin, boton_red))
boton_red.place(x=60, y=240)

#LED RGB:

# Crear un Frame negro en la parte superior
header_frame = tk.Frame(pantalla, bg="black", width=175, height=270)
header_frame.place(x=235, y=30)

# Agregar el título dentro del Frame
titulo_rgb = tk.Label(
    header_frame, 
    text="RGB", 
    font=("Arial", 14, "bold", "underline"),  # Fuente negrita y subrayada
    bg="black", 
    fg="white"
)
titulo_rgb.place(x=65, y=10)

red_slider = tk.Scale(pantalla, from_=0, to=255, orient="horizontal", label="Red", font=("Arial", 10, "bold"), bg="red", fg="white", width=10, command=lambda x: set_color())
red_slider.place(x=270, y=80)
green_slider = tk.Scale(pantalla, from_=0, to=255, orient="horizontal", label="Green", font=("Arial", 10, "bold"), bg="green", fg="white", width=10, command=lambda x: set_color())
green_slider.place(x=270, y=150)
blue_slider = tk.Scale(pantalla, from_=0, to=255, orient="horizontal", label="Blue", font=("Arial", 10, "bold"), bg="blue", fg="white", width=10, command=lambda x: set_color())
blue_slider.place(x=270, y=220)

# Ejecutar la ventana
pantalla.mainloop()


