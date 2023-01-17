import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *

def show():
    mysqldb=mysql.connector.connect(host="127.0.0.1",user="copilu",password="copilu12",database="bdGUI_v2")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT auto.VIN, auto.nr_inmatriculare, auto.client_id, lm.cost, p.rampa FROM bdGUI_v2.autoturism auto, bdGUI_v2.lucrari_mentenanta lm, bdGUI_v2.programare p  WHERE auto.VIN = lm.id_vin AND lm.id_lucrari_mentenanta = p.id_lucrari_mentenanta AND p.rampa IN (SELECT p2.rampa = '5' FROM bdGUI_v2.programare p2)")
    records = mycursor.fetchall()

    for i, (VIN, nr_inmatriculare, client_id, cost, rampa) in enumerate(records, start=1):
        listBox.delete()
        listBox.insert("", "end", values=(VIN, nr_inmatriculare, client_id, cost, rampa))
        mysqldb.close()

def interogare4():
    global listBox
    inter1 = Tk()
    inter1.title('Tabel Intergorare Complexa 4')
    inter1.geometry("1000x500")
    tk.Label(inter1, text="Interogare 4", fg="black", font=('Helvetica', 20)).place(x=500, y=20, anchor=CENTER)
    tk.Label(inter1, text="Sa se afiseze datele masinilor care au avut programare", fg="black", font=('Helvetica', 15)).place(x=500, y=50, anchor=CENTER)
    tk.Label(inter1, text="la rampa 5", fg="black", font=('Helvetica', 15)).place(x=500, y=70, anchor=CENTER)

    cols = ('VIN', 'Nr Inmatriculare', 'ID Client', 'Cost', 'Rampa') 
    listBox = ttk.Treeview(inter1, columns=cols, show='headings' )

    for col in cols:
        listBox.heading(col, text=col)
        listBox.grid(row=1, column=0, columnspan=2)
        listBox.place(x=10, y=220)

    show()
    inter1.mainloop()