import tkinter as tk
from tkinter import ttk
from task_manager import TaskManagerUI
from study_timer import StudyTimerUI
from calendar_view import CalendarViewUI

def open_dashboard():
    dashboard = tk.Tk()
    dashboard.title("StudyBuddy Dashboard")
    dashboard.geometry("800x600")
    dashboard.configure(bg="white")

    # Navigation panel
    nav_frame = tk.Frame(dashboard, width=200, bg="#BEE3DB")  # Calm greenish color
    nav_frame.pack(side="left", fill="y")

    # Main content area
    content_frame = tk.Frame(dashboard, bg="white")
    content_frame.pack(side="right", fill="both", expand=True)

    # Helper to switch sections
    def show_section(section_func):
        for widget in content_frame.winfo_children():
            widget.destroy()
        section_func(content_frame)

    # Navigation buttons
    nav_buttons = [
        ("Tasks", lambda: show_section(TaskManagerUI)),
        ("Study Timer", lambda: show_section(StudyTimerUI)),
        ("Calendar", lambda: show_section(CalendarViewUI))
    ]

    for label, command in nav_buttons:
        btn = ttk.Button(nav_frame, text=label, command=command)
        btn.pack(padx=10, pady=10, fill="x")

    dashboard.mainloop()

