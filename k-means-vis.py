from asyncio.proactor_events import _ProactorBaseWritePipeTransport
from asyncore import write
from cProfile import label
from cmath import sqrt
from dis import dis
from random import random
import this
import tkinter
import csv
from typing import Iterator
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
import random  
import math

petal_points =[]
k = 2

class point:
    
    def __init__(self,x_value, y_value):
        self.x_value = x_value
        self.y_value = y_value
    
    def print(self):
        print(self.x_value, self.y_value)

def calculate_distance(p1, p2):
    return (sqrt(float(pow((p2.x_value - p1.x_value),2) + pow((p2.y_value - p1.y_value),2))))
        

def generate_data_points(filename,delimiter ="\t"):
    with open(filename) as petal_data:
        output = []
        petal_data_reader = csv.reader(petal_data,delimiter=delimiter)
        #Skip the first entry: Column names
        iter_data = iter(petal_data_reader)
        next(iter_data)
        for row in iter_data:
            x_value = float(row[0])
            y_value = float(row[1])
            output.append(point(x_value,y_value))
            
    return output


#sepal_points = generate_data_points("sepal_data.txt")

petal_points = generate_data_points("petal_data.txt")

#initialize the output dictionary
point_groupings = {}

for x in range(0,k):
    point_groupings[x]= []

#select k random points
centroids = []

for x in range(0,k):
    new_centroid = centroids.append(random.choice(petal_points))

# calculate distance and group each point
for p in petal_points:
    shortest_distance = math.inf
    group_to_assign = 0
    for index, c in enumerate(centroids):
        distance = math.dist([p.x_value, p.y_value], [c.x_value, c.y_value])
        if distance < shortest_distance:
            shortest_distance = distance
            group_to_assign = index
    point_groupings[group_to_assign].append(p)

for c in centroids:
    c.print()
print("***********")

#calculate new centroids
for index,c in enumerate(centroids):
    for cluster in range(len(point_groupings)):
        avg_x =0
        avg_y =0
        for p in point_groupings[cluster]:
            avg_x += p.x_value
            avg_y += p.y_value
        if len(point_groupings[cluster]) != 0:
            avg_x = avg_x / len(point_groupings[cluster])
            avg_y = avg_y / len(point_groupings[cluster])
        else:
            avg_x = 0
            avg_y = 0
        c.x_value = avg_x
        c.y_value = avg_y

for c in centroids:
    c.print()

print()



