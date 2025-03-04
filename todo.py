import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def remove_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)

root = tk.Tk()
root.title("To-Do List")

task_entry = tk.Entry(root)
task_entry.pack()

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

task_listbox = tk.Listbox(root)
task_listbox.pack()

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

root.mainloop()

def save_tasks():
    with open("tasks.txt", "w") as file:
        tasks = task_listbox.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task_listbox.insert(tk.END, line.strip())
    except FileNotFoundError:
        pass

load_tasks()

