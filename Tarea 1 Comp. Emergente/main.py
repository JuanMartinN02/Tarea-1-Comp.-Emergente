# Tarea 1 (Perceptron basico) 
# Hecho por Juan Martin C.I: 29577475

import csv
import math
import matplotlib.pyplot as plt

# csv reader
def read_csv(path):
    data = []

    with open(path, 'r') as file:
        reader = csv.reader(file)

        next(reader) #skips the first line (header)

        for row in reader:
            num = [float(x.strip()) for x in row]
            data.append(num)

        return data

# Sum function
def sum(inputs, weights, bias):
    weight_sum = bias

    for x, y in zip(inputs, weights):
        weight_sum += x * y

    return weight_sum

# Sigmoid activation function
def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))

def step(x):
    return 1.0 if x >= 0 else 0.0

