from random import random
import math
import matplotlib.pyplot as plt
import numpy as np

def carre(x):
    return x >= 0

def linear(x):
    return x

# y = m x + p
# y = B0 + B1 * x
# y = B0 + B1 * x1 + B2 * x2
# 

class Neuron:

    def __init__(self, n):
        self.weights = []
        for i in range(n + 1):
            self.weights.append(random() * 4 - 2)
        print(self.weights)
    
    def output(self, inputs: list, activation):
        biased_inputs = inputs.copy()
        biased_inputs.insert(0, 1)
        out = 0
        for i in range(len(biased_inputs)):
            out += biased_inputs[i] * self.weights[i]
        print(f"p = {out}")
        return activation(out)
    
    def plot(self, inputs):
        weights = self.weights
        x = np.linspace(-0.5, 1.5, 100)
        y = [((-weights[0] - i * weights[1]) / weights[2]) for i in x]
        plt.plot(x, y, "--")
        for inp in inputs:
            plt.scatter(inp[0], inp[1])


class ClassicPerceptron:

    def __init__(self, examples, answers, activation, learn_rate, max_iter):
        self.examples = examples
        self.answers = answers
        self.activation = activation
        self.max_iter = max_iter
        self.neuron = Neuron(len(examples[0]))
        self.learn_rate = learn_rate
    
    def train(self):
        n = len(self.examples)
        for i in range(self.max_iter):
            error_score = 0
            for j in range(n):
                example = self.examples[j]
                answer = self.answers[j]
                y = self.neuron.output(example, self.activation)
                error = (answer - y)
                if error != 0:
                    error_score += 1
                biased_example = example.copy()
                biased_example.insert(0, 1)
                for w in range(len(self.neuron.weights)):
                    self.neuron.weights[w] += error * self.learn_rate * biased_example[w]
            print(error_score)
            if error_score == 0:
                print(f"done in {i} iterations")
                break

        

p = ClassicPerceptron([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
], [
    0,
    1,
    1,
    1
], carre, 1, 1000)

p.train()

print(p.neuron.output([0, 0], carre))
print(p.neuron.output([0, 1], carre))
print(p.neuron.output([1, 0], carre))
print(p.neuron.output([1, 1], carre))
p.neuron.plot( [[0, 0],
    [0, 1],
    [1, 0],
    [1, 1]])
plt.show()