from tkinter import *

def button_clicked():
    miles_value = int(input.get())
    km_value = int(miles_value * 1.6)
    num_label.config(text=str(km_value))

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

miles = Label(text="Miles", font=("Arial", 15))
miles.grid(column= 5, row=3)

equal = Label(text="is equal to", font=("Arial", 15))
equal.grid(column=2, row=5)

km = Label(text="km", font=("Arial", 15))
km.grid(column=5, row=5)

num_label = Label(text="0")
num_label.grid(column= 3, row=5)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=3, row=7)

input = Entry(width=8)
input.grid(column=3, row=3)



window.mainloop()
