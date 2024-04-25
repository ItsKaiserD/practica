from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title("FRAMES")
window.iconbitmap('Calculator_512.ico')

frame = Frame(window, padx=50, pady=50)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Warframe: Ninjas Play Free")
b2 = Button(frame, text="10 Million Registered Loser")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)


window.mainloop()