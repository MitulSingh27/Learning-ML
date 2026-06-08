#An EV startup wants to predict driving range based on battery capacity.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error

'''
| Battery Capacity (kWh) | Range (km) |
| ---------------------- | ---------- |
| 20                     | 150        |
| 25                     | 185        |
| 30                     | 220        |
| 35                     | 255        |
| 40                     | 290        |
| 45                     | 325        |
| 50                     | 360        |
| 55                     | 395        |
| 60                     | 430        |
| 65                     | 465        |
| 70                     | 500        |
| 75                     | 535        |

'''
capacity=np.array([20,25,30,35,40,45,50,55,60,65,70,75]).reshape(-1,1)
range=np.array([150,185,220,255,290,325,360,395,430,465,500,535])

x=capacity
y=range
x_train,x_test,y_train,y_test= train_test_split(
    capacity,
    range,
    test_size=0.2,
    random_state=42
)
model=LinearRegression()
model.fit(x_train,y_train)
prediction=model.predict(x_test)
print(model.coef_,'\n',model.intercept_)
print(x_test)
print(y_test)
print(prediction)
print(mean_squared_error(y_test,prediction))
print(mean_absolute_error(y_test,prediction))
