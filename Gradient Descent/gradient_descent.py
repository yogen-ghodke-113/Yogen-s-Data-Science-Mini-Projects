import numpy as np
import pandas as pd

df = pd.read_csv('dataset2.csv')
x = []
y = []

# Populate x and y values from csv :

for z in df['x'][0:]:
    x.append(z)

for z in df['y'][0:]:
    y.append(z)

length = len(x)


def cost_ini(m, c):
    j = 0
    for z in range(length):
        j += ((m * x[z]) + c - y[z]) ** 2
    j = j / 2 * length
    return j


# Choosing Initial Value as y-int = y_mean and slope = 0

m = 0
c = np.array(y).mean()

print(f"Initial Line : y = {m}x + {c}")
print(f"Initial Cost Function Value : {cost_ini(m, c).__round__(2)}")

# Gradient Descent

theta0 = np.array(y).mean()
theta1 = 0
rate = 0.0005


def cost_derivative(t):
    j = 0
    for z in range(length):
        if (t):
            j += ((theta1 * x[z]) + theta0 - y[z]) * x[z]
        else:
            j += ((theta1 * x[z]) + theta0 - y[z])
    j = j * rate / length
    return j


prev = 0
count = 0

# This Particular Dataset takes 117617 Iterations to complete.

while 1:
    count += 1
    theta0 -= cost_derivative(False)
    theta1 -= cost_derivative(True)
    current = cost_ini(theta1, theta0)
    print(count, current.__round__(2), theta0, theta1)
    if (current == prev):
        break
    prev = current
