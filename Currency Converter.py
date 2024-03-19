import tkinter
from tkinter import Entry, W, ttk


def Convert():
    var2 = indicator.get()
    var3 = var1.get()
    if var2 == "China":
        e3.delete(0, END)
        var4 = ((var3 * 6.88), "Yuan")
        e3.insert(0, var4)
    elif var2 == "France":
        e3.delete(0, END)
        var4 = ((var3 * 0.81), "Euro")
        e3.insert(0, var4)
    elif var2 == "Mexico":
        e3.delete(0, END)
        var4 = ((var3 * 18.90), "MXN")
        e3.insert(0, var4)
    elif var2 == "Ghana":
        e3.delete(0, END)
        var4 = ((var3 * 4.00), "Ceti")
        e3.insert(0, var4)
    elif var2 == "Nigeria":
        e3.delete(0, END)
        var4 = ((var3 * 361.01), "Naira")
        e3.insert(0, var4)
    elif var2 == "United States":
        e3.delete(0, END)
        var4 = ((var3 * 1.00), "USD")
        e3.insert(0, var4)
    else:
        e3.delete(0, END)
        var4 = "Error: Please choose a country"
        e3.insert(0, var4)


def Clear():
    e1.delete(0, END)
    e3.delete(0, END)


root = tkinter.Tk()
root.title("Currency Converter")

indicator = StringVar(value="Choose a country")
var1 = IntVar()

Label(text="Currency Converter", padx=10, font=("arial", 30, "bold")).grid(
    row=0, column=1
)
Label(text="Amount ($)", padx=10, font=("arial", 30, "bold")).grid(row=1, sticky=W)
e1 = Entry(width=30, font=("arial", 30, "bold"), textvariable=var1)
e1.grid(row=1, column=1)

Label(text="Country", padx=10, font=("arial", 30, "bold")).grid(row=2, sticky=W)
e2 = ttk.Combobox(width=29, font=("arial", 30, "bold"), textvariable=indicator)
e2["values"] = ("China", "France", "Mexico", "Ghana", "Nigeria", "United States")
e2.grid(row=2, column=1)


Label(text="Total", padx=10, font=("arial", 30, "bold")).grid(row=3, sticky=W)
e3 = Entry(width=30, font=("arial", 30, "bold"))
e3.grid(row=3, column=1)


Button(text="Convert", font=("arial", 30, "bold"), width=15, command=Convert).grid(
    row=4, column=1, sticky=W
)
Button(text="Clear", font=("arial", 30, "bold"), width=15, command=Clear).grid(
    row=4, column=1, sticky=E
)


root.mainloop()
