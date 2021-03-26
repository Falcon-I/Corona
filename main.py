from covid_india import states
import tkinter as tk
root = tk.Tk()
root.geometry('550x350')
root.title("CORONA")

def clickap():
    apc = states.getdata('Andhra Pradesh')
    data.delete(0, "end")
    data.insert(0, apc)

def clicki():
    ic = states.getdata('Total')
    data.delete(0, "end")
    data.insert(0, ic)

data = tk.Entry(width=100)
ap = tk.Button(text="Andhra pradesh", width=15, height=3, command=clickap)
india = tk.Button(text="India", width=15, height=3, command=clicki)
data.pack();india.pack();ap.pack()

root.mainloop()
