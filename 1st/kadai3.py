# kadai3.py
# バージョンは 3.11.9

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.5) # 3-1
plt.ylim(-10, 10)
fx = 1 / x
gx = x
hx = x ** 2
kx = x ** 3
plt.plot(x, fx, label="f(x)=1/x")
plt.plot(x, gx, linestyle="--", label="g(x)=x")
plt.plot(x, hx, linestyle="-.", label="h(x)=x^2")
plt.plot(x, kx, linestyle=":", label="k(x)=x^3")
plt.legend()
print("課題4-1")
plt.show()

x = np.arange(-1, 4, 0.1) # 3-2
y = 3.7 * x ** 2 - 7.0 * x + 3.1
plt.plot(x, y)
r = np.random.normal(0, 7, 50)
plt.scatter(x, y + r, color="red")
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
print("課題4-2")
plt.show()