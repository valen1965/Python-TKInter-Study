from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt

# TKinter GUI

root = Tk()
root.title('Codemy.com - Learn to Code')
root.geometry("400x600")
#


def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.hist(house_prices, 50)
    plt.show()


my_button = Button(root, text="Graph It!", command=graph)
my_button.pack()

root.mainloop()
