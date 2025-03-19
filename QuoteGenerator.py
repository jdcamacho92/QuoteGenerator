# importing the requests library
import requests
import time
import random
import tkinter
from tkinter import *

# quoteslist=[]
# for _ in range(3):
#     try:
#         r = requests.get('http://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json')
#         data = r.json()
#         quoteslist.append(data)
#     except requests.exceptions.RequestException as e:
#      print(f"Error obteniendo la cita: {e}")

window = Tk()
window.title("Daily Quote Generator")
window.geometry('450x250')
window.resizable(True, True)
lbl = Label(window, text="Click to get a quote", wraplength=400, justify="center")
lbl.grid(column=0, row=0, columnspan=2, pady=10, padx=10)
def clicked():
    try:
        r = requests.get('http://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json')
        data = r.json()
        quote = f"Quote: {data.get('quoteText', 'No quote available')} , Author: {data.get('quoteAuthor', 'Unknown')}"
        lbl.configure(text=quote)
    except requests.exceptions.RequestException as e:
        lbl.configure(text="Error fetching quote. Try again later.")

def copy_to_clipboard():
    window.clipboard_clear()
    window.clipboard_append(lbl.cget("text"))
    window.update()

btn = Button(window, text="New Quote", command=clicked)
btn.grid(column=0, row=1, columnspan=2, pady=10)
copy_btn = Button(window, text="Copy", command=copy_to_clipboard)
copy_btn.grid(column=0, row=2, columnspan=2, pady=5)
window.mainloop()
