import os
import numpy as np
from pyparsing import alphas




alphas = np.linspace(0.1,1.0,5)
l1_ratios = np.linspace(0.1,1.0,5)

#This is a driver

for alpha in alphas:
    for l1 in l1_ratios:
        print(f"logging experiment for alpha: {alpha} and l1_ratio {l1}")
        os.system(f"python demo.py -a {alpha}   -l1 {l1}")
