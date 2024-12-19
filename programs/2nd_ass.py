import matplotlib.pyplot as plt

X = [0, 2, 4, 6, 8]
Y1 = [0, 4, 16, 36, 64]
Y2 = [0, 2, 4, 6, 8]

plt.plot(X, Y1, color='blue', linestyle='--', marker='o', label='Line 1: Quadratic')
plt.plot(X, Y2, color='red', linestyle=':', marker='s', label='Line 2: Linear')

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Multiple Lines on Same Axes')
plt.legend()

plt.show()
