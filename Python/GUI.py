# from tkinter import *
# root=Tk()
# a=Label(root,text='Hello World')
# a.pack()
# root.mainloop()

# from tkinter import *
# from tkinter.ttk import *
# root=Tk()
# root.geometry('200x200')
# btn=Button(root,text='Click me!',command=root.destroy)
# btn.pack(side='top')
# root.mainloop()

# from tkinter import *
# root=Tk()
# root.geometry('100x100')
# btn=Button(root,text='click me!',bd='5',command=root.destroy)
# btn.pack(side='top')
# root.mainloop()
#
# from tkinter import *
# from tkinter.ttk import *
# root=Tk()
# root.geometry('100x100')
# btn=Button(root,text="Click me",command=root.destroy)
# btn.pack(side="top")
# root.mainloop()

# from tkinter import *
# from tkinter.ttk import *
# root=Tk()
# root.geometry('100x100')
# style=Style()
# style.configure('W.TButton',font=('calibri',10,'bold','underline'))
# btn1=Button(root,text='Quit!',style='W.TButton',command=root.destroy)
# btn1.grid(row=0,column=3,padx=100)
# btn2=Button(root,text="Click me!",command=None)
# btn2.grid(row=1,column=3,pady=10,padx=100)
# root.mainloop()

# from tkinter import *
# from tkinter.ttk import *
# root=Tk()
# root.geometry('100x100')
# style=Style()
# style.configure("TButton",font=('calibri',10,'bold','underline'),foreground='red')
# btn1=Button(root,text='quit!',style='TButton',command=root.destroy)
# btn1.grid(row=0,column=3,padx=100)
# btn2=Button(root,text="Click me",command=None)
# btn2.grid(row=1,column=3,pady=10,padx=100)
# root.mainloop()

from tkinter import Tk,mainloop,LEFT,RIGHT
from tkinter.ttk import *
root=Tk()
root.geometry('250x150')
label_frame=LabelFrame(root,text='This is LabelFrame')
label_frame.pack(expand='yes',fill='both')
label1=Label(label_frame,text='1.This is a LabelFrame')
label1.place(x=0,y=5)
label2=Label(label_frame,text='2.This is another LabelFrame')
label2.place(x=0,y=35)
label3=Label(label_frame,text='3.We can add multiple\n widges in it')
label3.place(x=0,y=65)
mainloop()