from tkinter import *
from PIL import Image, ImageTk
#----------------------------------------------------------------------
window = Tk()
window.title("PVV Ingenieria")
window.config(background="white")
#----------------------------------------------------------------------
portada = Image.open("pvv_logo.png")
resized = portada.resize((250,100))
img_portada = ImageTk.PhotoImage(resized)
portada_label = Label(window, image=img_portada, background="orange")
#----------------------------------------------------------------------
def close_window():
    window.destroy()
exit = Button(window, text="Salir de la Aplicación", command=close_window)
exit.config(background="orange", borderwidth=0, activebackground="orange", font=15)
#----------------------------------------------------------------------
midlbl1 = Label(window, background="orange")
midlbl2 = Label(window, background="orange")
#----------------------------------------------------------------------
finanzas_logo = Image.open("finanzas.png")
finanzas_rsize = finanzas_logo.resize((150,150))
finanzas_icon = ImageTk.PhotoImage(finanzas_rsize)

comercial_logo = Image.open("comercial.png")
comercial_rsize = comercial_logo.resize((150,150))
comercial_icon = ImageTk.PhotoImage(comercial_rsize)

operaciones_logo = Image.open("operaciones.png")
operaciones_rsize = operaciones_logo.resize((150,150))
operaciones_icon = ImageTk.PhotoImage(operaciones_rsize)

gestion_logo = Image.open("gestion.png")
gestion_rsize = gestion_logo.resize((150,150))
gestion_icon = ImageTk.PhotoImage(gestion_rsize)

caphumano_logo = Image.open("caphumano.png")
caphumano_rsize = caphumano_logo.resize((150,150))
caphumano_icon = ImageTk.PhotoImage(caphumano_rsize)

ecommerce_logo = Image.open("ecommerce.png")
ecommerce_rsize = ecommerce_logo.resize((150,150))
ecommerce_icon = ImageTk.PhotoImage(ecommerce_rsize)

capacitaciones_logo = Image.open("capacitaciones.png")
capacitaciones_rsize = capacitaciones_logo.resize((150,150))
capacitaciones_icon = ImageTk.PhotoImage(capacitaciones_rsize)

otros_logo = Image.open("otros.png")
otros_rsize = otros_logo.resize((150,150))
otros_icon = ImageTk.PhotoImage(otros_rsize)
#----------------------------------------------------------------------
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
#----------------------------------------------------------------------

#----------------------------------------------------------------------

#----------------------------------------------------------------------
boton1 = Button(window, text="Ingresar", background="orange", activebackground="yellow")
boton2 = Button(window, text="Ingresar", background="orange", activebackground="yellow")
boton3 = Button(window, text="Ingresar", background="orange", activebackground="yellow")
boton4 = Button(window, text="Ingresar", background="orange", activebackground="yellow")
boton5 = Button(window, text="Ingresar", background="orange", activebackground="yellow")
boton6 = Button(window, text="Ingresar", background="orange", activebackground="yellow")
boton7 = Button(window, text="Ingresar", background="orange", activebackground="yellow")
boton8 = Button(window, text="Ingresar", background="orange", activebackground="yellow")
#----------------------------------------------------------------------
finanzas_title = Label(window, text="Finanzas", background="white")
finanzas_title.config(font=("Arial", 20))
comercial_title = Label(window, text="Comercial", background="white")
comercial_title.config(font=("Arial", 20))
operaciones_title = Label(window, text="Operaciones", background="white")
operaciones_title.config(font=("Arial", 20))
gestion_title = Label(window, text="Gestión", background="white")
gestion_title.config(font=("Arial", 20))
caphumano_title = Label(window, text="Gestión del Capital Humano", background="white")
caphumano_title.config(font=("Arial", 20))
ecommerce_title = Label(window, text="E-Commerce", background="white")
ecommerce_title.config(font=("Arial", 20))
capacitacion_title = Label(window, text="Capcitaciones", background="white")
capacitacion_title.config(font=("Arial", 20))
otros_title = Label(window, text="Otros", background="white")
otros_title.config(font=("Arial", 20))
#----------------------------------------------------------------------
img1 = Label(window, image=finanzas_icon, background="white")
img2 = Label(window, image=comercial_icon, background="white")
img3 = Label(window, image=operaciones_icon, background="white")
img4 = Label(window, image=gestion_icon, background="white")
img5 = Label(window, image=caphumano_icon, background="white")
img6 = Label(window, image=ecommerce_icon, background="white")
img7 = Label(window, image=capacitaciones_icon, background="white")
img8 = Label(window, image=otros_icon, background="white")
#----------------------------------------------------------------------
portada_label.grid(column=0, row=0, sticky="nsew")
exit.grid(column=3, row=0, sticky="nsew")
midlbl1.grid(column=1, row=0, sticky="nsew")
midlbl2.grid(column=2, row=0, sticky="nsew")
#----------------------------------------------------------------------
finanzas_title.grid(row=1, column=0)
comercial_title.grid(row=1, column=1)
operaciones_title.grid(row=1, column=2)
gestion_title.grid(row=1, column=3)
caphumano_title.grid(row=5, column=0)
ecommerce_title.grid(row=5, column=1)
capacitacion_title.grid(row=5, column=2)
otros_title.grid(row=5, column=3)
#----------------------------------------------------------------------
img1.grid(row=2, column=0)
img2.grid(row=2, column=1)
img3.grid(row=2, column=2)
img4.grid(row=2, column=3)
img5.grid(row=6, column=0)
img6.grid(row=6, column=1)
img7.grid(row=6, column=2)
img8.grid(row=6, column=3)
#----------------------------------------------------------------------
boton1.grid(row=4, column=0)
boton2.grid(row=4, column=1)
boton3.grid(row=4, column=2)
boton4.grid(row=4, column=3)
boton5.grid(row=8, column=0)
boton6.grid(row=8, column=1)
boton7.grid(row=8, column=2)
boton8.grid(row=8, column=3)
#----------------------------------------------------------------------
window.mainloop()

