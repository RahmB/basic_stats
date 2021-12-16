# Import the matplotlib module here.  No other modules should be used.
# Import plotting library
import matplotlib.pyplot as plt
#import.... 
from os import *
# Import Numpy
import numpy as np


def mean(my_list):   # This is the defintion in the head.
    i = 0
    my_sum = 0
    for number in my_list:
        my_sum = my_sum + my_list[i]
        i+=1
    mu = my_sum / i
    print('mean = ' + str(mu))
        
    return mu

def sd(my_list):
    j = 0
    sigma = 0
    my_sumsd = 0
    mu = mean(my_list)
    for number in my_list:
        my_sumsd = my_sumsd + (my_list[j] - mu)**2
        j +=1
    sigma = (my_sumsd/j)**(.5)
    print('standard deviation = ' + str(sigma))
    return sigma
    
def norm(my_list):
    k = 0
    l = 0
    mu = mean(my_list)
    sigma = sd(my_list)
    for number in my_list:
        if abs(my_list[l] - mu) < sigma:
            k += 1
            l += 1
        else:
            l += 1
    dist = k / l
    return dist
     
def is_norm(my_list):
    dist = norm(my_list)
    if 0.66 < dist < 0.70:
        print('Data is normally distributed')
        return True
    else:
        print('Data is not normally distributed')
        return False
    
def is_skew(my_list):
    m = 0
    skew = 0
    sumsk = 0
    mu = mean(my_list)
    sigma = sd(my_list)
    for numbers in my_list:
        sumsk = (my_list[m] - mu)**3 + sumsk
        m +=1
        
    skew = sumsk /(len(my_list)*sigma**3)
    print('skewness = ' + str(skew))

    if skew == 0:
        print('skewness = 0, therefore sample is normally distributed')
    else:
        print('skewness =/= 0, therefore sample is not normally distributed')
    
def graph(my_list):

    plt.hist(my_list,density=True, facecolor='b')
    sigma = sd(my_list) #stores standard deviation
    mu = mean(my_list) #stores mean



    plt.title('my_list Histogram')
    plt.xlabel('Number')
    plt.ylabel('Probability')
    
    plt.xlim(mu - 4*sigma, mu + 4*sigma)
    plt.grid(True)
    plt.show()

    
def stats(my_list):
    mu = mean(my_list)
    std = sd(my_list)
    dist = norm(my_list)
    graph(my_list)
    is_norm(my_list)
    is_skew(my_list)
    return (mu, std, dist)
    