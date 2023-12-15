import tkinter as tk
from tkinter import Button, StringVar, Widget, ttk
from tkinter.constants import END

win = tk.Tk()
win.geometry("1350x700+0+0")
win.title("Cab service System")

#Background Color
win.config(bg="lightgray")

#Adding some style
style = ttk.Style()

#Pick a theme 
style.theme_use("default")

style.configure("Treeview",
  background="white",
  foreground="black",
  rowheight=25,
  fieldbackground="white"
)

#Change selected color
style.map(
  "Treeview",
  background=[("selected", "darkred")]
)

#Top Menu 

title_label = tk.Label(
  win, 
  text="Cab Service System",
  font=("Arial", 20, "bold"),
  padx=15,
  pady=15, 
  border=0, 
  relief=tk.GROOVE, 
  bg="teal",
  foreground="white"
)
title_label.pack(side=tk.TOP, fill=tk.X)

#Left Menu

detail_frame = tk.LabelFrame(
  win, text="Vechical Records", 
  font=("Arial", 14), 
  bg="lightgray", 
  foreground="black",
  relief=tk.GROOVE
)
detail_frame.place(x=40, y=90, width=480, height=570)


#Data Frame

data_frame = tk.Frame(
  win,  
  bg="teal",
  relief=tk.GROOVE
)
data_frame.place(x=490, y=98, width=830, height=565)



#Label with Entry

id_lab = tk.Label(
  detail_frame, 
  text="vechical number:", 
  font=("Arial", 8), 
  bg="lightgray", 
  foreground="black"
)
id_lab.place(x=20, y=15)

#entry
id_ent = tk.Entry(
  detail_frame, 
  bd=1,
  font=("arial", 10), 
  bg="white", 
  foreground="black",
)
id_ent.place(x=110, y=17, width=250, height=30)

owner_lab = tk.Label(
  detail_frame, 
  text="vechical owner:", 
  font=("Arial", 8), 
  bg="lightgray", 
  foreground="black"
)
owner_lab.place(x=20, y=15)

#entry
owner_ent = tk.Entry(
  detail_frame, 
  bd=1,
  font=("arial", 10), 
  bg="white", 
  foreground="black",
)
owner_ent.place(x=110, y=17, width=250, height=30)




#2
name_lab = tk.Label(
  detail_frame, 
  text="Type of vechical:", 
  font=("Arial", 8), 
  bg="lightgray", 
  foreground="black"
)
name_lab.place(x=20, y=65)

#entry
name_ent = tk.Entry(
  detail_frame, 
  bd=1,
  font=("arial", 10), 
  bg="white", 
  foreground="black",
)
name_ent.place(x=110, y=65, width=250, height=30)

#3
state_lab = tk.Label(
  detail_frame, 
  text="State of vechical:", 
  font=("Arial", 8), 
  bg="lightgray", 
  foreground="black"
)
state_lab.place(x=20, y=113)

#entry
state_ent = ttk.Combobox(
  detail_frame, 
  font=("arial", 16),
)
state_ent["values"] = ("AC", "non AC")
state_ent.place(x=110, y=113, width=250, height=30)

#4
num_lab = tk.Label(
  detail_frame, 
  text="count passangers", 
  font=("Arial", 8), 
  bg="lightgray", 
  foreground="black"
)
num_lab.place(x=30, y=161)

#entry
num_ent = tk.Entry(
  detail_frame, 
  bd=1,
  font=("arial", 16), 
  bg="white", 
  foreground="black",
)
num_ent.place(x=110, y=161, width=250, height=30)

#5
max_lab = tk.Label(
  detail_frame, 
  text="max weight:", 
  font=("Arial", 8), 
  bg="lightgray", 
  foreground="black"
)
max_lab.place(x=20, y=209)

#entry
max_ent = tk.Entry(
  detail_frame, 
  bd=1,
  font=("arial", 16), 
  bg="white", 
  foreground="black",
)
max_ent.place(x=110, y=209, width=250, height=30)

#6
len_lab = tk.Label(
  detail_frame, 
  text="Max length", 
  font=("Arial", 8), 
  bg="lightgray", 
  foreground="black"
)
len_lab.place(x=20, y=257)

#entry
len_ent = tk.Entry(
  detail_frame, 
  bd=1,
  font=("arial", 16), 
  bg="white", 
  foreground="black",
)
len_ent.place(x=110, y=257, width=250, height=30)


 


