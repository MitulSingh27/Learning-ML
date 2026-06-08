#A vehicle manufacturer wants to estimate fuel efficiency based on vehicle weight.
#Build a model that predicts fuel efficiency (km/l) from vehicle weight (kg).

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

'''
dataset-
| Weight (kg) | Fuel Efficiency (km/l) |
| ----------- | ---------------------- |
| 800         | 24                     |
| 900         | 22                     |
| 1000        | 21                     |
| 1100        | 19                     |
| 1200        | 18                     |
| 1300        | 17                     |
| 1400        | 15                     |
| 1500        | 14                     |
| 1600        | 13                     |
| 1700        | 12                     |

'''
weight=np.array([800,900,1000,1100,1200,1300,1400,1500,1600,1700]).reshape(-1,1)
efficiency=np.array([24,22,21,19,18,17,15,14,13,12])
model=LinearRegression()
model.fit(weight,efficiency)
predictions=model.predict(weight)
print(model.predict([[1800]]))
print(model.predict([[1250]]))
print(model.coef_)
print(model.intercept_)
plt.scatter(weight,efficiency)
plt.plot(weight,predictions,color="red")
plt.show()