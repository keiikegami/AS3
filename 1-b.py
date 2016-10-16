import numpy as np
import matplotlib.pyplot as plt
% matplotlib inline
import pandas as pd

y = q1.values[:, 1]
def pos(sigma):
    return np.exp(sigma*np.dot(y, y)/(2*(sigma + 1)) - sum(y)/2) / (sigma*(np.sqrt(2*np.pi * (sigma + 1)))**100)

np.random.seed(1234)
samples = [10]
for i in range(10000):
    u = np.random.uniform()
    propose = samples[-1] + np.random.normal(scale = 0.5)
    prob = min(1, pos(propose)/pos(samples[-1]))
    
    if prob < u:
        samples.append(samples[-1])
    else:
        samples.append(propose)

plt.figure(figsize = (10, 8))
plt.title("trace plot")
plt.plot(samples)
plt.show()