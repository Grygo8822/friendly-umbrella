from asyncio.proactor_events import _ProactorBaseWritePipeTransport
from asyncore import write
from cProfile import label
from cmath import sqrt
from dis import dis
from random import random
from mpl_toolkits.mplot3d import Axes3D
import this
import tkinter
import csv
from turtle import distance, shape
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
dimensions = 4
        

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

def get_serial_dimension(points):
    for point in points:
        output = [[],[],[],[]]
        for index, value in enumerate(point):
            output[index].append(value)
    return output

#table containing lists for x point value, y point value etc...
#[[x-values],[y-values],[z-values]...]
def get_values_per_corrdinate(c_points,k,dimensions):
    values_per_coordinate = []
    if k!=1:
        for x in range(k):
            values_per_coordinate.append([])
            for y in range(dimensions):
                values_per_coordinate[x].append([])
            for x in range(k):
                for point in c_points[x]:
                    for index,dimension_value in enumerate(point):
                        values_per_coordinate[x][index].append(dimension_value)
    else:
        for x in range(dimensions):
            values_per_coordinate.append([])
        for point in c_points:
            for index, dimension_value in enumerate(point):
                values_per_coordinate[index].append(dimension_value)
    
    return values_per_coordinate
    
def combine_clusters_per_coordinate(points, centroids, k, dimensions):
    for index,value in enumerate(centroids):
        for dim_value in value:
            points[index]

        


#sepal_points = generate_data_points("sepal_data.txt")

# petal_points = generate_data_points(filename)

# centroids = select_random_points(petal_points, k)

# clustered_points = cluster_points(petal_points, centroids)

# calculate_new_centroids(centroids, clustered_points)

# values_per_coordinate = get_values_per_corrdinate(clustered_points)

# fig = plt.figure()
# ax = fig.add_subplot(111, projection="3d")

# img = ax.scatter(values_per_coordinate[0][0], values_per_coordinate[0][1], values_per_coordinate[0][2], c=values_per_coordinate[0][3], cmap = plt.cool(), marker="v", depthshade = False)

# img2 = ax.scatter(values_per_coordinate[1][0], values_per_coordinate[1][1], values_per_coordinate[1][2], c=values_per_coordinate[1][3], cmap = plt.hot(),  marker="o",depthshade = False)


# #fig.colorbar(img)
# #fig.colorbar(img2)
# plt.show()




print()



