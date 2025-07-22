# src/task_manager.py

import tkinter as tk
from tkinter import ttk, messagebox
import datetime
from utils import save_tasks_to_file, load_tasks_from_file

tasks = load_tasks_from_file()  # ← Load saved tasks on app launch

def TaskManagerUI(parent):
    # Clear and set up layout
    for widget in parent.winfo_children():
        widget.destroy()

    # --- Input Fields Frame ---
    input_frame = tk.Frame(parent)
    input_frame.pack(pady=10)

    # Title
    tk.Label(input_frame, text="Task Title:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    title_entry = tk.Entry(input_frame, width=30)
    title_entry.grid(row=0, column=1, padx=5, pady=5)

    # Category
    tk.Label(input_frame, text="Category:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    category_combo = ttk.Combobox(input_frame, values=["Homework", "Study", "Exam Prep", "Personal"], state="readonly", width=28)
    category_combo.grid(row=1, column=1, padx=5, pady=5)
    category_combo.current(0)

    # Due Date
    tk.Label(input_frame, text="Due Date (YYYY-MM-DD):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    due_date_entry = tk.Entry(input_frame, width=30)
    due_date_entry.grid(row=2, column=1, padx=5, pady=5)

    # --- Add Button ---
    def add_task():
        tasks.append(task)
        save_tasks_to_file(tasks)  # ← Save after adding
        update_task_list()

        # Simple validation
        if not title or not due_date:
            messagebox.showwarning("Input Error", "Please fill in all fields.")
            return

        try:
            datetime.datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Date Format Error", "Use format YYYY-MM-DD.")
            return

        task = {
            "title": title,
            "category": category,
            "due_date": due_date
        }
        tasks.append(task)
        update_task_list()
        title_entry.delete(0, tk.END)
        due_date_entry.delete(0, tk.END)

    add_button = ttk.Button(parent, text="Add Task", command=add_task)
    add_button.pack(pady=10)

    # --- Task List ---
    list_frame = tk.Frame(parent)
    list_frame.pack()

    task_listbox = tk.Listbox(list_frame, width=60, height=10)
    task_listbox.pack(side="left", fill="y")

    scrollbar = tk.Scrollbar(list_frame, orient="vertical")
    scrollbar.config(command=task_listbox.yview)
    scrollbar.pack(side="right", fill="y")
    task_listbox.config(yscrollcommand=scrollbar.set)

    def update_task_list():
        task_listbox.delete(0, tk.END)
        for i, task in enumerate(tasks):
            line = f"{i+1}. {task['title']} [{task['category']}] - Due: {task['due_date']}"
            task_listbox.insert(tk.END, line)

   def delete_selected_task():
        selection = task_listbox.curselection()
        if not selection:
            messagebox.showwarning("No selection", "Please select a task to delete.")
            return
        index = selection[0]
        del tasks[index]

        save_tasks_to_file(tasks)  # ← Save updated task list to JSON
        update_task_list()


    delete_button = ttk.Button(parent, text="Delete Selected Task", command=delete_selected_task)
    delete_button.pack(pady=5)

    update_task_list()

