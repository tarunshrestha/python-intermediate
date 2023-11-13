import tkinter as tk
from tkinter import ttk

def on_button_click():
    result_label.config(text=f"Hello, {entry.get()}!")

# Create the main window
window = tk.Tk()
window.title("Modern Tkinter App")
window.geometry("400x200")

# Create and configure styles for a more modern look
style = ttk.Style()
style.theme_use("clam")  # Other options: 'alt', 'default', 'classic'

# Header Label
header_label = ttk.Label(window, text="Welcome to the Modern Tkinter App", font=('Helvetica', 16, 'bold'))
header_label.pack(pady=10)

# Entry Widget
entry = ttk.Entry(window, width=30)
entry.pack(pady=10)

# Button Widget
button = ttk.Button(window, text="Click Me", command=on_button_click)
button.pack(pady=10)

# Result Label
result_label = ttk.Label(window, text="", font=('Helvetica', 12))
result_label.pack(pady=10)

# Run the application
window.mainloop()
