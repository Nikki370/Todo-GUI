import tkinter as tk
from tkinter import messagebox
import json

# File to store tasks
TASK_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks():
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file)

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def remove_task():
    try:
        selected_task_index = task_list.curselection()[0]
        task_list.delete(selected_task_index)
        tasks.pop(selected_task_index)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove!")

# GUI setup
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")

# Task Entry
frame = tk.Frame(root)
frame.pack(pady=10)

task_entry = tk.Entry(frame, width=30)
task_entry.pack(side=tk.LEFT, padx=10)
add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.pack(side=tk.RIGHT)

# Task Listbox
task_list = tk.Listbox(root, width=50, height=15)
task_list.pack(pady=20)

# Remove Button
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

# Load existing tasks
tasks = load_tasks()
for task in tasks:
    task_list.insert(tk.END, task)

# Run the GUI
root.mainloop()
