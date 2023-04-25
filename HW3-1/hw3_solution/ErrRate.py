
import numpy as np
import matplotlib.pyplot as plt

def factorial_loop (n):
    factor = 1
    for i in range(1,n+1):
        factor *= i
    return factor

def err_rate(e_base: float): 
    # TODO: caculate the ensemble error rate 
    e_ensemble = 0
    for i in range(8,16):
        e_ensemble += factorial_loop(15)/factorial_loop(i)/factorial_loop(15-i)*(e_base**i)*((1-e_base)**(15-i))

    return e_ensemble

def output(e_base: float): 
    
    # TODO: caculate the ensemble error rate and return a string as sample.out
    e_ensemble = err_rate(e_base)

    return (f'The ensemble error rate = {e_ensemble:.3f} when error rate = {e_base:.3f}')


def draw():
    e_bases = np.arange(0,1, 0.0001)
    e_ensembles = [err_rate(e) for e in e_bases]
    # TODO: plot and save the relationship of e_base vs e_ensemble
    plt.plot(e_bases, e_ensembles)
    plt.savefig('Ensemble_error.png')



