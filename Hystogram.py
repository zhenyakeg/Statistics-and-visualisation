__author__ = 'student'
import random
import matplotlib.pyplot as plt

random.seed(0)
n = 9000000
values = [random.normalvariate(0, 1) for i in range(n)]
plt.hist(values, bins=10000)
plt.show()