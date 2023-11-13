from tkinter import *

window = Tk()
window.title("Miles to Kilometer converter")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

m_input = Entry(width=7)
m_input.grid(column=1, row=0)

m_label = Label(text="Miles")
m_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

def Calculate():
    print('calculating..........')
    miles = float(m_input.get())
    kilometer = miles * 1.60934
    return kilometer_result_label.config(text=f"{kilometer}")

calculate_button = Button(text="Calculate", command=Calculate)
calculate_button.grid(column=1, row=2)



window.mainloop()