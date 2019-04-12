#import editdistance
import numpy as np
#from DataLoader import DataLoader, Batch
#from Model import Model, DecoderType
#from SamplePreprocessor import preprocess
#from WordSegmentation import *
from tkinter import *
from tkinter import filedialog
import os
import sqlite3


def clicked(a):
        file = filedialog.askopenfilename(initialdir = "/", title = "Select file")
        a.set(file)
       


	
if __name__ == '__main__':
	#main()
        window = Tk()
        window.title("input")
        window.geometry('500x500')
        window.configure(background='light blue')
        var=StringVar()
        #window.bind("<Return>", lambda event: clicked())
       
        
        btn = Button(window, text=" Browse ")
        
        btn.config(font=("Sans Serif", 10))
        btn.place(x = 200, y = 150 , width=120, height=25)
        btn.bind('<Enter>',clicked(var))
        e = Entry(window,text=var)
        e.config(font=("Sans Serif", 10))
        e.place(x = 60, y = 100 , width=390, height=25)
        window.mainloop()
