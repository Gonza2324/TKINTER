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
def render_clientes():
    rows = cur.execute("""SELECT * FROM cliente""").fetchall()

    tree.delete(*tree.get_children())

    for row in rows:
        tree.insert("", END, row[0], values=(row[1], row[2], row[3]))

def insertar(cliente):
    cur.execute("""
                INSERT INTO cliente (nombre, telefono, emprese) VALUES (?, ?, ?)
                """, (cliente["nombre"], cliente["telefono"], cliente["empresa"]))
    conn.commit()
    render_clientes()

def nuevo_cliente():
    def guardar():
        if not nombre.get():
            messagebox.showerror("Error", "El nombre es obligatorio")
            return
        if not telefono.get():
            messagebox.showerror("Error", "El telefono es obligatorio")
            return
        if not empresa.get():
            messagebox.showerror("Error", "La empresa es obligatorio")
            return

        cliente = {
            "nombre": nombre.get(),
            "telefono": telefono.get(),
            "empresa": empresa.get()
        }
        insertar(cliente)
        top.destroy()

    top = Toplevel()
    top.title("Nuevo cliente")

    #--------------Nombre--------------
    lnombre = Label(top, text="Nombre")
    nombre = Entry(top, width=40)
    lnombre.grid(row=0, column=0)
    nombre.grid(row=0, column=1)

    #--------------Telefono----------------
    ltelefono = Label(top, text="Telefono")
    telefono = Entry(top, width=40)
    ltelefono.grid(row=1, column=0)
    telefono.grid(row=1, column=1)

    #--------------Empresa---------------
    lempresa = Label(top, text="Empresa")
    empresa = Entry(top, width=40)
    lempresa.grid(row=2, column=0)
    empresa.grid(row=2, column=1)

    #---------------------Guardar-------------------------
    save = Button(top, text="Guardar", command=guardar)
    save.grid(row=3, column=1)

    top.mainloop()

def eliminar_cliente():
    id = tree.selection()[0]

    cliente = cur.execute("SELECT * FROM cliente WHERE id = ?", (id, )).fetchone()
    respuesta = messagebox.askokcancel("¿Seguro?", f"¿Estas seguro de eliminar el cliente {cliente[1]}?")
    if respuesta:
        cur.execute("DELETE FROM cliente WHERE id = ?", (id, ))
        conn.commit()
        render_clientes()
    else:
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

render_clientes()

root.mainloop()
