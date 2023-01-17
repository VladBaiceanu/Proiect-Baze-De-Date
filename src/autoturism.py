import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *

def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0,select['nr_inmatriculare'])
    e2.insert(0,select['expirare_itp'])
    e3.insert(0,select['client_id'])
    e4.insert(0,select['id_model'])
    e5.insert(0,select['VIN'])

def Add():
    nr_inmatriculare = e1.get()
    expirare_itp = e2.get()
    client_id = e3.get()
    id_model = e4.get()
    VIN = e5.get()

    mysqldb=mysql.connector.connect(host="127.0.0.1",user="copilu",password="copilu12",database="bdGUI_v2")
    mycursor=mysqldb.cursor()

    try:
       sql = "INSERT INTO  autoturism (nr_inmatriculare, expirare_itp, client_id, id_model, VIN) VALUES (%s, %s, %s, %s, %s)"
       mycursor.execute(sql, (nr_inmatriculare, expirare_itp, client_id, id_model, VIN))
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("info", "Autoturism adaugat cu succes")
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e5.delete(0, END)

    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()

def update():
    nr_inmatriculare = e1.get()
    expirare_itp = e2.get()
    client_id = e3.get()
    id_model = e4.get()
    VIN = e5.get()
    mysqldb=mysql.connector.connect(host="127.0.0.1",user="copilu",password="copilu12",database="bdGUI_v2")
    mycursor=mysqldb.cursor()

    try:
       sql = "UPDATE autoturism SET nr_inmatriculare=%s, expirare_itp=%s, client_id=%s, id_model=%s WHERE VIN= %s"
       mycursor.execute(sql, (nr_inmatriculare, expirare_itp, client_id, id_model, VIN))
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Record Updateddddd successfully...")

       e1.delete(0, END)
       e2.delete(0, END)
       e1.focus_set()

    except Exception as e:

       print(e)
       mysqldb.rollback()
       mysqldb.close()

def delete():
    VIN = e5.get()

    mysqldb=mysql.connector.connect(host="127.0.0.1",user="copilu",password="copilu12",database="bdGUI_v2")
    mycursor=mysqldb.cursor()

    try:
       sql = "DELETE FROM autoturism WHERE VIN = %s"
       val = (VIN,)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("info", "Tabel sters cu succes....")

       e1.delete(0, END)
       e2.delete(0, END)
       e1.focus_set()

    except Exception as e:

       print(e)
       mysqldb.rollback()
       mysqldb.close()

def show():
   mysqldb=mysql.connector.connect(host="127.0.0.1",user="copilu",password="copilu12",database="bdGUI_v2")
   mycursor = mysqldb.cursor()
   mycursor.execute("SELECT nr_inmatriculare, VIN, expirare_itp, model.model_nume, client.nume FROM bdGUI_v2.autoturism INNER JOIN bdGUI_v2.model ON autoturism.id_model=model.id_model INNER JOIN bdGUI_v2.client ON autoturism.client_id = client.id_user")
   records = mycursor.fetchall()
   print(records)
   
   for i, (nr_inmatriculare, VIN, expirare_itp, model_nume, nume) in enumerate(records, start=1):
      listBox.delete()
      listBox.insert("", "end", values=(nr_inmatriculare, VIN, expirare_itp, model_nume, nume))
      mysqldb.close()

def autoturism():
      autoturism = Tk()
      autoturism.title('Tabel Autoturism')
      autoturism.geometry("800x500")
      global e1
      global e2
      global e3
      global e4
      global e5
      global listBox

      # tk.Label(autoturism, text="Inregistare marci", fg="red", font=(None, 30)).place(x=300, y=5)

      tk.Label(autoturism, text="Nr Inmatriculare").place(x=10, y=10)
      Label(autoturism, text="Expirare ITP").place(x=10, y=40)
      Label(autoturism, text="ID Client").place(x=10, y=70)
      Label(autoturism, text="ID Model").place(x=10, y=100)
      Label(autoturism, text="VIN").place(x=10, y=130)


      e1 = Entry(autoturism)
      e1.place(x=140, y=10)

      e2 = Entry(autoturism)
      e2.place(x=140, y=40)

      e3 = Entry(autoturism)
      e3.place(x=140, y=70)

      e4 = Entry(autoturism)
      e4.place(x=140, y=100)

      e5 = Entry(autoturism)
      e5.place(x=140, y=130)



      Button(autoturism, text="Add",command = Add,height=3, width= 13).place(x=30, y=160)
      Button(autoturism, text="Update",command = update,height=3, width= 13).place(x=180, y=160)
      Button(autoturism, text="Delete",command = delete,height=3, width= 13).place(x=330, y=160)
      Button(autoturism, text="Show",command = show,height=3, width= 13).place(x=480, y=160)


      cols = ('Nr Inmatriculare', 'VIN', 'Expirare ITP', 'Nume model', 'Nume CLient') 
      listBox = ttk.Treeview(autoturism, columns=cols, show='headings' )

      for col in cols:
         listBox.heading(col, text=col)
         listBox.grid(row=1, column=0, columnspan=2)
         listBox.place(x=10, y=220)

      show()
      listBox.bind('<Double-Button-1>',GetValue)
      autoturism.mainloop()
      