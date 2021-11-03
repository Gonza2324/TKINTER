from tkinter import *
from tkinter import ttk
from sympy import *
import sqlite3

#-----------BASE DE DATOS------------#
midb = sqlite3.connect("Derivadas.db")
cursor = midb.cursor()

#------------------VARIBALES SIMBOLICAS--------------#
x = Symbol("x")
y = Symbol("y")
q = Symbol("q")
t = Symbol("t")

#----------------------------APLICACION------------------------#
root = Tk()
root.title("Derivadas de Funciones Reales de una Sola variable")
