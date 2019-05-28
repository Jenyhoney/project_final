
from __future__ import unicode_literals
import re
import os,sys,codecs
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import docxpy
import codecs
import string
import nltk
import unicodedata
from functools import reduce
#from collections import defaultdict
import math
import sys
from collections import defaultdict
from tkinter.scrolledtext import ScrolledText
from tkinter import constants as const
from polyglot_tokenizer import Tokenizer
import urllib3.request
#import urllib2.request
import requests
import tika
from tika import parser
from bs4 import BeautifulSoup
from lxml.html import fromstring
from requests import get
from urllib.parse import urlencode, urlparse, parse_qs
from gensim.summarization.summarizer import summarize
import GoogleScraper
import urllib.parse
import urllib.request
from googlesearch import search
import webbrowser
import tkHyperlinkManager
from bs4.element import Comment
import math
from collections import Counter
from PyPDF2 import PdfFileReader
from sklearn.feature_extraction.text import TfidfVectorizer
characters = " .,!#$%^&*();:\n\t\\\"?!{}[]<>"
WORD = re.compile(r'\w+')
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
        self.totScore=0
        self.cosScore=[]
        self.jaccard=[]
        
##        for i in range(10):
##            b[i]=ttk.Label(self.labelFrame,text=i)
##            b[i].grid(row=50+i,colum=1)
        
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
        ext=self.filename.split(".")[-1]
        if ext=='doc' or ext=='docx':
            self.text = docxpy.process(self.filename)
        if ext=='pdf':
            
            obj=open(self.filename,'rb')
            reader=PdfFileReader(obj)
            num=reader.numPages
            print (num)
            page=reader.getPage(0)
            self.text=page.extractText()

            obj.close()
    
        print(self.text)
        self.txt=ScrolledText(self.labelFrame, width=50, height=20)
        self.txt.grid(row=1,column=3)
        self.txt.insert(const.END,self.text)
        self.button1()
        #self.label1.config(text=self.text)
        # self.entry1.insert(0,self.text)
    def button1(self):
        self.button=ttk.Button(self.labelFrame,text="Check",command=self.urlretrieve)
        self.button.grid(column=3,row=25,sticky=W)
        
        
        return
    def urlretrieve(self):
        n=9
        total=0
        t=self.text
        self.queries = self.getQueries(t,n)
        #q = [' '.join(d) for d in queries]
        print(self.queries)
        self.myList=[]
        for s in self.queries:
            self.searchQuery(s)
        
        for i,url in enumerate(self.myList):
##            self.label=ttk.Label(self,text=url)
##            self.label.grid(row=30+i,column=1,sticky=W)
        
            self.getContent(self.myList[i])
            
            cosscr=self.finding()
            if cosscr==0:
                pass
            else:
                self.label=ttk.Label(self,text=url)
                self.label.grid(row=30+i,column=1,sticky=W)
                self.scoreLabel=ttk.Label(self,text=cosscr)
                self.scoreLabel.grid(row=30+i,column=3,sticky=W)
        for i in range(len(self.myList)):
            print("\n",self.myList[i])
            #self.getContent(self.myList[i])
        if len(self.cosScore)==0:
            total="Not plagiarized"
        else:
            for i in self.cosScore:    
                self.totScore=float(self.totScore+i)
                total=float(self.totScore/len(self.cosScore))
                
            print("total similarity = ",total)
        fontl=('times',20,'bold')
        self.labelscr=ttk.Label(self.labelFrame,text=total)
        self.labelscr.config(font=fontl)
        self.labelscr.grid(row=2)
                #self.view1()
        return

    def getQueries(self,text,n):
        
        sentenceEnders = re.compile('[.!?]')
        sentenceList = sentenceEnders.split(text)
        for x in sentenceList:
            if x=='' or x==' ':
                sentenceList.remove(x)
        return sentenceList
    def searchQuery(self,text):
        print("\n searching..")
        try:
            text = text.encode('utf-8')
        except:
            text =  text
        
        n = 3  # number of result
        query = text
        results = search(query, stop=n)  # returns a generator
    
        for result in results:
            #print(result)
            self.myList.append(result)
        if len(self.myList)==0:
            self.labelscr=ttk.Label(self.labelFrame,text="Not Plagiarised")
            self.labelscr.config(font=fontl)
            self.labelscr.grid(row=2)
            exit()
        
        return
    def getContent(self,text):
        #cos=0
        print("\n\nCONTENT\n")
        try:
            url=text
            #print(url)
            html = urllib.request.urlopen(url).read()
            self.Ntext=self.text_from_html(html)
            print(self.Ntext)
            #find=self.finding()
            #jacScore=self.jaccard(self.text,self.Ntext)
            #self.jaccard.append(jacScore)
            #self.similarity_chk(self.text,self.Ntext)
        except:
            print("connection error")
            #find=0
            
        return 
    def view1(self):
        
