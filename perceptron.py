import numpy as np
import random


class Perceptron(object):

    def __init__(self, no_of_inputs, learning_rate=0.01, iterations=100):
        self.iterations = iterations
        self.learning_rate = learning_rate
        self.no_of_inputs = no_of_inputs
        self.weights = [random.uniform(-0.5, 0.5) for _ in
                        range(self.no_of_inputs + 1)]  # ZADANIE DOMOWE 1 - losowosc - zrobione
        self.pocket = self.weights
        self.ratchet = self.weights

# Zaburzenie wejścia
    def noisy(self, input):
        x = random.randrange(0, 25)
        if input[x] == 1:
            input[x] = 0
        else:
            input[x] = 1
        return input

# Algorytm SPLA
    def train(self, training_data, labels):
        stop = 0
        for _ in range(self.iterations):
            if _ != 0 and stop == 0:  # Warunek stopu
                break
            else:
                stop = 0
            randPick = list(range(0, len(training_data)))  # Pomocnicza tablica do losowości
            random.shuffle(randPick)
            for x in randPick:
                input = training_data[x][:]
                makeNoise = random.randrange(0, 50)  # Losowanie czy zaburzyć
                if makeNoise == 1:
                    input = self.noisy(input)
                prediction = self.output(input)
                err = labels[x] - prediction
                if err != 0:  # Warunek stopu
                    stop = 1
                    self.weights[1:] += self.learning_rate * err * input
                    self.weights[0] += self.learning_rate * err

    def output(self, input):
        summation = np.dot(self.weights[1:], input) + self.weights[0]
        if summation > 0:
            activation = 1
        else:
            activation = 0
        return activation

# Algorytm PLA
    def trainPLA(self, training_data, labels):
        lifetime = 0
        highestLifetime = 0
        for _ in range(self.iterations):
            randPick = list(range(0, len(training_data)))
            random.shuffle(randPick)
            for x in randPick:
                input = training_data[x][:]
                makeNoise = random.randrange(0, 50)
                if makeNoise == 1:
                    input = self.noisy(input)
                prediction = self.outputPLA(input)
                err = labels[x] - prediction
                if err != 0:
                    self.weights[1:] += self.learning_rate * err * input
                    self.weights[0] += self.learning_rate * err
                    lifetime = 0
                else:
                    lifetime += 1
                    if lifetime > highestLifetime:
                        self.pocket = self.weights
                        highestLifetime = lifetime
                        lifetime = 0

    def outputPLA(self, input):
        summation = np.dot(self.pocket[1:], input) + self.pocket[0]
        if summation > 0:
            activation = 1
        else:
            activation = 0
        return activation

# Algorytm RPLA
    def trainRPLA(self, training_data, labels):
        lifetime = 0
        examples = 0
        highestLifetime = 0
        highestExamples = 0
        for _ in range(self.iterations):
            randPick = list(range(0, len(training_data)))
            random.shuffle(randPick)
            for x in randPick:
                input = training_data[x][:]
                makeNoise = random.randrange(0, 50)
                if makeNoise == 1:
                    input = self.noisy(input)
                prediction = self.outputRPLA(input)
                err = labels[x] - prediction
                if err != 0:
                    self.weights[1:] += self.learning_rate * err * input
                    self.weights[0] += self.learning_rate * err
                    lifetime = 0
                    examples = 0
                else:
                    lifetime += 1
                    examples += 1
                    if lifetime > highestLifetime and examples > highestExamples:
                        self.ratchet = self.weights
                        highestLifetime = lifetime
                        highestExamples = examples
                        lifetime = 0

    def outputRPLA(self, input):
        summation = np.dot(self.ratchet[1:], input) + self.ratchet[0]
        if summation > 0:
            activation = 1
        else:
            activation = 0
        return activation
