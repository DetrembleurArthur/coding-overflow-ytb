import matplotlib.pyplot as plt
import random
import math

features = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

targets = [
    0,
    0,
    0,
    1
]

class Neuron:

    def __init__(self, n, bias=True):
        self.weights = []
        self.allow_bias = bias
        for i in range(n + 1 if bias else n):
            #self.weights.append(random.random() * 4 - 2)
            self.weights.append(0)

    
    def potential(self, feature):
        if self.allow_bias:
            feature = feature.copy()
            feature.insert(0, 1)
        p = 0
        n = len(self.weights)
        for i in range(n):
            p += self.weights[i] * feature[i]
        return p
    
    def predict(self, activation, feature):
        return activation(self.potential(feature))
    
    def predict_all(self, activation, features):
        ret = []
        for feature in features:
            pr = self.predict(activation, feature)
            ret.append(pr)
            print(f"Feature: {feature} => Prediction: {pr}")
        return ret
    
    def correction(self, error, learning_rate, feature):
        if self.allow_bias:
            feature = feature.copy()
            feature.insert(0, 1)
        n = len(self.weights)
        for i in range(n):
            print(f"correction {i}: {self.weights[i]} += {learning_rate} * {error} * {feature[i]}")
            #self.plot_neuron_line(features, title=f"Droite de décision (i={i+1})")
            self.weights[i] += learning_rate * error * feature[i]
        print(f"correction: {self.weights}")
    
    def y(self, x):
        bias = self.weights[0] if self.allow_bias else 0
        b1 = self.weights[1 if self.allow_bias else 0]
        b2 = self.weights[2 if self.allow_bias else 1]
        if b2 == 0.0:
            b2 = 0.000001
        return (-x * b1 - bias) / b2
    
    def plot_neuron_line(self, features, block=False, title="No title", margin_divider=2):
        if len(features) != 0:
            fx = [row[0] for row in features]
            fy = [row[1] for row in features]
            plt.clf()
            plt.title(title)
            margin_y = (max(fy) - min(fy)) / margin_divider
            plt.ylim((min(fy) - margin_y,max(fy) + margin_y))
            margin_x = (max(fx) - min(fx)) / margin_divider
            plt.xlim((min(fx) - margin_x,max(fx) + margin_x))
            plt.axline((0, self.y(0)), (1, self.y(1)))
            plt.scatter(fx, fy)
            plt.show(block=block)
            plt.pause(0.3)
        

    def __repr__(self):
        buffer = ""
        for i in range(len(self.weights)):
            index = i if self.allow_bias else i + 1
            buffer += f"{self.weights[i]} * X{index} "
            if i != len(self.weights) - 1:
                buffer += " + "
        return buffer + " = 0"



class Perceptron:

    def __init__(self, n, activation, learning_rate):
        self.neuron = Neuron(n, bias=True)
        self.activation = activation
        self.learning_rate = learning_rate
        self.error_distribution = []
    
    def learn(self, features, targets, max_iteration=1000, plot_frequency=1):
        self.error_distribution.clear()
        num_of_features = len(features)
        last_it = 0
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
            last_it = i
            if errors_counter == 0:
                print("Neuron ready")
                break
            if i % plot_frequency == 0:
                print(self.neuron)
                self.neuron.plot_neuron_line(features, title=f"Droite de décision (i={i+1})")
        print("done")
        self.neuron.plot_neuron_line(features, True, title=f"Droite de décision finale (i={last_it+1})")


def activation(x):
    return 1 if x >= 0 else 0

perceptron = Perceptron(2, activation, 1)
perceptron.learn(features, targets)

neuron = perceptron.neuron

neuron.predict_all(activation, features)
print(neuron)
x = [*range(0, len(perceptron.error_distribution), 1)]
plt.title("Erreurs au cours des itérations")
plt.step(x,perceptron.error_distribution)
plt.show()
