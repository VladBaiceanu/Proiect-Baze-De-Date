import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *

def show():
    mysqldb=mysql.connector.connect(host="127.0.0.1",user="copilu",password="copilu12",database="bdGUI_v2")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT auto.VIN, auto.nr_inmatriculare, auto.client_id, m.model_nume, lm.cost FROM bdGUI_v2.autoturism auto, bdGUI_v2.lucrari_mentenanta lm, bdGUI_v2.model m WHERE auto.VIN = lm.id_vin AND lm.cost = (SELECT MAX(lm2.cost) FROM bdGUI_v2.lucrari_mentenanta lm2)")
    records = mycursor.fetchall()

    for i, (VIN, nr_inmatriculare, client_id, model_nume, cost) in enumerate(records, start=1):
        listBox.delete()
        listBox.insert("", "end", values=(VIN, nr_inmatriculare, client_id, model_nume, cost))
        mysqldb.close()

def interogare3():
    global listBox
    inter1 = Tk()
    inter1.title('Tabel Intergorare Complexa 3')
    inter1.geometry("1000x500")
    tk.Label(inter1, text="Interogare 3", fg="black", font=('Helvetica', 20)).place(x=500, y=20, anchor=CENTER)
    tk.Label(inter1, text="Sa se afiseze datele masinilor cu cel mai mare", fg="black", font=('Helvetica', 15)).place(x=500, y=50, anchor=CENTER)
    tk.Label(inter1, text="cost de reparatie", fg="black", font=('Helvetica', 15)).place(x=500, y=70, anchor=CENTER)

    cols = ('VIN', 'Nr Inmatriculare', 'ID Client', 'Nume model', 'Cost') 
    listBox = ttk.Treeview(inter1, columns=cols, show='headings' )

    for col in cols:
        listBox.heading(col, text=col)
        listBox.grid(row=1, column=0, columnspan=2)
        listBox.place(x=10, y=220)

    show()
    inter1.mainloop()