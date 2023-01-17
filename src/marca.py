import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *

#incerc implementare doar pentru tabelul marca

def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0,select['id_marca'])
    e2.insert(0,select['marca_nume'])


# def Add(e1,e2):
def Add():
    # id_marca = e1.get()
    marca_nume = e2.get()
   #  a = e2.get()

    mysqldb=mysql.connector.connect(host="127.0.0.1",user="copilu",password="copilu12",database="bdGUI_v2")
    mycursor=mysqldb.cursor()

    try:
       sql = "INSERT INTO  marca (marca_nume) VALUES (%s)"
       val = list(marca_nume)
       mycursor.execute(sql, (marca_nume,))
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Marca inserata cu succes")
       e1.delete(0, END)
       e2.delete(0, END)

    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()


# def update(e1,e2):
def update():
    marca_nume1 = e1.get()
    marca_nume = e2.get()
    mysqldb=mysql.connector.connect(host="127.0.0.1",user="copilu",password="copilu12",database="bdGUI_v2")
    mycursor=mysqldb.cursor()

    try:
       sql = "UPDATE marca SET marca_nume= %s WHERE marca_nume= %s"
       val = (marca_nume,marca_nume1)
       mycursor.execute(sql, val)
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

# def delete(e1,e2):
def delete():
    marca_nume = e2.get()

    mysqldb=mysql.connector.connect(host="127.0.0.1",user="copilu",password="copilu12",database="bdGUI_v2")
    mycursor=mysqldb.cursor()

    try:
       sql = "DELETE FROM marca WHERE marca_nume = %s"
       val = (marca_nume,)
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

# def show(listboxx):
def show():
   mysqldb=mysql.connector.connect(host="127.0.0.1",user="copilu",password="copilu12",database="bdGUI_v2")
   mycursor = mysqldb.cursor()
   mycursor.execute("SELECT id_marca,marca_nume FROM marca")
   records = mycursor.fetchall()
   print(records)
   
   for i, (id_marca, marca_nume) in enumerate(records, start=1):
      listBox.delete()
      listBox.insert("", "end", values=(id_marca, marca_nume))
      mysqldb.close()
         
def marca():
   marca = Tk()
   marca.title('Tabel Marca')
   marca.geometry("800x500")
   global e1
   global e2
   global e3
   global e4
   global listBox

   tk.Label(marca, text="Inregistare marci", fg="red", font=(None, 30)).place(x=300, y=5)

   tk.Label(marca, text="id_marca").place(x=10, y=10)
   Label(marca, text="marca_nume").place(x=10, y=40)

   e1 = Entry(marca)
   e1.place(x=140, y=10)

   e2 = Entry(marca)
   e2.place(x=140, y=40)



   Button(marca, text="Add",command = Add,height=3, width= 13).place(x=30, y=130)
   Button(marca, text="update",command = update,height=3, width= 13).place(x=140, y=130)
   Button(marca, text="Delete",command = delete,height=3, width= 13).place(x=250, y=130)
   Button(marca, text="Show",command = show,height=3, width= 13).place(x=360, y=130)


   cols = ('ID marca', 'Nume marca') 
   listBox = ttk.Treeview(marca, columns=cols, show='headings' )

   for col in cols:
      listBox.heading(col, text=col)
      listBox.grid(row=1, column=0, columnspan=2)
      listBox.place(x=10, y=200)

   show()
   listBox.bind('<Double-Button-1>',GetValue)

   marca.mainloop()
