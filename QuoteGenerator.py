# importing the requests library
import requests
import time
import random
import tkinter
from tkinter import *




quoteslist=[]
i=0
while (i<3):
    r = requests.get('http://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json')
    data = r.json()
    quoteslist.append(data)
    i+=1


#quote = f"Quote: {random.choice(quoteslist)['quoteText']} , Author: {random.choice(quoteslist)['quoteAuthor']}"
window = Tk()
window.title("Daily Quote Generator")
window.geometry('350x200')
#lbl = Label(window, text=quote)
lbl = Label(window, text="Click to get a quote")
lbl.grid(column=0, row=0)
btn = Button(window, text="Generate New Quote")
def clicked():
    quote = f"Quote: {random.choice(quoteslist)['quoteText']} , Author: {random.choice(quoteslist)['quoteAuthor']}"
    lbl.configure(text=quote)
btn = Button(window, text="New Quote", command=clicked)
btn.grid(column=1, row=2)
window.mainloop()
