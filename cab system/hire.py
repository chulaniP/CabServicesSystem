import tkinter as tk
from tkinter import Button, StringVar, Widget, ttk
from tkinter.constants import END

win = tk.Tk()
win.geometry("1350x700+0+0")
win.title("Hiring for vehical")

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
  text="Hiring information",
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
  win, text="job Records", 
  font=("Arial", 14), 
  bg="lightgray", 
  foreground="black",
  relief=tk.GROOVE
)
detail_frame.place(x=40, y=90, width=420, height=570)


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

#2
name_lab = tk.Label(
  detail_frame, 
  text="Full name:", 
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
  text="Type of vehical:", 
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
state_ent["values"] = ("car1","car2", "three-wheel 1","three-wheel 2","three-wheel 3","Lorry","trucks")
state_ent.place(x=110, y=113, width=250, height=30)

#4
num_lab = tk.Label(
  detail_frame, 
  text="Time", 
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
city_lab = tk.Label(
  detail_frame, 
  text="City:", 
  font=("Arial", 8), 
  bg="lightgray", 
  foreground="black"
)
city_lab.place(x=20, y=209)
#entry
city_ent = tk.Entry(
  detail_frame, 
  bd=1,
  font=("arial", 16), 
  bg="white", 
  foreground="black",
)
city_ent.place(x=110, y=209, width=250, height=30)

#6
len_lab = tk.Label(
  detail_frame, 
  text="telephone number", 
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


# Database frame
main_frame = tk.Frame(
  data_frame,
  bg="teal",
  bd=2,
  relief=tk.GROOVE
)
main_frame.pack(fill=tk.BOTH, expand=True)

y_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL)


hire_table = ttk.Treeview(main_frame, columns=(
  "vechical number","Full name", "Type of vehical","Time", "City", "telephone number" 
), yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

y_scroll.config(command=hire_table.yview)
x_scroll.config(command=hire_table.xview)

y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

hire_table.heading("vechical number", text="vechical number")
hire_table.heading("Full name", text="Full name")
hire_table.heading("Type of vehical", text="Type of vehical")
hire_table.heading("Time", text="Time")
hire_table.heading("City", text="City")
hire_table.heading("telephone number", text="telephone number")

hire_table["show"] = "headings"

hire_table.column("vechical number", width=100)
hire_table.column("Full name", width=100)
hire_table.column("Type of vehical", width=100)
hire_table.column("Time", width=100)
hire_table.column("City", width=100)
hire_table.column("telephone number", width=100)





hire_table.pack(fill=tk.BOTH, expand=True)

#Default data 

data=[
  ["12180247","Kamal", "Car 1", "3.00","Kaluthara","01267894"],
  ["12180234","Nimal", "Car 2", "7.00", "Panadura","07768954"],
  
]

#Create stripped row tags
hire_table.tag_configure("oddrow", background="white")
hire_table.tag_configure("evenrow", background="#00AEAE")

global count
count=0
for record in data:
  if count % 2 == 0:
    hire_table.insert(parent="", index="end", iid=count, text="", values=(record[0], record[1],record[2],record[3],record[4],record[5]), tags=("evenrow"))
  else:
    hire_table.insert(parent="", index="end", iid=count, text="", values=(record[0], record[1],record[2],record[3],record[4],record[5]), tags=("oddrow"))

  count += 1


 
    
    


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
  text="Book",
  bd=2,
  font=("Arial", 13), width=15,
 
)
add_btn.grid(row=0, column=0, padx=2, pady=2)
win.mainloop()




