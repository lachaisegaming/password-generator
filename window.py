from tkinter import *
from tkinter.ttk import *


root = Tk()

root.wm_geometry("500x400")





slider = Scale(root, from_=8, to=20, length=200, orient=HORIZONTAL)
slider.grid(row = 0, column = 0, sticky = W, pady = 2)


button = Button(root, text="generate password")

root.mainloop()