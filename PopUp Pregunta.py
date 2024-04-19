from tkinter import * 
from PIL import ImageTk, Image
from tkinter import messagebox

window = Tk()
window.title("POP-UP")
window.iconbitmap('Calculator_512.ico')

def popup():
    respuesta = messagebox.askyesno("Confirmación", "Esta Seguro?")
    Label(window, text=respuesta).pack()
    if respuesta == 1:
        Label(window, text="Clickeaste Si").pack()
    else:
        Label(window, text="Clickeaste No").pack()


boton = Button(window, text="Clickea", command=popup).pack()

window.mainloop()