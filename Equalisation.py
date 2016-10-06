__author__ = 'student'
import numpy as np
import matplotlib.pyplot as plt
import random
def get_percentile(values, bucket_number):
    P=[0.0]
    for i in range (1, bucket_number):
        P.append(np.percentile(values, 100/bucket_number*i))
    return  P
def get_percentile_number(value,percentiles):
    k=0
    for x in percentiles:
        if x<value:
            k=percentiles.index(x)
    return k
def value_equalisation(value,  percentiles, add_random=True):
    random_noise = random.uniform(0,1/len(percentiles))
    idx = get_percentile_number(value, percentiles)
    if add_random:
        new_value  = idx*1/len(percentiles)+random_noise
    else:
        new_value = idx*1/len(percentiles)
    return new_value


data_file=open('img.txt', 'r')
data=[list(map(float, l.split()))  for l in data_file.readlines()]

fdata = []
for d in data:
    fdata.extend(d)

plt.hist(fdata, bins=150)
plt.show()
p = get_percentile(fdata, 100)

for i in range(len(data)):
    for j in range(len(data[i])):
        data[i][j] = value_equalisation(data[i][j], p)

fdata1 = []
for d in data:
    fdata1.extend(d)
plt.hist(fdata1, bins=150)
plt.show()

plt.imshow(data, cmap = plt.get_cmap('gray'))
plt.show()

