from asyncio.proactor_events import _ProactorBaseWritePipeTransport
from asyncore import write
from cProfile import label
from cmath import sqrt
from dis import dis
from random import random
import this
import tkinter
import csv
from turtle import distance
from typing import Iterator
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
import random  
import math
import os

import os

here = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(here, 'data.txt')

petal_points =[]
k = 2
        

def generate_data_points(filename,delimiter ="\t"):

    with open(filename) as data:
        output = []
        data_reader = csv.reader(data,delimiter=delimiter)
        for row in data_reader:
            output.append( (float(row[0].replace(",",".")), float(row[1].replace(",",".")), float(row[2].replace(",",".")),float(row[3].replace(",","."))))
            
    return output

def select_random_points(points, number_of_points_to_pick = 3):
    output = []
    for x in range(0,k):
        output.append(random.choice(points))
    return output

# calculate distance and group each point
def cluster_points(points, centroids):
    output = {}
    for x in range(k):
        output[x] = []
    for p in petal_points:
        shortest_distance = math.inf
        group_to_assign = 0
        for index, c in enumerate(centroids):
            distance = math.dist(c, p)
            if distance < shortest_distance:
                shortest_distance = distance
                group_to_assign = index
        output[group_to_assign].append(p)
    return output

def calculate_new_centroids(centroids, point_groupings):
    for index,c in enumerate(centroids):
        for cluster in range(len(point_groupings)):
            averages = [0,0,0,0]
            for p in point_groupings[cluster]:
               averages[0] += p[0]
               averages[1] += p[1]
               averages[2] += p[2]
               averages[3] += p[3]

            points_in_cluster = len(point_groupings[cluster])
            if points_in_cluster != 0:
               
               averages[0] = averages[0] / points_in_cluster
               averages[1] = averages[1] / points_in_cluster
               averages[2] = averages[2] / points_in_cluster
               averages[3] = averages[3] / points_in_cluster
            else:
                averages = [0,0,0,0]
            c = averages

#sepal_points = generate_data_points("sepal_data.txt")

petal_points = generate_data_points(filename)

centroids = select_random_points(petal_points, k)

clustered_points = cluster_points(petal_points, centroids)

calculate_new_centroids(centroids, clustered_points)

for item in clustered_points.items():
    plt.plot(item)

plt.show()
clustered_points = cluster_points(petal_points, centroids)

print()





