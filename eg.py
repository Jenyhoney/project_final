from tkinter import *
from tkinter import filedialog

window = Tk() # user input window

MyText= StringVar()

def DisplayDir(Var):
    feedback = filedialog.askdirectory()
    Var.set(feedback)

Button(window, text='Browse', command=DisplayDir(MyText)).pack()
Entry(window, textvariable = MyText).pack()
Button(window, text='OK', command=window.destroy).pack()

mainloop()
