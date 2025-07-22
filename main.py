import tkinter as tk
from tkinter import ttk

def open_dashboard(root):
    # This will be replaced later when we build the dashboard
    root.destroy()
    new_window = tk.Tk()
    new_window.title("StudyBuddy Dashboard")
    new_window.geometry("800x600")
    ttk.Label(new_window, text="(Dashboard placeholder)", font=("Helvetica", 16)).pack(pady=200)
    new_window.mainloop()

def welcome_screen():
    root = tk.Tk()
    root.title("StudyBuddy")
    root.geometry("400x300")
    root.configure(bg="#EAF6F6")  # light blue-green tone

    # Title
    ttk.Label(root, text="StudyBuddy", font=("Helvetica", 24, "bold")).pack(pady=20)

    # Tagline
    ttk.Label(root, text="Your smart student assistant", font=("Helvetica", 12)).pack(pady=10)

    # Start Button
    start_btn = ttk.Button(root, text="Start", command=lambda: open_dashboard(root))
    start_btn.pack(pady=30)

    root.mainloop()

if __name__ == "__main__":
    welcome_screen()
