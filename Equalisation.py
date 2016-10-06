__author__ = 'student'
import numpy as np
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
def value_equalisation(value,  percentiles):
    idx =get_percentile_number(value, percentiles)
    new_value  = idx*1/len(percentiles)
    return new_value
