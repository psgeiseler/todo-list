
import tkinter as tk
from tkinter import *

todolist = []

root = tk.Tk()
root.title("Todo List")
root.geometry('400x600')

label = Label(root, text='Todo List', font=('Arial',40,'bold'))
label.pack()

entry= tk.Entry(root, width=30)
entry.pack(pady=5)

todolist_frame = tk.Frame(root, width=40)
todolist_frame.pack(pady=5)

def addTask():
    text= entry.get()

    if text.strip == "":
        return
    
    completed_var = tk.BooleanVar(value=False)

    checkbox = tk.Checkbutton(
        todolist_frame,
        text=text,
        variable=completed_var
    )
    checkbox.pack(anchor="w")

    task = {
        "text": text, 
        "completed": tk.BooleanVar(value=False),
        "widget": checkbox 
    }

    todolist.append(task)
    entry.delete(0, tk.END)

def delAll():
    for task in todolist:
        task["widget"].destroy()

    todolist.clear


add_button = tk.Button(root,text='Add Task', command=addTask)
add_button.pack(pady=5)

del_button = tk.Button(root,text='Delete Tasks', command=delAll)
del_button.pack(pady=5)

root.mainloop()