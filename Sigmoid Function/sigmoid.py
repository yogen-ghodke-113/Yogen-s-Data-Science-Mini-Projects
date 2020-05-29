import matplotlib.pyplot as plt
import numpy as np
x = []
y = []
for z in range(-30,40,10):
    x.append(z)
    t = 1 / (1 + np.exp(-z))
    y.append(t)
plt.scatter(x, y)
plt.xlabel("x")
plt.ylabel("Sigmoid(X)")

plt.show()