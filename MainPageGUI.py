import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
from src.model import model
from src.marca import marca
from src.autoturism import autoturism
from src.interogare1 import interogare1
from src.interogare2 import interogare2
from src.interogare3 import interogare3
from src.interogare4 import interogare4
from src.interogare5 import interogare5

w1=Tk()
w1.title('Pagina principala')
w1.geometry("500x500")
cmb = ttk.Combobox(w1, width="10", values=("Marca", "Model", "Autoturism", "Interog Comp 1", "Interog Comp 2", "Interog Comp 3", "Interog Comp 4", "Interog 5"))
def open():
    if cmb.get() == "Marca":
        marca()
    elif cmb.get() == "Model":
        model()
    elif cmb.get() == "Autoturism":
        autoturism()
    elif cmb.get() == "Interog Comp 1":
        interogare1()
    elif cmb.get() == "Interog Comp 2":
        interogare2()
    elif cmb.get() == "Interog Comp 3":
        interogare3()
    elif cmb.get() == "Interog Comp 4":
        interogare4()
    elif cmb.get() == "Interog 5":
        interogare5()    
    elif cmb.get() == "":
        messagebox.showinfo("nimic de aratat!", "Alege ceva...")    

cmb.place(relx="0.1", rely="0.1")
btn = ttk.Button(w1, text="Alege Tabelul", command=open)
btn.place(relx="0.5", rely="0.1")
w1.mainloop()   