from tkinter import *


def calculate():
    miles = int((entry1.get()))
    kilometers = round(miles/1000)
    label3.config(text=kilometers)


# window config
window = Tk()
window.title('Kilometer converter')
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

label1 = Label(text='Equals to')
label1.grid(column=0, row=1)
label1.config(padx=5, pady=5)

entry1 = Entry()
entry1.insert(END, '0')
entry1.grid(column=2, row=0)

label2 = Label(text='Miles')
label2.grid(column=3, row=0)
label2.config(padx=5, pady=5)

label3 = Label(text='0')
label3.grid(column=2, row=1)
label3.config(padx=5, pady=5)

label4 = Label(text='Kilometers')
label4.grid(column=3, row=1)
label4.config(padx=5, pady=5)

button1 = Button(text='Calculate', command=calculate)
button1.grid(column=2, row=2)
button1.config(padx=5, pady=5)

window.mainloop()
