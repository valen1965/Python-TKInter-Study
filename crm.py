from tkinter import *
from PIL import ImageTk, Image
import mysql.connector

# another connector

#import mysql.connector.python.rf


# TKinter GUI

root = Tk()
root.title('Codemy.com - Learn to Code')
root.geometry("400x600")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="valen1965",
)

print(mydb)

root.mainloop()
