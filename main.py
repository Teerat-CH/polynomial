import numpy as np
from matplotlib import pyplot as plt

n = int(input("Enter number count"))

list_of_sequence = []

for i in range(n):
    list_of_sequence.append(int(input('Enter your numbers : ')))


x = [1,2,3,4,5]
y = [1,2,3,4,5]

coefficients = np.polyfit(x, y, 3)

poly = np.poly1d(coefficients)

new_x = np.linspace(x[0], x[-1])

new_y = poly(new_x)

plt.plot(x, y, "o", new_x, new_y)