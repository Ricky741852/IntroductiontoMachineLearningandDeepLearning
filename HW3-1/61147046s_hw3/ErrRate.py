import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb
import math

def output(e_base: float):
    n = 15
    probs = [comb(n, i) * e_base**i * (1-e_base)**(n-i)
             for i in range(math.ceil(n/2), n+1)]
    e_ensemble = sum(probs)
    # print("The ensemble error rate = {:.3f} when error rate = {:.3f}\n".format(e_ensemble, e_base))
    return "The ensemble error rate = {:.3f} when error rate = {:.3f}\n".format(e_ensemble, e_base)

def draw():
    n = 15
    e_bases = np.arange(0, 1, 0.0001)
    e_ensembles = [sum([comb(n, i) * e_base**i * (1-e_base)**(n-i)
                        for i in range(math.ceil(n/2), n+1)])
                   for e_base in e_bases]
    plt.plot(e_bases,
             e_ensembles,
             label='Ensemble error')

    plt.plot(e_bases,
             e_bases,
             linestyle='--',
             label='Base error')
    plt.grid(True)
    plt.title('ErrRate')
    plt.xlabel('Base error')
    plt.ylabel('Base/Ensemble error')
    plt.savefig('Ensemble_error.png')
    plt.show()



