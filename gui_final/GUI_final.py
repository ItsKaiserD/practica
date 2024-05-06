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
portada_label.grid(column=0, row=0, sticky="nsew")
exit.grid(column=3, row=0, sticky="nsew")
midlbl1.grid(column=1, row=0, sticky="nsew")
midlbl2.grid(column=2, row=0, sticky="nsew")
#----------------------------------------------------------------------
window.mainloop()

