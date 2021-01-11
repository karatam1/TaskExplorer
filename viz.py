from tkinter import *
from think import *

cmd = Tk()
cmd.title("Command Tool")
operator=""
text_Input = StringVar()
canvas1 = Canvas(cmd, width = 400, height = 300)
canvas1.pack()
label1 = Label(cmd, text='Enter a command')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

entry1 = Entry (cmd) 
canvas1.create_window(200, 140, window=entry1)


def getcommand():
    sent = entry1.get()
    find(sent)

button1 = Button(text='Execute Command', command=getcommand, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)


cmd.mainloop()