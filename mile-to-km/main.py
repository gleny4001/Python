from tkinter import *

# window setup
window = Tk()
window.title("Mile to Km converter")
window.minsize(250, 80)


def mile_to_km():
    converted.config(text=int(user_input.get()) * 1.60934)


user_input = Entry(text="0", width=15)
user_input.grid(column=1, row=0)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

is_equal = Label(text="  is equal to")
is_equal.grid(column=0, row=1)

converted = Label(text="0")
converted.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

button = Button(text="Calculate", command=mile_to_km)
button.grid(column=1, row=2)

window.mainloop()
