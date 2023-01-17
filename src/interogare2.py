import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *

def show():
    mysqldb=mysql.connector.connect(host="127.0.0.1",user="copilu",password="copilu12",database="bdGUI_v2")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT auto.VIN, auto.nr_inmatriculare, auto.client_id, m.model_nume FROM autoturism auto, model m WHERE auto.id_model = m.id_model and auto.expirare_itp > '2023-01-01' and m.id_marca IN  (SELECT marca.id_marca FROM bdGUI_v2.marca WHERE marca.marca_nume = 'AUDI')")
    records = mycursor.fetchall()

    for i, (VIN, nr_inmatriculare, client_id, model_nume) in enumerate(records, start=1):
        listBox.delete()
        listBox.insert("", "end", values=(VIN, nr_inmatriculare, client_id, model_nume))
        mysqldb.close()
        
def interogare2():
    global listBox
    inter1 = Tk()
    inter1.title('Tabel Intergorare Complexa 2')
    inter1.geometry("800x500")
    tk.Label(inter1, text="Interogare 2", fg="black", font=('Helvetica', 20)).place(x=400, y=20, anchor=CENTER)
    tk.Label(inter1, text="Sa se afiseze datele masini atunci cand marca lui este AUDI", fg="black", font=('Helvetica', 15)).place(x=400, y=50, anchor=CENTER)
    tk.Label(inter1, text="si data expirarii este dupa 01.01.2023", fg="black", font=('Helvetica', 15)).place(x=400, y=70, anchor=CENTER)

    cols = ('VIN', 'Nr Inmatriculare', 'ID Client', 'Nume model') 
    listBox = ttk.Treeview(inter1, columns=cols, show='headings' )

    for col in cols:
        listBox.heading(col, text=col)
        listBox.grid(row=1, column=0, columnspan=2)
        listBox.place(x=10, y=220)

    show()
    inter1.mainloop()
