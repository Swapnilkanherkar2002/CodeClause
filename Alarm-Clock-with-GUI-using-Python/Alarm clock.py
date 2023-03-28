from playsound import playsound
from tkinter import *
from win10toast import ToastNotifier
import datetime
import time
running=True
def alarm(set_alarm):
    toast = ToastNotifier()
    while True:
        time.sleep(1)
        date = datetime.datetime.now()
        now = date.strftime("%H:%M:%S")
        if now == set_alarm:
            print("Alarm Clock")
            toast.show_toast("Alarm Clock",duration=1)
            playsound('alarm1.mp3')

def getvalue():
    set_alarm = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm)
def close():
    root.destroy()

root = Tk()
root.geometry("170x150")
info = Label(root,text = "(24)Hour  Min   Sec").place(x = 50)
set_time = Label(root,text = "Set Time",font=("Cambria",10,"bold")).place(x=0,y=30)

# Entry Variables
hour = StringVar()
min = StringVar()
sec = StringVar()

# Entry Widget
hour_E = Entry(root,textvariable = hour,width = 4).place(x=60,y=30)
min_E = Entry(root,textvariable = min,width = 4).place(x=90,y=30)
sec_E = Entry(root,textvariable = sec,width = 4).place(x=120,y=30)

submit = Button(root,text = "Set Alarm",width = 10,command = getvalue).place(x =50,y=70)
close = Button(root,width=10, text ="Close", command = close).place(x=50,y=100)
root.mainloop()
