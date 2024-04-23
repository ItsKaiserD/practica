# Tkinter va a ser la libreria que usaré por ahora (y ojala para siempre) para la GUI
from tkinter import *
# PILLOW para el uso de imagenes
from PIL import Image, ImageTk

# Creamos la ventana principal y le ponemos título 
window = Tk()
window.title("PVV INGENIERIA")
# RECORDAD REVISAR LO DEL ICONO PARA LA VENTANA 

#Probando distintos tamaños de pantalla
window.geometry("1080x720")

#Imagen de "Portada" y su ajuste de tamaño 
img_portada = Image.open("logo_prueba.png")

resize_portada = img_portada.resize((250, 100))

img = ImageTk.PhotoImage(resize_portada)

label_portada = Label(image=img)

#Función para cerrar la aplicación 
def cerrar():
    window.destroy()

#Botón que Cierra la Aplicación 
close = Button(window, text="Salir de la Aplicación", padx=12, pady=12, command=cerrar)

#Colocación de los widgets en la pantalla; tengo que configurar bien la posición del botón de cerrado
close.grid(sticky="E")
label_portada.grid(row=0, column=0, columnspan=2)

#Mainloop para abrir la aplicación
window.mainloop()