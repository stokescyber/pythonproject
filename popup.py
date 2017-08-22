#!/usr/bin/env python3

import tkinter
import sys
import os

from tkinter import *
#from tkinter import Tk, Label
root = Tk()
root.title("Error!!!")
root.geometry("300x150+350+350")

text = Label(root, text='You messed up')
text.config(font=('times', 26, 'italic bold'))
text.pack()

button = Button(text="OK", width="20", command=lambda:root.destroy()).pack()

root.mainloop()

