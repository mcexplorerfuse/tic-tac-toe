import tkinter 
from tkinter import messagebox

tasks = []

tk = tkinter.Tk()
name = tkinter.StringVar()
index = tkinter.StringVar()
tk.title("Tkinter")
tk.geometry("800x600+350+100")
tk.configure(bg="#ffffff")
tk.resizable(False,False)
text = tkinter.Label(text="TO DO LIST:",bg="#000000",fg="#ff0000",font="calibri 20 italic")
text.place(x=0, y=50, width=800, height=30)

def execute_button():
    accual_name=name.get()
    if accual_name=="":
        messagebox.showerror("ERROR","BOŞLUK BIRAKAMAZSINIZ.")
    else:
        tasks.append(accual_name)

def execute_button2():
    i = len(tasks)
    abc = 0
    while not abc == i:
        text2 = tkinter.Label(text=tasks[abc],bg="#ffffff",fg="#000000",font="calibri 20 normal")
        text2.place(x=1, y=(200*(abc/5))+175, width=800, height=20)
        abc +=1

def execute_button3():
    
    index_entry = tkinter.Entry(tk, textvariable=index,font=("calibri", 15 , "bold"),bg="#cccccc",fg="#555555" )
    index_entry.place(x=50, y=100, width=700, height=40)
    try:    
        accual_index = index.get()
        int(accual_index)
    except:
        print(accual_index,index)
        exit(0)

name_entry = tkinter.Entry(tk, textvariable=name,font=("calibri", 15 , "bold"),bg="#cccccc",fg="#555555" )
name_entry.place(x=50, y=100, width=700, height=40)


button = tkinter.Button(text="ADD TASK",bg="#777777",fg="#222222",font=("comic-sans" , 14 , "normal"),command=execute_button)
button.place(x=350, y=500, width=120, height=50)

button2 = tkinter.Button(text="SHOW TASKS",bg="#777777",fg="#222222",font=("comic-sans" , 14 , "normal"),command=execute_button2)
button2.place(x=225, y=500, width=120, height=50)

button3 = tkinter.Button(text="DELETE TASKS",bg="#777777",fg="#222222",font=("comic-sans" , 14 , "normal"),command=execute_button3)
button3.place(x=475, y=500, width=120, height=50)

tk.mainloop()