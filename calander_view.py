# src/calendar_view.py

import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from task_manager import tasks  # Uses the shared task list from task_manager.py

# Color map for task categories
CATEGORY_COLORS = {
    "Homework": "#A3D2CA",
    "Study": "#FFC5AB",
    "Exam Prep": "#F7D6E0",
    "Personal": "#C3F584"
}

def CalendarViewUI(parent):
    for widget in parent.winfo_children():
        widget.destroy()

    frame = tk.Frame(parent)
    frame.pack(pady=10)

    # Calendar Widget
    calendar = Calendar(frame, selectmode='day', date_pattern='yyyy-mm-dd')
    calendar.grid(row=0, column=0, padx=20)

    # Task Display Box
    task_display = tk.Text(frame, height=15, width=40, state="disabled", bg="#F4F4F4")
    task_display.grid(row=0, column=1)

    def show_tasks_for_date(event=None):
        selected_date = calendar.get_date()
        display_text = ""
        for task in tasks:
            if task["due_date"] == selected_date:
                color = CATEGORY_COLORS.get(task["category"], "#FFFFFF")
                display_text += f"{task['title']} ({task['category']})\n"
        # Update the display box
        task_display.configure(state="normal")
        task_display.delete("1.0", tk.END)
        if display_text:
            task_display.insert(tk.END, display_text)
        else:
            task_display.insert(tk.END, "No tasks for this date.")
        task_display.configure(state="disabled")

    # Initial display
    show_tasks_for_date()

    # Bind calendar selection
    calendar.bind("<<CalendarSelected>>", show_tasks_for_date)
