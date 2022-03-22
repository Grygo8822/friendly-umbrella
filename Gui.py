from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import kmeansvis

root = Tk()
root.geometry("640x480")

def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.hist(house_prices, 50)
    plt.show()

my_button = Button(root, text="Graph!", command=graph)
my_button.pack()

root.mainloop()