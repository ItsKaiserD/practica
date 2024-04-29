# Tkinter va a ser la libreria que usaré por ahora (y ojala para siempre) para la GUI
from tkinter import *
# PILLOW para el uso de imagenes
from PIL import Image, ImageTk

# Creamos la ventana principal
window = Tk()
#Título de la Ventana
window.title("PVV INGENIERIA")
#Configuramos para que el tamaño sea reajustable o no
window.resizable(width="true", height="true")

#Definimos una función para cerrar la interfaz
def close():
    window.destroy()

#Abrimos una imagen que se usara como logo en la esquina de la pantalla, para luego 
#reajustar su tamaño más que nada para que quepa bien en la ventana. 
portada = Image.open("logo_prueba.png")
prtd_resize = portada.resize((250,100))
img_portada = ImageTk.PhotoImage(prtd_resize)

#Abrimos otra imagen que voy a usar como placeholder para los diversos módulos, en los siguientes días 
#estaré trabajando en buscar o hacer las fotos necesarias.
perfil_prueba = Image.open("perfil.png")
prfl_resize = perfil_prueba.resize((75,75))
prfil = ImageTk.PhotoImage(prfl_resize)

#ESTA ES POSIBLEMENTE LA FORMA MÁS BRUTA DE HACER ESTE PROYECTO, PERO DE QUE FUNCIONA, FUNCIONA
#Widgets Principales
img_label = Label(window, image=img_portada, background="yellow")
exit_btn = Button(window, text="Salir de la Aplicación", command=close)
exit_btn.config(background="yellow", activebackground="blue")
midlbl1 = Label(window, background="yellow")
midlbl2 = Label(window, background="yellow")

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

#Imagenes de los Módulos
img1 = Label(window, image=prfil)
img2 = Label(window, image=prfil)
img3 = Label(window, image=prfil)
img4 = Label(window, image=prfil)
img5 = Label(window, image=prfil)
img6 = Label(window, image=prfil)
img7 = Label(window, image=prfil)
img8 = Label(window, image=prfil)

#Texto Descriptivo de los Módulos de los Módulos
txt1 = Label(window, text="WHEN YOU SEE MY FACE,\n HOPE IT GIVES YOU HELL,\n HOPE IT GIVES YOU HELL")
txt2 = Label(window, text="BUCKLE UP,\n RUB A DUB DUB,\n YEAH YEAH,\n TOO LATE MY BABY")
txt3 = Label(window, text="WHATS THE WORST THAT I CAN SAY\n THINGS ARE BETTER IF I STAY\n SO LONG AND GOODNIGHT")
txt4 = Label(window, text="WHOOOAA\n WHATEVER MAKES YOU BRAG,\n BUT I GOT HIM WHERE I WANT HIM NOW")
txt5 = Label(window, text="COME, BREAK ME DOWN\n BURY ME, BURY ME\n I AM FINISHED WITH YOU")
txt6 = Label(window, text="IVE BECOME SO NUMB\n I CANT FELL YOU THERE\n BECOME SO TIRED\n SO MUCH MORE AWARE")
txt7 = Label(window, text="IT JUST TAKE SOME TIME\n LITTLE GIRL YOU ARE\n IN THE MIDDLE OF THE RIDE")
txt8 = Label(window, text="IF I GO CRAZY\n THEN WILL YOU STILL\n CALL ME SUPERMAN?")

#Botón de los Módulos
btn1 = Button(window, text="Ingresar", background="yellow", activebackground="blue")
btn2 = Button(window, text="Ingresar", background="yellow", activebackground="blue")
btn3 = Button(window, text="Ingresar", background="yellow", activebackground="blue")
btn4 = Button(window, text="Ingresar", background="yellow", activebackground="blue")
btn5 = Button(window, text="Ingresar", background="yellow", activebackground="blue")
btn6 = Button(window, text="Ingresar", background="yellow", activebackground="blue")
btn7 = Button(window, text="Ingresar", background="yellow", activebackground="blue")
btn8 = Button(window, text="Ingresar", background="yellow", activebackground="blue")

#Configuración de las Columnas y Filas de la ventana 
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

#Inserción de los Widgets 
img_label.grid(column=0, row=0, sticky="nsew")
midlbl1.grid(column=1, row=0, sticky="nsew")
midlbl2.grid(column=2, row=0, sticky="nsew")
exit_btn.grid(column=3, row=0, sticky="nsew")
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