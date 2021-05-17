import youtube_dl
import os
import sys
import pandas as pd
import time
from textblob import TextBlob
import sys
import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
from main import *
import webbrowser


window = tk.Tk(className='TTheHolyTubeBot - V2')
photo = PhotoImage(file='background.gif')
window.iconphoto(False, photo)
window.geometry('1000x300')
window.configure(bg='#0b132b')

top = Frame(window)
bottom = Frame(window)
bottomm = Frame(window)
top.pack(side=TOP)
bottom.pack(side=BOTTOM, expand=True)








# function to change properties of button on hover

def changeOnHover(button, colorOnHover, colorOnLeave):

    # adjusting backgroung of the widget
    # background on entering widget

    button.bind('<Enter>', func=lambda e: \
                button.config(background=colorOnHover))

    # background color on leving widget

    button.bind('<Leave>', func=lambda e: \
                button.config(background=colorOnLeave))


new = 1
url = 'https://www.youtube.com/ttheholyone'


def openwebyt():
    webbrowser.open(url, new=new)


url1 = 'https://discord.gg/ebeAytzSeH'


def openwebdiscord():
    webbrowser.open(url1, new=new)


def prograam():
    wholeprogram()

def about():
    return messagebox.showinfo('About TTheHolyTubeBot:',
                               """
Developer:
TTheHolyOne#1642
This is a bot for youtube!
It is constantly updated and I quite enjoy it.
VERSION 2
""")


def connecthelp():
    return messagebox.showinfo('How to Connect to Tweepy API:',
                               """
Hello!
I'm TTheHolyOne the developer of this program!

Help not done
""")


# welcome message

welcome = tk.Label(text='Welcome to TTheHolyTubeBot! Have Fun!\n',
                   bg='#0b132b', fg='#8C81D4', borderwidth=0)
welcome.pack()





seper = tk.Label(text='\n', borderwidth=0, width=0, height=1, bg='#0b132b',fg='#0b132b')
seper.pack(in_=bottom, side=RIGHT)

button1 = tk.Button(
    text='Download Video',
    width=16,
    height=2,
    bg='#3a506b',
    fg='White',
    justify=CENTER,
    padx=10,
    borderwidth=1,
    command=prograam
    )

button1.pack(in_=bottom, side=RIGHT)

# follow all your followers button

seper = tk.Label(text='\n', borderwidth=0, width=0, height=1, bg='#0b132b',fg='#0b132b')
seper.pack(in_=bottom, side=RIGHT)

butons1 = tk.Button(
    text='',
    width=2,
    height=2,
    padx=0,
    borderwidth=0,
    justify=LEFT,
    bg='#0b132b',
    )
butons1.pack(in_=top, side=LEFT)
discord = tk.Button(
    text='Discord',
    width=20,
    height=2,
    bg='#3a506b',
    fg='Red',
    justify=LEFT,
    command=openwebdiscord,
    )
butons1.pack()
discord.pack(in_=top, side=LEFT)
butons11 = tk.Button(
    text=' ',
    width=2,
    height=2,
    borderwidth=0,
    bg='#0b132b',
    justify=RIGHT,
    )
butons11.pack(in_=top, side=LEFT)

# About Button

seper = tk.Label(text='\n', borderwidth=0, width=0, height=1, bg='#0b132b',fg='#0b132b')
seper.pack(in_=bottom, side=RIGHT)

button9 = tk.Button(
    text='Help',
    width=20,
    height=2,
    bg='#3a506b',
    fg='#49A078',
    justify=CENTER,
    command=connecthelp,
    )
button9.pack(in_=top, side=LEFT)

# Quit Button

seper = tk.Label(text='\n', borderwidth=0, width=0, height=1, bg='#0b132b',fg='#0b132b')
seper.pack()
butons = tk.Button(
    text='',
    width=2,
    height=2,
    bg='#0b132b',
    borderwidth=0,
    justify=CENTER,
    )
butons.pack(in_=top, side=LEFT)
button10 = tk.Button(
    text='Quit',
    width=20,
    height=2,
    bg='#3a506b',
    fg='Red',
    justify=LEFT,
    command=quit,
    )
button10.pack(in_=top, side=LEFT)
seper = tk.Label(text='\n', borderwidth=0, width=0, height=1, bg='#0b132b',fg='#0b132b')
seper.pack()
butonss = tk.Button(
    text=' ',
    width=2,
    height=2,
    bg='#0b132b',
    borderwidth=0,
    justify=CENTER,
    )
butonss.pack(in_=top, side=LEFT)
button8 = tk.Button(
    text='About',
    width=20,
    padx=10,
    height=2,
    bg='#3a506b',
    fg='#49A078',
    justify=LEFT,
    command=about,
    )
button8.pack(in_=top, side=LEFT)

butonsss = tk.Button(
    text=' ',
    width=2,
    height=2,
    bg='#0b132b',
    fg='#0b132b',
    borderwidth=0,
    justify=CENTER,
    )
butonsss.pack(in_=top, side=LEFT)

youtube = tk.Button(
    text='Youtube',
    width=20,
    height=2,
    bg='#3a506b',
    fg='Red',
    justify=RIGHT,
    command=openwebyt,
    )
youtube.pack(in_=top, side=RIGHT)

# ----


# Hover stuff


changeOnHover(button1, 'black', '#3a506b')
changeOnHover(button8, 'black', '#3a506b')
changeOnHover(button9, 'black', '#3a506b')
changeOnHover(button10, 'black', '#3a506b')
changeOnHover(discord, 'black', '#3a506b')
changeOnHover(youtube, 'black', '#3a506b')

# Starts window

window.mainloop()
