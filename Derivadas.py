from tkinter import *
from tkinter import ttk, messagebox
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

#--------------------------------------------------APLICACION--------------------------------------------------------------#
root = Tk()
root.title("Derivadas de Funciones Reales de una Sola variable")

def render_funciones():
    cursor.execute("SELECT * FROM Funciones")

    rows = cursor.fetchall()

    tree.delete(*tree.get_children()) #*IMPORTANTE CUANDO QUIERO RENDERIZAR

    for row in rows:
        tree.insert("", END, row[0], values=(row[1], row[2]))

def insertar(datos):
    cursor.execute("""INSERT INTO Funciones (funciones, resultados) VALUES(%s, %s)""", (datos["funcion"], datos["resultado"]))
    midb.commit()
    render_funciones()

def Derivate():
    funtion_get = funcion.get()
    calculation = diff(funtion_get, x)
    str_calculation = str(calculation)
    answare.set(f"f'(x) = {str_calculation}")

    datos = {
        "funcion": funcion.get(),
        "resultado": str_calculation
    }

    insertar(datos)
    funcion.delete(0, END)

def Eliminar_Funcion():
    id = tree.selection()[0]

    cursor.execute("SELECT * FROM Funciones WHERE id = %s", (id, ))
    funcion = cursor.fetchone()

    respuesta = messagebox.askokcancel("¿Seguro?", f"Estas seguro de eliminar la funcion {funcion[1]}?")

    if respuesta:
        cursor.execute("DELETE FROM Funciones WHERE id = %s", (id, ))
        midb.commit()
        render_funciones()
    else:
        pass

funcion = Entry(root, width=40)
funcion.focus()
funcion.grid(row=0, column=0, columnspan=2, sticky="we")

answare = StringVar()
resultado = Label(root, textvariable=answare)
resultado. grid(row=1, column= 0, columnspan=2, sticky="we")

btn_calculo = Button(root, text="Calcular", command = Derivate)
btn_calculo.config(
    fg="black",
    background="#008000",
    bd= 1,
    relief=SOLID,
    font=("Arial", 12)
)
btn_calculo.grid(row=2, column=0, columnspan=2, sticky="we")

btn_borrar = Button(root, text="Eliminar", command = Eliminar_Funcion)
btn_borrar.config(
    fg="black",
    background="#CC3300",
    bd=1,
    relief=SOLID,
    font=("Arial", 12)
)
btn_borrar.grid(row=4, column=0, columnspan=2, sticky="we")

#-------------------TABLA--------------------#
tree = ttk.Treeview()
tree["columns"] = ("Funciones", "Resultados")
tree.column("#0", width=0, stretch=NO)
tree.column("Funciones")
tree.column("Resultados")

tree.heading("Funciones", text="Funciones")
tree.heading("Resultados", text="Resultados")

tree.grid(row=3, column=0, columnspan=2)

render_funciones()

root.bind("<Return>", lambda x:Derivate())
root.mainloop()