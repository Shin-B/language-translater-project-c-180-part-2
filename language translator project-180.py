from tkinter import * 
from tkinter import ttk
from googletrans import Translator, LANGUAGES
root = Tk()
root.geometry("1080x400")
root.config(bg="lightgreen")

language=list(LANGUAGES.values())

title=Label(root,text="LANGUAGE TRANSLATOR",bg="lightgreen",font=("Times",22,"bold"))
title.place(relx=0.5,rely=0.1 ,anchor=CENTER)

inputlabel=Label(root,text="Enter Text",bg="lightgreen",font=("Times",15,"bold"))
inputlabel.place(relx=0.02,rely=0.2 ,anchor=W)

srccombo=ttk.Combobox(root,state="readonly",values=language,width=22)
srccombo.place(relx=0.13, rely=0.2, anchor=W)
srccombo.set('english')

outputlabel=Label(root,text="Output",bg="lightgreen",font=("Times",15,"bold"))
outputlabel.place(relx=0.81,rely=0.2 ,anchor=E)

destcombo=ttk.Combobox(root,state="readonly",values=language,width=22)
destcombo.place(relx=0.97, rely=0.2, anchor=E)
destcombo.set('choose output language')

inputtext=Text(root,font=('Times', 10),bg='white',height='11',wrap=WORD,width=60,padx=5,pady=5,bd=0)
inputtext.place(relx=0.02,rely=0.5,anchor=W)

outputtext=Text(root,font=('Times', 10),bg='white',height='11',wrap=WORD,width=60,padx=5,pady=5,bd=0)
outputtext.place(relx=0.98,rely=0.5,anchor=E)

btn=Button(root,text="Translate",bg="orange",fg="white",padx=5,pady=5,font=('Times', 13))
btn.place(relx=0.5,rely=0.9,anchor=CENTER)






















root.mainloop()
