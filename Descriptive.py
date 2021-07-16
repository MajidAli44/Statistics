from statistics import mode
from statistics import median
from statistics import mean
import numpy as np


list=[1,2,3,4,5,67,8,9,8,7,6,5,4]

print(f'maen is {mean(list)}')

print(f'mode is :{mode(list)}')

print(f"median is :{median(list)}")

print(f'Standard Deviation is :{np.std(list)}')

print(f'Variance is :{np.var(list)}')



