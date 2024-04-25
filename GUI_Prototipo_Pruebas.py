# Tkinter va a ser la libreria que usaré por ahora (y ojala para siempre) para la GUI
from tkinter import *
# PILLOW para el uso de imagenes
from PIL import Image, ImageTk

# Creamos la ventana principal
window = Tk()
#Se le asigna un tamaño inicial 
window.geometry("600x400")
#Se le pone un título a la ventana
window.title("PVV INGENIERIA")
#Configuramos para que el tamaño sea reajustable o no
window.resizable(width="true", height="true")

#Widgets (ESTA ES LA MANERA MÁS CAVERNICOLA QUE HAY, PERO ES LA UNICA QUE ME HA RESULTADO XDDDDDDDDD)
img_label = Label(window, text="Imagen Portada")
exit_btn = Label(window, text="Salir de la Aplicación")
#Título de los Módulos
titulo1 = Label(window, text="Titulo 1")
titulo2 = Label(window, text="Titulo 2")
titulo3 = Label(window, text="Titulo 3")
titulo4 = Label(window, text="Titulo 4")
titulo5 = Label(window, text="Titulo 5")
titulo6 = Label(window, text="Titulo 6")
titulo7 = Label(window, text="Titulo 7")
titulo8 = Label(window, text="Titulo 8")
#Imagén de los Módulos
img1 = Label(window, text="Imagen 1")
img2 = Label(window, text="Imagen 2")
img3 = Label(window, text="Imagen 3")
img4 = Label(window, text="Imagem 4")
img5 = Label(window, text="Imagen 5")
img6 = Label(window, text="Imagen 6")
img7 = Label(window, text="Imagen 7")
img8 = Label(window, text="Imagen 8")
#Texto de los Módulos
txt1 = Label(window, text="Texto 1")
txt2 = Label(window, text="Texto 2")
txt3 = Label(window, text="Texto 3")
txt4 = Label(window, text="Texto 4")
txt5 = Label(window, text="Texto 5")
txt6 = Label(window, text="Texto 6")
txt7 = Label(window, text="Texto 7")
txt8 = Label(window, text="Texto 8")
#Botón de los Módulos
btn1 = Button(window, text="Botón 1")
btn2 = Button(window, text="Botón 2")
btn3 = Button(window, text="Botón 3")
btn4 = Button(window, text="Botón 4")
btn5 = Button(window, text="Botón 5")
btn6 = Button(window, text="Botón 6")
btn7 = Button(window, text="Botón 7")
btn8 = Button(window, text="Botón 8")

#Configuración de las Columnas y Filas 
window.columnconfigure((0,1,2,3), weight=200)
window.rowconfigure(0, weight= 200)
window.rowconfigure(1, weight= 200)
window.rowconfigure(2, weight= 200)
window.rowconfigure(3, weight= 200)
window.rowconfigure(4, weight= 200)
window.rowconfigure(5, weight= 200)
window.rowconfigure(6, weight= 200)
window.rowconfigure(7, weight= 200)
window.rowconfigure(8, weight= 200)

#Insertar los Widgets
img_label.grid(column=0, row=0)
exit_btn.grid(column=3, row=0)
#Títulos
titulo1.grid(row=1, column=0)
titulo2.grid(row=1, column=1)
titulo3.grid(row=1, column=2)
titulo4.grid(row=1, column=3)
titulo5.grid(row=5, column=0)
titulo6.grid(row=5, column=1)
titulo7.grid(row=5, column=2)
titulo8.grid(row=5, column=3)
#Imagenes
img1.grid(row=2, column=0)
img2.grid(row=2, column=1)
img3.grid(row=2, column=2)
img4.grid(row=2, column=3)
img5.grid(row=6, column=0)
img6.grid(row=6, column=1)
img7.grid(row=6, column=2)
img8.grid(row=6, column=3)
#Texto
txt1.grid(row=3, column=0)
txt2.grid(row=3, column=1)
txt3.grid(row=3, column=2)
txt4.grid(row=3, column=3)
txt5.grid(row=7, column=0)
txt6.grid(row=7, column=1)
txt7.grid(row=7, column=2)
txt8.grid(row=7, column=3)
#Botones
btn1.grid(row=4, column=0)
btn2.grid(row=4, column=1)
btn3.grid(row=4, column=2)
btn4.grid(row=4, column=3)
btn5.grid(row=8, column=0)
btn6.grid(row=8, column=1)
btn7.grid(row=8, column=2)
btn8.grid(row=8, column=3)

#Mainloop para abrir la aplicación
window.mainloop()