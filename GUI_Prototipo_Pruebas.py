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

def close():
    window.destroy()

portada = Image.open("logo_prueba.png")
prtd_resize = portada.resize((250,100))
img_portada = ImageTk.PhotoImage(prtd_resize)

perfil_prueba = Image.open("perfil.png")
prfl_resize = perfil_prueba.resize((75,75))
prfil = ImageTk.PhotoImage(prfl_resize)


#Widgets (ESTA ES LA MANERA MÁS CAVERNICOLA QUE HAY, PERO ES LA UNICA QUE ME HA RESULTADO XDDDDDDDDD)
img_label = Label(window, image=img_portada)
exit_btn = Button(window, text="Salir de la Aplicación", command=close)
#Título de los Módulos
titulo1 = Label(window, text="Finanzas")
titulo1.config(font=("Arial",15))
titulo2 = Label(window, text="Comercial")
titulo2.config(font=("Arial",15))
titulo3 = Label(window, text="Operaciones")
titulo3.config(font=("Arial",15))
titulo4 = Label(window, text="Gestión")
titulo4.config(font=("Arial",15))
titulo5 = Label(window, text="Gestión del Capital Humano")
titulo5.config(font=("Arial",15))
titulo6 = Label(window, text="E-Commerce")
titulo6.config(font=("Arial",15))
titulo7 = Label(window, text="Capcitaciones")
titulo7.config(font=("Arial",15))
titulo8 = Label(window, text="Otros")
titulo8.config(font=("Arial",15))
#Imagén de los Módulos
img1 = Label(window, image=prfil)
img2 = Label(window, image=prfil)
img3 = Label(window, image=prfil)
img4 = Label(window, image=prfil)
img5 = Label(window, image=prfil)
img6 = Label(window, image=prfil)
img7 = Label(window, image=prfil)
img8 = Label(window, image=prfil)
#Texto de los Módulos
txt1 = Label(window, text="WHEN YOU SEE MY FACE,\n HOPE IT GIVES YOU HELL,\n HOPE IT GIVES YOU HELL")
txt2 = Label(window, text="BUCKLE UP,\n RUB A DUB DUB,\n YEAH YEAH,\n TOO LATE MY BABY")
txt3 = Label(window, text="WHATS THE WORST THAT I CAN SAY\n THINGS ARE BETTER IF I STAY\n SO LONG AND GOODNIGHT")
txt4 = Label(window, text="WHOOOAA\n WHATEVER MAKES YOU BRAG,\n BUT I GOT HIM WHERE I WANT HIM NOW")
txt5 = Label(window, text="COME, BREAK ME DOWN\n BURY ME, BURY ME\n I AM FINISHED WITH YOU")
txt6 = Label(window, text="IVE BECOME SO NUMB\n I CANT FELL YOU THERE\n BECOME SO TIRED\n SO MUCH MORE AWARE")
txt7 = Label(window, text="IT JUST TAKE SOME TIME\n LITTLE GIRL YOU ARE\n IN THE MIDDLE OF THE RIDE")
txt8 = Label(window, text="IF I GO CRAZY\n THEN WILL YOU STILL\n CALL ME SUPERMAN?")
#Botón de los Módulos
btn1 = Button(window, text="Ingresar")
btn2 = Button(window, text="Ingresar")
btn3 = Button(window, text="Ingresar")
btn4 = Button(window, text="Ingresar")
btn5 = Button(window, text="Ingresar")
btn6 = Button(window, text="Ingresar")
btn7 = Button(window, text="Ingresar")
btn8 = Button(window, text="Ingresar")

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