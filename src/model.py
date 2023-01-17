import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *


def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0,select['model_nume'])
    e2.insert(0,select['marca_nume'])
    e3.insert(0,select['id_marca'])


def Add():
    model_nume = e1.get()
    marca_nume = e2.get()


    mysqldb=mysql.connector.connect(host="127.0.0.1",user="copilu",password="copilu12",database="bdGUI_v2")
    mycursor=mysqldb.cursor()

    try:
       sql1 = "SELECT id_marca,marca_nume FROM marca"
       mycursor.execute(sql1)
       sql_data = mycursor.fetchall()
       mysqldb.commit()
       lastid = mycursor.lastrowid

       print(sql_data)
       sql_data_dict = dict(sql_data)
       sql_data_dict_inv = {v: k for k, v in sql_data_dict.items()}
       id_marca = sql_data_dict_inv[marca_nume]
       
       sql2 = "INSERT INTO model(model_nume,id_marca) VALUES (%s, %s)"
       mycursor.execute(sql2,(model_nume, id_marca))
       mysqldb.commit()

       messagebox.showinfo("information", "Model inserat cu succes")
       e1.delete(0, END)
       e2.delete(0, END)

    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()

def update():
    model_nume = e1.get()
    id_marca = e3.get()

    mysqldb=mysql.connector.connect(host="127.0.0.1",user="copilu",password="copilu12",database="bdGUI_v2")
    mycursor=mysqldb.cursor()

    try:
       sql = "UPDATE model SET id_marca= %s WHERE model_nume= %s"
       val = (id_marca,model_nume)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("info", "Tabel modificat cu succes....")

       e1.delete(0, END)
       e2.delete(0, END)
       e1.focus_set()

    except Exception as e:

       print(e)
       mysqldb.rollback()
       mysqldb.close()

def delete():
    model_nume = e1.get()

    mysqldb=mysql.connector.connect(host="127.0.0.1",user="copilu",password="copilu12",database="bdGUI_v2")
    mycursor=mysqldb.cursor()

    try:
       sql = "DELETE FROM model WHERE model_nume = %s"
       val = (model_nume,)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("info", "Rand sters cu succes...")

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
   mycursor.execute("SELECT model_nume, marca.marca_nume, marca.id_marca  FROM bdGUI_v2.model INNER JOIN bdGUI_v2.marca ON model.id_marca = marca.id_marca" )
   records = mycursor.fetchall()
   print(records)
   
   for i, (model_nume, marca_nume, id_marca) in enumerate(records, start=1):
      listBox.delete()
      listBox.insert("", "end", values=(model_nume, marca_nume, id_marca))
      mysqldb.close()
         
def model():
      model = Tk()
      model.title('Tabel Model')
      model.geometry("800x500")
      global e1
      global e2
      global e3
      global listBox

      # tk.Label(model, text="Inregistare marci", fg="red", font=(None, 30)).place(x=300, y=5)

      tk.Label(model, text="Nume model").place(x=10, y=10)
      Label(model, text="Nume marca").place(x=10, y=40)
      Label(model, text="ID Marca").place(x=10, y=70)


      e1 = Entry(model)
      e1.place(x=140, y=10)

      e2 = Entry(model)
      e2.place(x=140, y=40)

      e3 = Entry(model)
      e3.place(x=140, y=70)



      Button(model, text="Add",command = Add,height=3, width= 13).place(x=30, y=130)
      Button(model, text="Update",command = update,height=3, width= 13).place(x=140, y=130)
      Button(model, text="Delete",command = delete,height=3, width= 13).place(x=250, y=130)
      Button(model, text="Show",command = show,height=3, width= 13).place(x=360, y=130)


      cols = ('Nume model', 'Nume Marca', 'ID Marca') 
      listBox = ttk.Treeview(model, columns=cols, show='headings' )

      for col in cols:
         listBox.heading(col, text=col)
         listBox.grid(row=1, column=0, columnspan=2)
         listBox.place(x=10, y=200)

      show()
      listBox.bind('<Double-Button-1>',GetValue)
      model.mainloop()

# def update():
#     model_nume_start = e1.get()
#     model_nume_final = e3.get()
#     marca_nume_final = e2.get()
#     mysqldb=mysql.connector.connect(host="127.0.0.1",user="copilu",password="copilu12",database="bdGUI_v2")
#     mycursor=mysqldb.cursor()

#     try:
#        sql1 = "SELECT id_marca,marca_nume FROM marca"
#        mycursor.execute(sql1)
#        sql_data = mycursor.fetchall()
#        mysqldb.commit()
#        lastid = mycursor.lastrowid

#        print(sql_data)
#        sql_data_dict = dict(sql_data)
#        sql_data_dict_inv = {v: k for k, v in sql_data_dict.items()}
#        id_marca_final = sql_data_dict_inv[marca_nume_final]
    
#        sql2 = "SELECT model_nume, id_model FROM model"
#        mycursor.execute(sql2)
#        sql_data = mycursor.fetchall()
#        mysqldb.commit()

#        sql_data_dict = dict(sql_data)
#        id_model_start = sql_data_dict_inv[model_nume_start]

#        sql3 = "UPDATE model SET model_nume= %s, id_marca= %s WHERE id_model= %s"
#        val = (model_nume_final, id_marca_final, id_model_start)
#        mycursor.execute(sql3, val)
#        mysqldb.commit()
#        lastid = mycursor.lastrowid
#        messagebox.showinfo("information", "Record Updateddddd successfully...")

#        e1.delete(0, END)
#        e2.delete(0, END)
#        e3.delete(0, END)
#        e1.focus_set()

#     except Exception as e:

#        print(e)
#        mysqldb.rollback()
#        mysqldb.close()