from tkinter import *
from sympy import *

x = Symbol("x")
t = Symbol("t")
q = Symbol("q")

root = Tk()
root.title("Derivadas")
root.geometry("250x100")

funcion = StringVar()
barra = Entry(root, width=40, textvariable=funcion)
barra.focus()
barra.grid(row=0, column=0, columnspan=1)


btn = Button(root, text="Cacular", command=Derivar)
btn.grid(row=2, column=0, columnspan=1)

def Derivar():
    valor = funcion.get()
    calcular = diff(valor, x)
    resultado.set(calcular)

resultado = StringVar()
l = Label(root, textvariable=resultado)
l.grid(row=1, column=0)


root.mainloop()