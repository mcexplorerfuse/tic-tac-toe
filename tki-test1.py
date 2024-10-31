import tkinter 
from tkinter import messagebox

tk = tkinter.Tk()
name = tkinter.StringVar()
tk.title("Tkinter")
tk.geometry("800x600+350+100")
tk.configure(bg="#ffffff")
tk.resizable(False,False)
text = tkinter.Label(text="TO DO LIST:",bg="#000000",fg="#ff0000",font="calibri 20 italic")
text.place(x=0, y=50, width=800, height=30)

name_entry = tkinter.Entry(tk, textvariable=name,font=("calibri", 15 , "bold"),bg="#cccccc",fg="#555555" )
name_entry.place(x=50, y=100, width=400, height=40)

def execute_button():
    accual_name=name.get()
    if accual_name=="":
        messagebox.showerror("ERROR","BOŞLUK BIRAKAMAZSINIZ.")

button = tkinter.Button(text="SEND",bg="#777777",fg="#222222",font=("comic-sans" , 14 , "normal"),command=execute_button)
button.place(x=80, y=150, width=300, height=150)



#to do list yapılacak--------------------------
#girilen görevler .txt dosyasında tutulacak----
#.txt dosyasından okuma/listeleme--------------
#.txt dosyasından görev silinmesi--------------

tk.mainloop()
