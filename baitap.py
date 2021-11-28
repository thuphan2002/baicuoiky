# Bài toán dự đoán cân nặng dựa trên chiều cao
from __future__ import division, print_function, unicode_literals
import numpy as np
import matplotlib.pyplot as plt

# height (cm)
X = np.array([[140, 150, 160, 170, 180, 190]]).T
# weight (kg)
y = np.array([[40, 55, 63, 75, 80, 100]]).T

plt.plot(X, y, 'go')
plt.axis([140, 190, 40, 100])
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()

# Building Xbar
one = np.ones((X.shape[0], 1))
Xbar = np.concatenate((one, X), axis = 1)

# Calculating weights of the fitting line
A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)
w = np.dot(np.linalg.pinv(A), b)
print('w = ', w)
# Preparing the fitting line
w_0 = w[0][0]
w_1 = w[1][0]
x0 = np.linspace(140, 180, 2)
y0 = w_0 + w_1*x0

# Drawing the fitting line
plt.plot(X.T, y.T, 'go')     # data
plt.plot(x0, y0)               # the fitting line
plt.axis([140, 190, 40, 100])
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()

y1 = w_1*155 + w_0
y2 = w_1*165 + w_0
print('Dự đoán cân nặng của người cao 155 cm: %.2f (kg), số thực : 52 (kg)'  %(y1) )
print('Dự đoán cân nặng của người cao 165 cm: %.2f (kg), số thực : 56 (kg)'  %(y2) )