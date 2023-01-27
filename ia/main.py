import matplotlib.pyplot as plt
import numpy as np
import random
import math

def plot_neuron_line(neuron, block=False):
    plt.clf()
    plt.ylim((-0.5,1.5))
    plt.axline((0, neuron.y(0)), (1, neuron.y(1)))
    plt.scatter([0,0,1,1], [0,1,0,1])
    plt.show(block=block)
    plt.pause(0.5)

BIAS = True
class Neuron:

    def __init__(self, n):
        self.weights = []
        for i in range(n + 1 if BIAS else n):
            #self.weights.append(random.random() * 4 - 2)
            self.weights.append(0)

    
    def potential(self, feature):
        feature = feature.copy()
        if BIAS:
            feature.insert(0, 1)
        p = 0
        n = len(self.weights)
        for i in range(n):
            p += self.weights[i] * feature[i]
        return p
    
    def predict(self, activation, feature):
        return activation(self.potential(feature))
    
    def correction(self, error, learning_rate, feature):
        feature = feature.copy()
        if BIAS:
            feature.insert(0, 1)
        for i in range(len(self.weights)):
            #print(f"correction {i}: {self.weights[i]} += {learning_rate} * {error} * {feature[i]}")
            self.weights[i] += learning_rate * error * feature[i]
        print(f"correction: {self.weights}")
    
    def y(self, x):
        bias = self.weights[0] if BIAS else 0
        b1 = self.weights[1 if BIAS else 0]
        b2 = self.weights[2 if BIAS else 1]
        if b2 == 0.0:
            b2 = 0.000001
        return (-x * b1 - bias) / b2
        

    def __repr__(self):
        return f"weights: {self.weights}"



class Perceptron:

    def __init__(self, n, activation, learning_rate):
        self.neuron = Neuron(n)
        self.activation = activation
        self.learning_rate = learning_rate
        self.error_distribution = []
    
    def learn(self, features, targets, max_iteration=1000, plot_frequency=1):
        self.error_distribution.clear()
        num_of_features = len(features)
        for i in range(max_iteration):
            print(f"it: {i + 1}")
            errors_counter = 0
            for k in range(num_of_features):
                feature = features[k]
                target = targets[k]
                y = self.neuron.predict(self.activation, feature)
                error = target - y
                if error != 0:
                    errors_counter += 1
                    self.neuron.correction(error, self.learning_rate, feature)
            self.error_distribution.append(errors_counter)
            if errors_counter == 0:
                print("Neuron ready")
                break
            if i % plot_frequency == 0:
                print(self.neuron)
                plot_neuron_line(self.neuron)
        print("done")
        plot_neuron_line(self.neuron, True)


def activation(x):
    return 1 if x >= 0 else 0

features = [
    [0.0, 0.0],
    [0.0, 1.0],
    [1.0, 0.0],
    [1.0, 1.0]
]

targets = [
    0.0,
    0.0,
    0.0,
    1.0
]
perceptron = Perceptron(2, activation, 1)
perceptron.learn(features, targets)

neuron = perceptron.neuron

print(f"(0, 0) => {neuron.predict(activation, [0, 0])}")
print(f"(0, 1) => {neuron.predict(activation, [0, 1])}")
print(f"(1, 0) => {neuron.predict(activation, [1, 0])}")
print(f"(1, 1) => {neuron.predict(activation, [1, 1])}")
print(neuron)
x = [*range(0, len(perceptron.error_distribution), 1)]
plt.step(x,perceptron.error_distribution)
plt.show()

#plot_neuron_line(perceptron.neuron, True)