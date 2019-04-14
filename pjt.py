
from __future__ import unicode_literals
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import docxpy
from tkinter.scrolledtext import ScrolledText
from tkinter import constants as const
from polyglot_tokenizer import Tokenizer

characters = " .,!#$%^&*();:\n\t\\\"?!{}[]<>"
class Root(Tk):
    
    def __init__(self):
        super(Root,self).__init__()
        self.title("Tkinter Browse")
        self.minsize(1000,600)
        self.labelFrame=ttk.Label(self,text="")
        self.labelFrame.grid(row=0,column=1)
        self.label_frame = ttk.Frame(self,height=50)
        self.label_frame.grid(row=10) # Stops child widgets of label_frame from resizing it

        self.entry=ttk.Entry(self.labelFrame,text="",width=50)
        self.entry.grid()
        self.button()
        

    def button(self):
       
        self.button=ttk.Button(self.labelFrame,text="Browse",command=self.filedialog)
        self.button.grid(column=3,row=0)
        
        
        #self.entry1=ttk.Entry(self.label_frame,width=50)
       # self.entry1.grid(row=10)
        ## self.label1=ttk.Label(self.labelFrame,text="",width=100)
        #self.label1.grid(row=10)
        
               
    def filedialog(self):
        #root.filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        
        self.filename = filedialog.askopenfilename(initialdir = "/", title = "Select file")
        self.entry.insert(0,self.filename)
        self.text = docxpy.process(self.filename)
        print(self.text)
        self.txt=ScrolledText(self.labelFrame, width=100, height=20)
        self.txt.grid(row=7)
        self.txt.insert(const.END,self.text)
        #self.label1.config(text=self.text)
       # self.entry1.insert(0,self.text)
        self.terms=self.token()
        print(self.terms)
        self.unique_terms = set(self.terms)
        print(self.unique_terms)
    def entry(self):
        
        self.entry=ttk.Entry(self.labelFrame,text="",width=50)
        self.entry.grid(column=1,row=6,padx=5,pady=60,ipady=3)
        return
    def token(self):
        """self.tkn = Tokenizer(lang='ml', smt=True) #smt is a flag for social-media-text
        self.text = docxpy.process(self.filename)
        print(self.tkn.tokenize(self.text))"""
        self.tkn=self.text.lower().split()
        return [term.strip(characters) for term in self.tkn]
	
if __name__ == '__main__':

    root=Root()
    root.mainloop()

