import tkinter as tk

# from tkinter import *
background = "grey"
window = tk.Tk()
window.title("My first GUI program.")
window.config(bg=background, padx=10, pady=10)
window.minsize(width=500, height=300)

# __________LABEL_______________
head = tk.Label(text="Hello", font=('Arial', 24, "bold"))
head.place(x=1, y=2)# you can use grid to do serially and dont use grid and pack together

i = tk.Label(text="Enter username: ", font=('Arial', 16, "bold"))
i.place(x=0, y=50)


head.config(bg=background, fg='white')
i.config(bg=background, fg='white')

# __________ENTRY_______________
write = tk.Entry()
write.place(x=170, y=55)
write.get()


# __________BUTTON_______________
def submit():
    print('0')
    i = write.get()
    em.config(text=f"Hello, {i}")


btn = tk.Button(text="Submit", font=('Arial', 12, "normal"), command=submit)
btn.config(fg='black', bg='white', width=5, height=1)
btn.place(x=300, y=55)

em = tk.Label(text="", font=('Arial', 8))
em.config(bg=background, fg='white')
em.place(x=200, y=100)

window.mainloop()  # TO keep the window run
