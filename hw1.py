#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np

def histogram_times(filename):
    toReturn = [0 for i in range(24)]
    with open(filename) as file:
        csv_reader = csv.reader(file)
        airplane_data = list(csv_reader)
    for i in airplane_data[1 : ]:
        temp = i[1][0 : 2]
        if not temp.isdigit():
            continue
        temp = int(temp)
        toReturn[temp] += 1
    return toReturn

def weigh_pokemons(filename, weight):
    toReturn = []
    with open (filename) as killMe:
        thingy = json.load(killMe)
    for i in thingy['pokemon']:
        if float(i['weight'][:-2]) == weight:
            toReturn.append(i['name'])
    return toReturn

def single_type_candy_count(filename):
    toReturn = 0
    with open (filename) as killMe:
        thingy = json.load(killMe)
    for i in thingy['pokemon']:
        if len(i['type']) == 1 and 'candy_count' in i:
            toReturn += i['candy_count']
    return toReturn

def reflections_and_projections(points):
    for i in points:
        i[1] = 2 - i[1]
    points = np.matmul([[0,-1],[1,0]],points)
    points = np.matmul([[1,3],[3,9]],points) / 10
    return points

def normalize(image):
    min = image[0][0]
    max = image[0][0]
    for i in image:
        for j in i:
            if j < min:
                min = j
            if j > max:
                max = j
    for i in range(len(image)):
        for j in range(len(image[i])):
            image[i][j] = (255/(max-min))*(image[i][j]-min)
    return image

print(normalize([[1,10],[2,3]]))
def sigmoid_normalize(image):
    pass
