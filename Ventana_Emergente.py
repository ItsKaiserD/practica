from tkinter import * 
from PIL import ImageTk, Image 

window = Tk()
window.title("Ventana 1")
window.geometry("1080x420")

def abrir():
    global imagen
    second_w = Toplevel()
    second_w.title("Ventana 2")
    second_w.geometry("1080x420")
    lbl = Label(second_w, text="Hola :)").pack()
    imagen = ImageTk.PhotoImage(Image.open("cat.jpg"))
    lbl = Label(second_w, image=imagen).pack()
    btn2 = Button(second_w, text="Cerrar Ventana", command=second_w.destroy).pack()


btn = Button(window, text="Venatan Secundaria", command=abrir).pack()

mainloop()