##        self.button=[]
##        for i in range(len(self.myList)):
##            self.button.append(ttk.Button(self.labelFrame,text=self.myList[i]))
##            self.button.grid(row=30+i,column=1,sticky=W)
##        self.click()
        self.cosScore=[]
        for i,url in enumerate(self.myList):
            self.label=ttk.Label(self,text=url)
            self.label.grid(row=30+i,column=1,sticky=W)
            self.label.bind("<Button-1>",lambda e,url=url:self.getContent(url))
        
        
        return
##    def click(self):
##        for i in range(len(self.myList)):
##            if self.button[i]:
##                self.button[i].command=self.getContent(self.button[i]['text'])
##        
    

    def tag_visible(self,element):
        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            return False
        if isinstance(element, Comment):
            return False
        return True


    
    def text_from_html(self,body):
        soup = BeautifulSoup(body, 'html.parser')
        texts = soup.findAll(text=True)
        visible_texts = filter(self.tag_visible, texts)  
        return u" ".join(t.strip() for t in visible_texts)

##    def view(self):
##        labels=[]
##        for i in range(len(self.myList)):
##            labels.append(ttk.Label(self.labelFrame,text=self.myList[i]))
##            labels[i].grid(row=30+i,column=1,sticky=W)
####        
####        for i in range(len(self.myList)):
####            b=ttk.Label(self.labelFrame,textvariable=self.myList[i])
####            b.grid(row=50+i,colum=1)
##        return    
##
##    
##    
## 
##    
##        
##        return sentenceList   
    def entry(self): 
        
        self.entry=ttk.Entry(self.labelFrame,text="",width=50)
        self.entry.grid(column=1,row=6,padx=5,pady=60,ipady=3)
        return
    def get_cosine(self,vec1, vec2):
         intersection = set(vec1.keys()) & set(vec2.keys())

         #calculating numerator
         numerator = sum([vec1[x] * vec2[x] for x in intersection])

         #calculating denominator
         sum1 = sum([vec1[x]**2 for x in vec1.keys()])
         sum2 = sum([vec2[x]**2 for x in vec2.keys()])
         denominator = math.sqrt(sum1) * math.sqrt(sum2)

         #checking for divide by zero
         if denominator==0:
            return 0.0
         else:
            return float(numerator) / denominator

    #converts given text into a vector
    def text_to_vector(self,text):
         #uses the Regular expression above and gets all words
         words = WORD.findall(text)
         #returns a counter of all the words (count of number of occurences)
         return Counter(words)

    #returns cosine similarity of two words
    #uses: text_to_vector(text) and get_cosine(v1,v2)
    def cosineSim(self,text1,text2):
         vector1 = self.text_to_vector(text1)
         vector2 = self.text_to_vector(text2)
         #print ("vectors=",vector1)
         cosine = self.get_cosine(vector1, vector2)
         #self.cosScore.append(cosine)
         cosine=round(cosine*100,2 )
         print("Similarity is" ,cosine,"%")
         
         return cosine

    def jaccard(self,text1,text2):
        intersection=set(text1).intersection(set(text2))
        union=set(text1).union(set(text2))
        jac=len(intersection)/len(union)
        jac=round(jac*100,2 )
        print(jac)
        return jac
    

    
        
    def similarity(self,text1,text2):
        print(";;;;;;;;;;;similarity.............")
        tfidf=TfidfVectorizer().fit_transform(text1,text2)
        pairewise_similarity=tfidf*tfidf.T
        print(pairewise_similarity)

    def finding(self):
        num=0
        
        for pattern in self.queries:
            print('Looking for "%s" ->' % (pattern), end=' ')
            if re.search(pattern, self.Ntext):
                num=num+1
                #print("====num===",num)
            else:
                #print("In else part  ====num===",num)
                pass
        if num==0:
            print("No matches i this text...Not plagiarised")
            cos=0
##            self.labelscr=ttk.Label(self.labelFrame,text="Plagiarised")
##            self.labelscr.config(font=fontl)
##            self.labelscr.grid(row=2)
##            print("plagiarised")
            
        if num>0:
            cos=self.cosineSim(self.text,self.Ntext)
            self.cosScore.append(cos)
            #self.similarity(self.text,self.Ntext)
        
        
        return cos
if __name__ == '__main__':

    root=Root()
    root.mainloop()

