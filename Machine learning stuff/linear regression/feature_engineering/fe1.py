import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error,root_mean_squared_error,r2_score
#A drone company wants to predict flight time.
'''
| Battery (Wh) | Payload (kg) | Flight Time (min) |
| ------------ | ------------ | ----------------- |
| 100          | 1            | 42                |
| 120          | 1            | 50                |
| 120          | 2            | 38                |
| 150          | 2            | 48                |
| 180          | 2            | 58                |
| 180          | 3            | 45                |
| 220          | 3            | 55                |
| 250          | 4            | 52                |
'''
Battery=np.array([100,120,120,150,180,180,220,250])
Payload=np.array([1,1,2,2,2,3,3,4])
Flight_time=np.array([42,50,38,48,58,45,55,52])
battery_per_kg = Battery/Payload
print(battery_per_kg)