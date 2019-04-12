from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import textwrap
import docxpy
from tkinter.scrolledtext import ScrolledText
from tkinter import constants as const
class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title("Tkinter Browse")
        self.minsize(640,500)
        #self.labelFrame=ttk.Label(self,text="")
        # self.labelFrame.grid(row=0,column=1)
        #self.label_frame = ttk.Frame(self,height=50)
        #self.label_frame.grid(row=10) # Stops child widgets of label_frame from resizing it

      
        self.button()
        

    def button(self):
       
        self.button=ttk.Button(self,text="Browse",command=self.filedialog)
        self.button.grid(column=3,row=3)
        self.entry=ttk.Entry(self,text="",width=50)
        self.entry.grid(row=3,column=1)
        
        self.entry1=ttk.Entry(self)
        self.entry1.grid(row=10)
        ## self.label1=ttk.Label(self.labelFrame,text="",width=100)
        #self.label1.grid(row=10)
        
               
    def filedialog(self):
        #root.filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        
        self.filename = filedialog.askopenfilename(initialdir = "/", title = "Select file")
        self.entry.insert(0,self.filename)
        self.text = docxpy.process(self.filename)
        print(self.text)
        self.txt=ScrolledText(self, width=150, height=10)
        self.txt.grid()
        self.txt.insert(const.END,self.text)
        #self.label1.config(text=self.text)
        self.entry1.insert(0,self.text)
        print(textwrap.fill(self.text))
        
    def entry(self):
        
        self.entry=ttk.Entry(self.labelFrame,text="",width=50)
        self.entry.grid(column=1,row=6,padx=5,pady=60,ipady=3)
        return
	
if __name__ == '__main__':

    root=Root()
    root.mainloop()

