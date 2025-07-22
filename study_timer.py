# src/study_timer.py

import tkinter as tk
from tkinter import ttk, messagebox

def StudyTimerUI(parent):
    for widget in parent.winfo_children():
        widget.destroy()

    timer_frame = tk.Frame(parent)
    timer_frame.pack(pady=50)

    # Time remaining variable
    time_left = tk.IntVar(value=25 * 60)  # Default: 25 minutes
    is_running = {"status": False}  # Mutable for inner function control

    def format_time(seconds):
        mins = seconds // 60
        secs = seconds % 60
        return f"{mins:02d}:{secs:02d}"

    # Label to show countdown
    time_label = tk.Label(timer_frame, text=format_time(time_left.get()), font=("Helvetica", 48))
    time_label.pack(pady=10)

    # Entry for setting custom timer
    custom_frame = tk.Frame(timer_frame)
    custom_frame.pack()

    tk.Label(custom_frame, text="Minutes:").pack(side="left")
    custom_entry = tk.Entry(custom_frame, width=5)
    custom_entry.insert(0, "25")
    custom_entry.pack(side="left")

    def set_timer():
        try:
            minutes = int(custom_entry.get())
            time_left.set(minutes * 60)
            update_display()
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number.")

    set_button = ttk.Button(custom_frame, text="Set", command=set_timer)
    set_button.pack(side="left", padx=5)

    def update_display():
        time_label.config(text=format_time(time_left.get()))

    def countdown():
        if is_running["status"]:
            if time_left.get() > 0:
                time_left.set(time_left.get() - 1)
                update_display()
                parent.after(1000, countdown)
            else:
                is_running["status"] = False
                messagebox.showinfo("Time's Up!", "Study session complete!")

    def start_timer():
        if not is_running["status"]:
            is_running["status"] = True
            countdown()

    def pause_timer():
        is_running["status"] = False

    def reset_timer():
        is_running["status"] = False
        time_left.set(25 * 60)
        update_display()

    # Buttons
    button_frame = tk.Frame(timer_frame)
    button_frame.pack(pady=10)

    ttk.Button(button_frame, text="Start", command=start_timer).pack(side="left", padx=5)
    ttk.Button(button_frame, text="Pause", command=pause_timer).pack(side="left", padx=5)
    ttk.Button(button_frame, text="Reset", command=reset_timer).pack(side="left", padx=5)

    update_display()