#Database frame 

main_frame = tk.Frame(
  data_frame,
  bg="teal",
  bd=2,
  relief=tk.GROOVE
)
main_frame.pack(fill=tk.BOTH, expand=True)

y_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL)

#Treeview database

cab_table = ttk.Treeview(main_frame, columns=(
  "vechical number","vechical owner", "Type of vechical", "State of vechical", "count passangers", "max weight", "Max length" 
), yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

y_scroll.config(command=cab_table.yview)
x_scroll.config(command=cab_table.xview)

y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

cab_table.heading("vechical number", text="vechical number")
cab_table.heading("vechical owner", text="vechical owner")
cab_table.heading("Type of vechical", text="Type of vechical")
cab_table.heading("State of vechical", text="State of vechical")
cab_table.heading("count passangers", text="count passangers")
cab_table.heading("max weight", text="max weight")
cab_table.heading("Max length", text="Max length")


cab_table["show"] = "headings"

cab_table.column("vechical number", width=100)
cab_table.column("vechical owner", width=100)
cab_table.column("Type of vechical", width=100)
cab_table.column("State of vechical", width=100)
cab_table.column("count passangers", width=100)
cab_table.column("max weight", width=100)
cab_table.column("Max length", width=100)




cab_table.pack(fill=tk.BOTH, expand=True)

#Default data 

data=[
  ["12180247","Kamal", "Car 1", "AC", "3","no","no"],
  ["12180234","Nimal", "Car 2", "NonAC", "4","no","no"],
  ["12112322","kasun", "Lorry", "no", "no", "2000kg","no"],
  ["12180248","Saman", "Car 2", "AC", "4","no","no"],
  ["12180249","Silva", "Three wheel 1", "no", "3","no","no"],
  ["12180250","Perera", "Three wheel 2", "no", "3","no","no"], 
  ["12180251","Fereando", "Three wheel 3", "no", "3","no","no"],
  ["12180789","Amal", "Trunks", "no", "no","no","12ft"],
]

#Create stripped row tags
cab_table.tag_configure("oddrow", background="white")
cab_table.tag_configure("evenrow", background="#00AEAE")

global count
count=0
for record in data:
  if count % 2 == 0:
    cab_table.insert(parent="", index="end", iid=count, text="", values=(record[0], record[1],record[2],record[3],record[4],record[5],record[6]), tags=("evenrow"))
  else:
    cab_table.insert(parent="", index="end", iid=count, text="", values=(record[0], record[1],record[2],record[3],record[4],record[5],record[6]), tags=("oddrow"))

  count += 1


#Functions

#Add Function
def add_record():
  cab_table.tag_configure("oddrow", background="white")
  cab_table.tag_configure("evenrow", background="#00AEAE")

  global count
  if count % 2 == 0:
    cab_table.insert(parent="", index="end", iid=count, text="", values=(
    id_ent.get(),
    owner_ent.get(),
    name_ent.get(),
    state_ent.get(),
    num_ent.get(),
    max_ent .get(),
    len_ent.get(),
        
),
    tags=("evenrow")
)
  else:
    cab_table.insert(parent="", index="end", iid=count, text="", values=(
    id_ent.get(),
    owner_ent.get(),
    name_ent.get(),
    state_ent.get(),
    num_ent.get(),
    max_ent .get(),
    len_ent.get(),
    
      
),
    tags=("oddrow")
)
  count += 1

#Delete All Function
def delete_all():
  for record in cab_table.get_children():
      cab_table.delete(record)
       

#Delete One Function
def delete_one():
  x = cab_table.selection()[0]
  cab_table.delete(x)

#button

btn_frame = tk.Frame(
  detail_frame,
  bg="lightgray",
  bd=0,
  relief=tk.GROOVE
)
btn_frame.place(x=40, y=400, width=310, height=130)



#Add Button
add_btn = tk.Button(
  btn_frame,
  bg="teal",
  foreground="white",
  text="Add",
  bd=2,
  font=("Arial", 13), width=15,
  command=add_record
)
add_btn.grid(row=0, column=0, padx=2, pady=2)


#Delete Button
delete_btn = tk.Button(
  btn_frame,
  bg="teal",
  foreground="white",
  text="Delete",
  bd=2,
  font=("Arial", 13), width=15,
  command=delete_one
)
delete_btn.grid(row=0, column=1, padx=2, pady=2)










win.mainloop()
