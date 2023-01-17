import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *


def show():
    mysqldb=mysql.connector.connect(host="127.0.0.1",user="copilu",password="copilu12",database="bdGUI_v2")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT auto.VIN, auto.nr_inmatriculare, auto.client_id, marca.id_marca  FROM bdGUI_v2.model, bdGUI_v2.autoturism auto  INNER JOIN bdGUI_v2.marca ON model.id_marca = marca.id_marca AND model.id_marca = auto.id_model")
    records = mycursor.fetchall()

    for i, (VIN, nr_inmatriculare, client_id, id_marca) in enumerate(records, start=1):
        listBox.delete()
        listBox.insert("", "end", values=(VIN, nr_inmatriculare, client_id, id_marca))
        mysqldb.close()

def interogare5():
    global listBox
    inter1 = Tk()
    inter1.title('Tabel Intergorare Complexa 5')
    inter1.geometry("1000x500")
    tk.Label(inter1, text="Interogare 5", fg="black", font=('Helvetica', 20)).place(x=500, y=20, anchor=CENTER)
    # tk.Label(inter1, text="Sa se afiseze datele masinilor cu cel mai mare", fg="black", font=('Helvetica', 15)).place(x=500, y=50, anchor=CENTER)
    # tk.Label(inter1, text="cost de reparatie", fg="black", font=('Helvetica', 15)).place(x=500, y=70, anchor=CENTER)

    cols = ('VIN', 'Nr Inmatriculare', 'ID Client', 'ID Marca') 
    listBox = ttk.Treeview(inter1, columns=cols, show='headings' )

    for col in cols:
        listBox.heading(col, text=col)
        listBox.grid(row=1, column=0, columnspan=2)
        listBox.place(x=10, y=220)

    show()
    inter1.mainloop()
