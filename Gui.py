from cProfile import label
from cgitb import text
from ctypes import alignment
from doctest import master
from fileinput import filename
from sre_parse import State
from tkinter import *
import tkinter
from tkinter.filedialog import askopenfile, askopenfilename
from turtle import left, right, width
from click import command
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from pyparsing import col
import kmeansvis
import os
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

here = os.path.dirname(os.path.abspath(__file__))
root = Tk()
root.geometry("1280x720")
dimensions = 0
number_of_points = 0
filename= None
points = None
k = None
centroids = None


def select_data():
    filetypes = [("Text files", "*.txt")]
    global filename
    filename = askopenfilename(title="Open a file", initialdir=here,filetypes=filetypes)
    pick_centroids_button['state'] =tkinter.NORMAL
    read_data(filename=filename)
    
def read_data(filename):
    if filename is not None:
        global points
        points = kmeansvis.generate_data_points(filename=filename)
        dimensions = len(points[0])
        number_of_points = len(points)
        set_data_info(dimensions, number_of_points,filename)
        
    else:
        #REPORT AND ERROR
        pass

def set_data_info(dimensions, nubmer_of_points,filename):
    file_info_label['text'] = f"Ile wymiarów: {dimensions}, punktów: {nubmer_of_points}"
    file_name_label['text'] = f"Wybrany plik: {filename.split('/')[-1]}"

def pick_random_centroids():
    global k, centroids,points
    k = int(k_input.get())
    if  k > 0 and k <= 8:
        centroids = kmeansvis.select_random_points(points,k)
        initialize_graph()
    else:
        print("Error")

def initialize_graph():
    global points, dimensions,canvas
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    img = ax.scatter([0,1,2,3],[0,1,2,3],[0,1,2,3],c=[0,1,2,3], cmap = plt.cool())
    fig.colorbar(img)
    canvas1 = FigureCanvasTkAgg(fig, master=canvas)
    canvas1.draw()
    canvas1.get_tk_widget().pack()

#Pick the data in this frame...
data_picker = LabelFrame(root, text="Wybierz dane:")
data_picker.grid(row=0, column=0,padx=15, pady=10,sticky=W)

#Initialize the data picker frame elements
#Catch that
pic_file_button = Button(data_picker, text="Wybierz plik", command=select_data)

file_name_label = Label(data_picker, text="")

file_info_label = Label(data_picker, text="Ile wymiarów: {ile_wymiar}, punktów: {ile_pkt}")

#Place the elements in the frame
pic_file_button.grid(row=0, column=0,sticky=W)
file_name_label.grid(row=0, column=1)
file_info_label.grid(row=1, column=0)


#Choose the alogorythm propreties (k)
#Pick random centroids
algo_settings_frame = LabelFrame(root, text="Skonfiguruj algorytm")
algo_settings_frame.grid(row=1, column=0, padx=15, pady=10, sticky=W)

#initialize elements
k_value_label = Label(algo_settings_frame, text="Wybierz K (od 2 do 8)")
k_input = Entry(algo_settings_frame, text="k")
pick_centroids_button = Button(algo_settings_frame, text="Losuj centroidy",state=tkinter.DISABLED, command=pick_random_centroids)

#Arrange elements
k_value_label.grid(row=0, column=0, sticky=W)
k_input.grid(row=0,column=1,sticky=W, padx=5)
pick_centroids_button.grid(row=1, column=0,sticky=W)


#Plot secion

canvas = Canvas(root, width=800, height=600)
canvas.pack(side="right")



root.mainloop() 