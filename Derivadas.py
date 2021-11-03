from tkinter import *
from tkinter import ttk
from sympy import *
import sqlite3

#VARIABLES SIMBOLICAS
x = Symbol("x")
t = Symbol("t")
q = Symbol("q")

#-----------BASE DE DATOS-------------
midb = sqlite3.connect("Derivadas.db")
cursor = midb.cursor()

cursor.execute("""
               CREATE TABLE if not exists funciones (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               funciones TEXT NOT NULL,
               resultados TEXT NOT NULL
               );
""")
midb.commit()

#----------------------------APLICACION--------------------------------
root = Tk()
root.title("Derivadas")

funcion = StringVar()
barra = Entry(root, width=40, textvariable=funcion)
barra.focus()
barra.grid(row=0, column=0, columnspan=2)

def Derivar_y_guardar():
    valor = funcion.get()
    calcular = diff(valor, x)
    resultado.set(str(calcular))#Posible cambio
    cursor.execute("""
                   INSERT INTO funciones (funciones, resultados) VALUES (?, ?)
                   """, (funcion.get(), calcular)

btn = Button(root, text="Cacular", background="#eee" ,command=Derivar_y_guardar)
btn.grid(row=2, column=0, columnspan=2, sticky= "we")

resultado = StringVar()
l = Label(root, textvariable=resultado)
l.grid(row=1, column=0, columnspan=2)

#-----------------TABLA----------------------
tree = ttk.Treeview()
tree["columns"] = ("funciones", "resultados")
tree.column("#0", width=0, stretch=NO)
tree.column("funciones")
tree.column("resultados")
tree.heading("funciones", text="Funciones")
tree.heading("resultados", text="Resultados")

tree.grid(row=3, column=0)

root.mainloop()
