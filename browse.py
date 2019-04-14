from __future__ import unicode_literals
from collections import defaultdict
import math
import sys
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
        self.N=len(self.text)
        print("length=",N)
        self.dictionary=set()
        self.postings=defaultdict(dict)
        self.document_frequency=defaultdict(dict)
        #self.length=defaultdict(float)

        
        self.txt=ScrolledText(self.labelFrame, width=100, height=20)
        self.txt.grid(row=7)
        self.txt.insert(const.END,self.text)
        #self.label1.config(text=self.text)
       # self.entry1.insert(0,self.text)
        self.terms=self.token()
        print(self.terms)
        self.unique_terms = set(self.terms)
        print(self.unique_terms)
        self.dictionary=dictionary.union(self.unique_terms)
        for each term in unique_terms:
            self.postings[term]=self.terms.count(term)
        
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
    def search():
        while True:
            do_search()
    
    def initialize_document_frequencies():
    """For each term in the dictionary, count the number of documents
    it appears in, and store the value in document_frequncy[term]."""
    global document_frequency
    for term in self.dictionary:
        document_frequency[term] = len(self.postings[term])

    def initialize_lengths():
        """Computes the length for each document."""
        global length
    
        self.l = 0
        for term in self.dictionary:
            self.l += imp(term)**2
        self.length = math.sqrt(l)
    def imp(term):
        """Returns the importance of term in document id.  If the term
        isn't in the document, then return 0."""
        if term in self.postings[term]:
            return self.postings[term]*inverse_document_frequency(term)
        else:
            return 0.0
    def inverse_document_frequency(term):
        """Returns the inverse document frequency of term.  Note that if
        term isn't in the dictionary then it returns 0, by convention."""
        if term in self.dictionary:
            return math.log(N/document_frequency[term],2)
        else:
            return 0.0

    def do_search():
        """Asks the user what they would like to search for, and returns a
        list of relevant documents, in decreasing order of cosine
        similarity."""
        self.query=sel.terms


        
        
	
if __name__ == '__main__':

    root=Root()
    root.mainloop()

