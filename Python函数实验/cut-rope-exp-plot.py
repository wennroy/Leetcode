from matplotlib import pyplot as plt
import numpy as np

def total_prod(a, num_split):
    x = a / num_split
    return x ** num_split

a = 60
x = np.array(range(1,a))
y = total_prod(a, x)
plt.plot(x,y)
plt.show()

