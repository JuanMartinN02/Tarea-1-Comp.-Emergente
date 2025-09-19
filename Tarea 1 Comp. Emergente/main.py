# Tarea 1 (Basic Perceptron) 
# Made by Juan Martin C.I: 29577475
# Universidad Metropolitana de Venezuela

import csv
import math
import matplotlib.pyplot as plt

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
def weightedSum(inputs, weights, bias):
    weight_sum = bias

    for x, y in zip(inputs, weights):
        weight_sum += x * y

    return weight_sum

# Sigmoid activation function
def sigmoid(x):
    r = 1.0 / (1.0 + math.exp(-x))
    return 1 if r >= 0.5 else 0.0

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

# Graph results
def plotResults(inputData, outputData, results):

    xs = [row[0] for row in inputData]
    if len(inputData[0]) > 1:
        ys = [row[1] for row in inputData]
    else:
        # If its only one dimension
        ys = list(range(len(inputData)))

    # Expected values
    plt.figure(figsize=(5,4))
    plt.scatter(xs, ys, c=outputData, cmap='tab10', s=40)
    plt.title("Expected values")
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.colorbar(label="Expected result")

    # Predicted values
    plt.figure(figsize=(5,4))
    plt.scatter(xs, ys, c=results, cmap='tab10', s=40)
    plt.title("Predicted values")
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.colorbar(label="Predicted result")

    # Does the values concide?
    matches = [int(e == p) for e, p in zip(outputData, results)]
    colors = ['green' if m == 1 else 'red' for m in matches]

    plt.figure(figsize=(5,4))
    plt.scatter(xs, ys, c=colors, s=40)
    plt.title("Coincides? green=yes / red=no")
    plt.xlabel("x1")
    plt.ylabel("x2")
    # legend
    plt.scatter([], [], c='green', label='Coincides')
    plt.scatter([], [], c='red', label='Doesnt coincide')
    plt.legend(loc='best')

    plt.show()

def main():

    print("Welcome to a manual perceptron emulator!")
    # Csv file input
    userCsv = input("Whats the name of the csv? (example: no_separables.csv): ").strip()

    while True:

        # Process Csv and clasify data
        data = readCsv(userCsv)
        outputData = getOutputData(data)
        inputData = getInputData(data)
        userWeights = []

        # Results
        results = []

        # Bias input
        while True:
            try:
                userBias = float(input("Enter the bias value (example: 3.05): "))
                break
            
            except ValueError:
                print("Invalid input, please enter a numerical value")
        
        # Weights input
        while True:

            try:
                userWeights.clear()
                n = 1
                for i in inputData[0]:
                    userWeightIt = float(input(f"Enter the weight value of x{n}: "))
                    userWeights.append(userWeightIt)
                    n = n + 1
                break


            except ValueError:
                print("Invalid input, please inter a numerical value")

        print(userWeights)

        # Perceptron logic
        print("Choose an activation function (Input the number 1 or 2)")
        while True:
            try:
                actFunction = int(input("1.- Sigmoid / 2.- Step: "))

                if actFunction == 1:
                    print("Sigmoid activation function!")
                    for x in inputData:
                        results.append(sigmoid(weightedSum(x, userWeights, userBias)))

                elif actFunction == 2:
                    print("Step activation function!")
                    for x in inputData:
                        results.append(step(weightedSum(x, userWeights, userBias)))

                else:
                    print("Invalid option, choosing Sigmoid by default!")
                    for x in inputData:
                        results.append(sigmoid(weightedSum(x, userWeights, userBias)))
                break
            
            except ValueError:
                print("Invalid input, please enter a numerical value")
        
        print("--------------------------")
        print("PREDICTED VALUE: ")
        print(results)
        plotResults(inputData, outputData, results)

        print("--------------------------")
        print("Try again with different weights and bias? (Input the number 1 or 2)")
        repeat = int(input("1.- yes / 2.- no"))
        if repeat == 2:
            break
        else:
            continue


main()


