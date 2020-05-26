import numpy as np
import pandas as pd

df = pd.read_csv('dataset2.csv')
x = []
y = []

# Populate x and y values from csv :

for z in df['x'][0:]:
    x.append(z)

count = 0
for z in df['y'][0:]:
    count += 1
    y.append(z)

x_mean = np.array(x).mean()
y_mean = np.array(y).mean()

num = 0
den = 0

# Finding Regression Line using simple slope formula :
# Without Minimization of Squared Error

for z in range(len(x)):
    num += y[z] - y_mean
    den += x[z] - x_mean

m1 = num / den
c1 = y_mean - (m1 * x_mean)

print(f" y1 = {m1.__round__(2)}x + {c1.__round__(2)}")

# Finding Regression Line using O.L.S formula : sum( xy ) / sum ( x^2 ) :

num = 0
den = 0

for z in range(len(x)):
    num += (x[z] - x_mean) * (y[z] - y_mean)
    den += (y[z] - y_mean) * (y[z] - y_mean)

m2 = num / den
c2 = y_mean - (m2 * x_mean)
print(f" y2 = {m2.__round__(2)}x + {c2.__round__(2)}")

# Finding Regression Line using O.L.S formula : sum( y^2 ) / sum ( xy ) :

num = 0
den = 0

for z in range(len(x)):
    num += (y[z] - y_mean) * (y[z] - y_mean)
    den += (x[z] - x_mean) * (y[z] - y_mean)

m3 = num / den
c3 = y_mean - (m3 * x_mean)
print(f" y3 = {m3.__round__(2)}x + {c3.__round__(2)}")

# Finding Regression Line by taking mean of methods #2 and #3

m4 = (m2 + m3) / 2
c4 = (c2 + c3) / 2

print(f" y4 = {m4.__round__(2)}x + {c4.__round__(2)}")

# Finding Sum of Squared Errors for all 4 :
# Minimum means more accurate
# ( Actual y - Predicted y ) ^ 2

l1 = []
l2 = []
l3 = []
l4 = []
l5 = []

for z in range(len(x)):
    l1.append((y[z] - (m1 * x[z]) + c1) ** 2)
    l2.append((y[z] - (m2 * x[z]) + c2) ** 2)
    l3.append((y[z] - (m3 * x[z]) + c3) ** 2)
    l4.append((y[z] - (m4 * x[z]) + c4) ** 2)
    l5.append((y[z] - (1.001 * x[z]) + 0.1073) ** 2)

sse1 = sum(l1).__round__(2)
sse2 = sum(l2).__round__(2)
sse3 = sum(l3).__round__(2)
sse4 = sum(l4).__round__(2)
sse5 = sum(l5).__round__(2)

print(f"SSE using Slope Formula : {sse1}")
print(f"SSE using OLS : sum( xy ) / sum ( x^2 ) : {sse2}")
print(f"SSE using OLS : sum( y^2 ) / sum ( xy ) : {sse3}")
print(f"SSE by taking mean of #2 and #3 : {sse4}")
print(f"SSE of Linear Regression Result Online : {sse5}")
