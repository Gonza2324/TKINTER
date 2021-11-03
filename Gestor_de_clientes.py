from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

root = Tk()
root.title("CRM")

#------------------BASE DE DATOS----------------
conn = sqlite3.connect("CRM.db")
cur = conn.cursor()

cur.execute("""
            CREATE TABLE if not exists cliente (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            telefono TEXT NOT NULL,
            emprese TEXT NOT NULL
            );
            """)
conn.commit()

#----------------------BOTONES Y FUNCIONES---------------------
def nuevo_cliente():
    pass


def eliminar_cliente():
    pass


btn = Button(root, text="nuevo cliente", command=nuevo_cliente)
btn.grid(row=0, column=0)

btn_eliminar = Button(root, text="eliminar cliente", command=eliminar_cliente)
btn_eliminar.grid(row=0, column=1)

#----------------------TABLA----------------------- 
tree = ttk.Treeview()
tree["columns"] = ("Nombre", "Telefono", "Empresa")
tree.column("#0", width=0, stretch=NO)
tree.column("Nombre")
tree.column("Telefono")
tree.column("Empresa")

tree.heading("Nombre", text="Nombre")
tree.heading("Telefono", text="Telefono")
tree.heading("Empresa", text="Empresa")

tree.grid(row=1, column=0, columnspan=2)

root.mainloop()
