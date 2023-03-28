from tkinter import *
import pyshorteners
import pyperclip
root = Tk()
root.title("URL SHORTNER")
root.configure(bg= "green")
url = StringVar()
sortUrl = StringVar()
def urlshort():
    sort_Url = url.get()
    generatedurl = pyshorteners.Shortener().tinyurl.short(sort_Url)
    sortUrl.set(generatedurl)
def copy():
   generatedurl = sortUrl.get()
   pyperclip.copy(generatedurl)
Label(root,text = "Url shortener app", font = "Arial").pack(pady = 10)
Entry(root,textvariable = url).pack(pady =5)
Button(root,text = "generate url" ,command = urlshort).pack(pady=5)
Entry(root,textvariable =sortUrl ).pack(pady= 5)
Button(root,text= "copy url",command= copy).pack(pady=5)

root.mainloop()
