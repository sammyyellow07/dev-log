import datetime
import textwrap
from tkinter import *
from tkinter import ttk

def save_log():
    txt = entry.get("1.0",'end-1c')
    formatted_txt = textwrap.fill(txt)
    print(formatted_txt)
    with open("devlog.txt","a") as fh:
        string = "\n" + "_"*25 + f"\n{datetime.datetime.now()}\n\n{formatted_txt}"
        fh.write(string)
        print(string)
        fh.close()
    
main = Tk()
main.title("DevLog Entry")
main.geometry("900x600")
title = Label(main,text="Developmental Error Log",font="Helvetica 18 bold")
title.pack()
entry = Text(main)
entry.pack()
button = Button(main,text="Save Log",command=save_log)
button.pack()
main.mainloop()