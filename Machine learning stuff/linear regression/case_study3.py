#A drone company wants to estimate flight time based on payload weight.
#The heavier the payload, the shorter the flight time.
#Your task:
#Predict drone flight time from payload weight.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

'''
dataset-
| Payload Weight (kg) | Flight Time (minutes) |
| ------------------- | --------------------- |
| 0                   | 42                    |
| 1                   | 39                    |
| 2                   | 37                    |
| 3                   | 35                    |
| 4                   | 32                    |
| 5                   | 30                    |
| 6                   | 27                    |
| 7                   | 25                    |
| 8                   | 23                    |
| 9                   | 20                    |

'''
Payload_weight=np.array([0,1,2,3,4,5,6,7,8,9]).reshape(-1,1)
Flight_time=np.array([42,39,37,35,32,30,27,25,23,20])
model=LinearRegression()
model.fit(Payload_weight,Flight_time)
prediction=model.predict(Payload_weight)
print(model.coef_)
print(model.intercept_)
print(model.predict([[2.5]]))
print(model.predict([[11]]))
plt.scatter(Payload_weight,Flight_time)
plt.plot(Payload_weight,prediction,color="red")
plt.show()


