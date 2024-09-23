from tkinter import *

def submit():
    username = entry.get()
    print('Hello ' + username)
    entry.config(state=DISABLED)

def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get()) - 1, END)

window = Tk()

entry = Entry(window, font=('Arial', 50), fg='#00FF00', bg='black')

entry.pack(side=LEFT)
submit_button = Button(window, text='sub', command=submit)
submit_button.pack(side=RIGHT)
submit_button = Button(window, text='del', command=delete)
submit_button.pack(side=RIGHT)
submit_button = Button(window, text='<|X|', command=backspace)
submit_button.pack(side=RIGHT)

window.mainloop()