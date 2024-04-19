from tkinter import * 
from PIL import ImageTk, Image

window = Tk()
window.title("Opción Multiple")
window.iconbitmap('Calculator_512.ico')

r = IntVar()
r.set(2)

nodes = [
    ("Hola","Hola"),
    ("Adios","Adios"),
    ("KKK","KKK"),
    ("Symphony","Symphony")
]

noc = StringVar()
noc.set("Hola")

for texto, node in nodes:
    Radiobutton(window, text=texto, variable=noc, value=node).pack(anchor=W)

def clicked(value):
    mylabel = Label(window, text=noc.get())
    mylabel.pack()

#Radiobutton(window, text="Opción 1:", variable=r, value=1, command= lambda: clicked(r.get())).pack()
#Radiobutton(window, text="Opción 2:", variable=r, value=2, command= lambda: clicked(r.get())).pack()

#mylabel = Label(window, text=noc.get())
#mylabel.pack()

boton = Button(window, text="Clickea", command=lambda: clicked(noc.get())).pack()

window.mainloop()