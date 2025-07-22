# src/progress_view.py

import tkinter as tk
from task_manager import tasks
from collections import Counter

def ProgressViewUI(parent):
    for widget in parent.winfo_children():
        widget.destroy()

    frame = tk.Frame(parent)
    frame.pack(pady=20)

    # --- Header ---
    tk.Label(frame, text="Study Progress Overview", font=("Helvetica", 16, "bold")).pack(pady=10)

    # --- Task Summary ---
    total_tasks = len(tasks)
    tk.Label(frame, text=f"Total Tasks: {total_tasks}", font=("Helvetica", 12)).pack(pady=5)

    # --- Count by Category ---
    category_counts = Counter(task["category"] for task in tasks)
    tk.Label(frame, text="Tasks by Category:", font=("Helvetica", 12, "underline")).pack(pady=5)

    for category, count in category_counts.items():
        tk.Label(frame, text=f"{category}: {count}", font=("Helvetica", 11)).pack()

    # --- (Future Feature) Completed Tasks ---
    # If we add completion tracking, we can show this:
    # completed = sum(1 for task in tasks if task.get("completed"))
    # tk.Label(frame, text=f"Completed Tasks: {completed}", font=("Helvetica", 12)).pack(pady=10)
