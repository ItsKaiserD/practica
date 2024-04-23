from tkinter import *
# PIL o Pillow hay que instalarlo aparte de importarlo (PIP install Pillow en consola/terminal)
from PIL import ImageTk, Image

# Creamos la ventana principal 
window = Tk()
# Título de la Ventana
window.title("LA CALCULADORA MÁS PERRONA")
# TRATÉ DE PONERLE UN ICONO A LA APP, Y EL CODIGO COMPILA, PERO NO ME MUESTR EL ICONO XD (REVISAR FUTURAMENTE)
window.iconbitmap('Calculator_512.ico')

# Cuadro de texto (para anotar variables)
e = Entry(window, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

my_img = ImageTk.PhotoImage(Image.open("cat.jpg"))
my_label = Label(image=my_img)

# Función para el clickeo de los botones numerales
def button_click(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

# Función para limpiar la calculadora
def button_clear():
    e.delete(0, END)

# Función para sumar (por ahora solo 2 números)
def button_sum():
    first_nmbr = e.get()
    global f_num
    global math
    math = "Suma"
    f_num = int(first_nmbr)
    e.delete(0, END)

# Función para mostrar el resultado
def button_total():
    second_nmbr = e.get()
    e.delete(0, END)
    if math == "Suma":
        e.insert(0, f_num + int(second_nmbr))
    
    if math == "Resta":
        e.insert(0, f_num - int(second_nmbr))
    
    if math == "Multiplicación":
        e.insert(0, f_num * int(second_nmbr))
    
    if math == "División":
        e.insert(0, f_num / int(second_nmbr))
    return

def button_menos():
    first_nmbr = e.get()
    global f_num
    global math
    math = "Resta"
    f_num = int(first_nmbr)
    e.delete(0, END)

def button_multi():
    first_nmbr = e.get()
    global f_num
    global math
    math = "Multiplicación"
    f_num = int(first_nmbr)
    e.delete(0, END)

def button_divi():
    first_nmbr = e.get()
    global f_num
    global math
    math = "División"
    f_num = int(first_nmbr)
    e.delete(0, END)


# Todos los botones de la calculadora
button_1 = Button(window, text="1", padx=40, pady=20, command= lambda: button_click(1))
button_2 = Button(window, text="2", padx=40, pady=20, command= lambda: button_click(2))
button_3 = Button(window, text="3", padx=40, pady=20, command= lambda: button_click(3))
button_4 = Button(window, text="4", padx=40, pady=20, command= lambda: button_click(4))
button_5 = Button(window, text="5", padx=40, pady=20, command= lambda: button_click(5))
button_6 = Button(window, text="6", padx=40, pady=20, command= lambda: button_click(6))
button_7 = Button(window, text="7", padx=40, pady=20, command= lambda: button_click(7))
button_8 = Button(window, text="8", padx=40, pady=20, command= lambda: button_click(8))
button_9 = Button(window, text="9", padx=40, pady=20, command= lambda: button_click(9))
button_0 = Button(window, text="0", padx=40, pady=20, command= lambda: button_click(0))
button_add = Button(window, text="+", padx=39, pady=20, command=button_sum)
button_equal = Button(window, text="=", padx=91, pady=20, command=button_total)
button_elim = Button(window, text="Limpiar", padx=79, pady=20, command=button_clear)

button_sub = Button(window, text="-", padx=41, pady=20, command=button_menos)
button_mult = Button(window, text="x", padx=40, pady=20, command=button_multi)
button_div = Button(window, text="/", padx=40, pady=20, command=button_divi)


# Grid para mostrar los botones acomodados en columnas 
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_elim.grid(row=4, column=1,columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1,columnspan=2)

button_sub.grid(row=6, column=0)
button_mult.grid(row=6, column=1)
button_div.grid(row=6, column=2)

my_label.grid(row=7, column=0)

# El loop que muestra la ventana
window.mainloop()
