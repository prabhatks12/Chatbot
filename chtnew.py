# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 14:19:42 2018

@author: prabhat
"""

from chatterbot import ChatBot
import os
from tkinter import *

global text2
text2=" "    
    


chatbot = ChatBot("Alice")

from chatterbot.trainers import ListTrainer
chatbot.set_trainer(ListTrainer)

#put your directory path here

for files in os.listdir("F:\cht\chatterbot-corpus-master\chatterbot_corpus\data\english/"):
    data=open("F:\cht\chatterbot-corpus-master\chatterbot_corpus\data\english/" + files,"r").readlines()
    chatbot.train(data)

 #display part from here   
root=Tk()
root.geometry("300x400");
l1=Label(root,text="You:")
#l2=Label(root,text="Gender:")

ent=Entry(root)

var_chk=IntVar()

#rd1=Radiobutton(root,text="Male",variable=var_chk,value=1)
#rd2=Radiobutton(root,text="Female",variable=var_chk,value=2)

l1.grid(row=0)
#l2.grid(row=1)
ent.grid(row=0,column=1,sticky=W)

#rd1.grid(row=1,column=1)
#rd2.grid(row=1,column=1)

btn=Button(root,text="SEND",bg="Purple",fg="white",command=show_data)
btn.grid(row=0,columnspan=3,sticky=E,padx=10, pady=10)

txt=Text(root,width=37,height=20,wrap=WORD)
txt.grid(row=3,columnspan=2)
root.mainloop()


def show_data():
    global text2
    txt.delete(0.0,'end')
    textname=str(ent.get())
    sent="YOU:"+textname
    reply=str(chatbot.get_response(textname))
    text2=sent+"\n"+"BOT:"+reply+"\n"+text2+"\n\n"
    print("va::",text2)
    txt.insert(0.0,text2)


    
    