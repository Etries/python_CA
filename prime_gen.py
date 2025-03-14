#! /usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import random

#PART A

def part_a_example():
    """ This is for demonstration adn testing pupose only"""
    
    xarray = np.array(range(1, 11))
    y1array = np.array([101, 103, 107, 109, 113, 127, 131, 137, 139, 149])
    y2array = np.array(sorted(list(range(121, 131)), reverse=True))


    plt.figure(figsize=(10, 6))
    # // Plot the data //
    plt.plot(xarray, y1array, label='Series 1')
    plt.plot(xarray, y2array, label='Series 2')
    # // Add title and legend //
    plt.title('Graph of two number series')
    plt.legend()
    # // Display the plot //
    plt.grid(False) # Equivalent to unset='grid'
    plt.show()



# PART B
def graph_plotter(n_array):
    """ matplot example from the CA was utlised in this function"""

    
    xarray = np.array(n_array[0])
    yarray = np.array(n_array[1])
    plt.figure(figsize=(10, 6))
    plt.plot(xarray, yarray, label='Series 1')
    plt.legend()
    # // Display the plot //
    plt.grid(False) # Equivalent to unset='grid'
    plt.show()

    
def prime_generator(size_limit):
    """ This is a prime generator"""

    m = 2
    factors = []
    while m <= size_limit:
        for x in range(1, m+1):
            if m % x == 0:
                factors.append(x)
        if len(factors) == 2:
            yield m
        factors.clear()
        m += 1

def main():
    
    
    size = 1000
    xsize  = 10

    #A list to store prime numbers generated
    prime_pool = list(prime_generator(size))

    #A random index from 0 upto "size" amount less than the pool
    random_index = random.randint(0, len(prime_pool)- xsize) 
    x_array = np.arange(1,11)
    y_array = np.array(prime_pool[random_index: random_index+xsize])
    
    #stacked both arrays into one to get a 2-dim numpy.ndarray
    two_dim_array = np.vstack((x_array, y_array))
    graph_plotter(two_dim_array)
   
if __name__ == "__main__":
    main()
