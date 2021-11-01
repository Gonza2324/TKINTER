from tkinter import *
import sqlite3

root = Tk()
root.title("Todo list")
root.geometry("500x500")

conn = sqlite3.connect("todo.db")

c = conn.cursor()

c.execute("""
    CREATE TABLE IF NOT EXISTS todo(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        description TEXT NOT NULL,
        complete BOOLEAN NOT NULL
        );
""")

conn.commit()

def remove(id):
    def _remove():
        c.execute("DELETE FROM todo WHERE id = ?", (id, ))
        conn.commit()
        render()

    return _remove

#* Currying (con esto podemos retrazar la ejecucion de una funcion)
def complete_true(id):
    def _complete():
        todo = c.execute("SELECT * from todo WHERE id = ?", (id, )).fetchone()
        c.execute("UPDATE todo SET complete = ? WHERE id = ?", (not todo[3], id))
        conn.commit()
        render()

    return _complete

def render():
    rows = c.execute("SELECT * FROM todo").fetchall()

    for widget in frame.winfo_children():
        widget.destroy()

    for i in range (0, len(rows)):
        id = rows[i][0]
        completed = rows[i][3]
        description = rows[i][2]
        color = "#555555" if completed else "black"
        l = Checkbutton(frame, text=description, fg = color,width=42, anchor=W, command = complete_true(id))
        l.grid(row=i, column=0, sticky="w")
        btn = Button(frame, text="Eliminar", command=remove(id))
        btn.grid(row=i, column=1)
        l.select() if completed else l.deselect()

def addTodo():
    todo = e.get() #!El nombre del campo es complete no completed
    if todo:
        c.execute("""
                INSERT INTO todo (description, complete) VALUES (?, ?)
                """, (todo, False))
        conn.commit()
        e.delete(0, END)
        render()
    else:
        pass

l = Label(root, text="Tarea")
l.grid(row=0, column=0)

e = Entry(root, width=40)
e.focus() #*Puede ser que de error
e.grid(row=0, column=1)


btn = Button(root, text="Agregar", command=addTodo)
btn.grid(row=0, column=3)

frame = LabelFrame(root, text="Mis Tareas", padx = 5, pady=5)
frame.grid(row=1, column=0, columnspan=3, sticky="nswe", padx=5)

root.bind("<Return>" , lambda x: addTodo())

render()

root.mainloop()