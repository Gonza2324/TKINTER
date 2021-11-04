from tkinter import *
from tkinter import ttk
from sympy import *
import mysql.connector

#-----------BASE DE DATOS------------#
midb = mysql.connector.connect(
    host = "localhost",
    user = "Gonzalo",
    password = "KORNkorn2402",
    database = "derivadas"
)

cursor = midb.cursor()

#------------------VARIBALES SIMBOLICAS--------------#
x = Symbol("x")
y = Symbol("y")
q = Symbol("q")
t = Symbol("t")

#--------------------------------------------------APLICACION----------------------------------------------------------#
root = Tk()
root.title("Derivadas de Funciones Reales de una Sola variable")
def Derivate():
    funtion_get = funcion.get()
    calculation = diff(funtion_get, x)
    str_calculation = str(calculation)
    answare.set(str_calculation)

    cursor.execute("""INSERT INTO Funciones (funciones, resultados) VALUES(%s, %s)""", (funcion.get(), str_calculation))
    midb.commit()

    funcion.delete(0, END)

funcion = Entry(root, width=40)
funcion.focus()
funcion.grid(row=0, column=0, columnspan=2, sticky="we")

answare = StringVar()
resultado = Label(root, textvariable=answare)
resultado. grid(row=1, column= 0, columnspan=2, sticky="we")

btn_calculo = Button(root, text="Calcular", command = Derivate)
btn_calculo.grid(row=2, column=0, columnspan=2, sticky="we")

tree = ttk.Treeview()
tree["columns"] = ("Funciones", "Resultados")
tree.column("#0", width=0, stretch=NO)
tree.column("Funciones")
tree.column("Resultados")

tree.heading("Funciones", text="Funciones")
tree.heading("Resultados", text="Resultados")

tree.grid(row=3, column=0, columnspan=2)

#cursor.execute("""INSERT INTO Funciones (funciones, resultados) VALUES (%s, %s)""", ())
#midb.commit()

root.mainloop()
