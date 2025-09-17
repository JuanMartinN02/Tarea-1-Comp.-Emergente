# Tarea 1 (Perceptron basico) 
# Hecho por Juan Martin C.I: 29577475

import csv
import math
import matplotlib.pyplot as plt

#datos = [x1,x2,xn,y]

# csv reader
def readCsv(path):
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

# Step activation function
def step(x):
    return 1.0 if x >= 0 else 0.0

# Separates inputdata data from data
def getInputData(data):

    # takes all rows except the last one (x1,x2,...,xn leaves out y)
    inputdata = [row[:-1] for row in data]

    return inputdata

# Separates output data from data
def getOutputData(data):
        
    # takes the last row (y)
    outputdata = [row[-1] for row in data]
    
    return outputdata


def main():

    print("Welcome to a manual perceptron emulator!")

    while True:
        
        # Csv file input
        userCsv = input("Whats the name of the csv? (example: no_separables.csv): ").strip()

        # Process Csv and clasify data
        data = readCsv(userCsv)
        outputData = getOutputData(data)
        inputData = getInputData(data)
        userWeights = []

        # Bias input
        while True:
            try:
                userBias = float(input("Enter the bias value (example: 3.05): "))
                break
            
            except ValueError:
                print("Invalid input, please inter a numerical value")
        
        # Weights input
        while True:

            try:
                userWeights.clear()

                for i in inputData[0]:
                    n = 1
                    userWeightIt = float(input(f"Enter the weight value of x{n}: "))
                    userWeights.append(userWeightIt)
                    n = n + 1
                break


            except ValueError:
                print("Invalid input, please inter a numerical value")

        print(userWeights)

        break


main()


