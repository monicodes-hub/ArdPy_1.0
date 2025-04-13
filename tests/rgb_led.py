#usar con firmata1 en arduino (firmata standard)

from pyfirmata2 import Arduino
import tkinter as tk

# Conectar con el puerto serial donde está conectado tu Arduino
board = Arduino('COM3')  # Cambia 'COM3' por el puerto correspondiente en tu máquina

# Definir los pines a los que están conectados los LEDs RGB (estos son PWM)
RED_PIN = 3     # Rojo
GREEN_PIN = 5  # Verde
BLUE_PIN = 6   # Azul

# Inicializar los pines como salida PWM
red = board.get_pin('d:3:p')  # d:9:p significa "digital pin 9 con PWM"
green = board.get_pin('d:5:p')
blue = board.get_pin('d:6:p')

# Función para cambiar el color
def set_color(red_value, green_value, blue_value):
    red.write(red_value)
    green.write(green_value)
    blue.write(blue_value)

# Funciones para cambiar los colores con los botones
def red_on():
    set_color(red_slider.get(), 0, 0)  # Rojo con intensidad del slider
    print(f"Color: Rojo, Intensidad: {red_slider.get()}")

def green_on():
    set_color(0, green_slider.get(), 0)  # Verde con intensidad del slider
    print(f"Color: Verde, Intensidad: {green_slider.get()}")

def blue_on():
    set_color(0, 0, blue_slider.get())  # Azul con intensidad del slider
    print(f"Color: Azul, Intensidad: {blue_slider.get()}")

def off():
    set_color(0, 0, 0)  # Apagar
    print("Color: Apagado")

# Crear la ventana principal con Tkinter
root = tk.Tk()
root.title("Control LED RGB con Intensidad")

# Crear los botones para cambiar el color
btn_red = tk.Button(root, text="Rojo", bg="red", fg="white", command=red_on, width=20)
btn_red.pack(pady=10)

btn_green = tk.Button(root, text="Verde", bg="green", fg="white", command=green_on, width=20)
btn_green.pack(pady=10)

btn_blue = tk.Button(root, text="Azul", bg="blue", fg="white", command=blue_on, width=20)
btn_blue.pack(pady=10)

btn_off = tk.Button(root, text="Apagar", bg="gray", fg="white", command=off, width=20)
btn_off.pack(pady=10)

# Crear sliders para ajustar la intensidad de los colores
red_slider = tk.Scale(root, from_=0, to=1, orient="horizontal", resolution=0.01, label="Intensidad Rojo")
red_slider.set(0)  # Valor inicial
red_slider.pack(pady=10)

green_slider = tk.Scale(root, from_=0, to=1, orient="horizontal", resolution=0.01, label="Intensidad Verde")
green_slider.set(0)  # Valor inicial
green_slider.pack(pady=10)

blue_slider = tk.Scale(root, from_=0, to=1, orient="horizontal", resolution=0.01, label="Intensidad Azul")
blue_slider.set(0)  # Valor inicial
blue_slider.pack(pady=10)

# Ejecutar la interfaz gráfica
root.mainloop()

# Después de cerrar la ventana, apagar el LED
set_color(0, 0, 0)
board.exit()