from cProfile import label
from tkinter import *
import os
os.system('clear')

# TKinter GUI

root = Tk()
root.title('Codemy.com - Learn to Code')
root.geometry("400x600")
#
#
#

myLabel = Label(root, text="Enter your first name:")
myLabel.pack()


root.mainloop()
