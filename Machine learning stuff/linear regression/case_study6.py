#Predict battery life from battery capacity.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error
'''
| Battery Capacity (mAh) | Battery Life (Hours) |
| ---------------------- | -------------------- |
| 2000                   | 8                    |
| 2500                   | 10                   |
| 3000                   | 12                   |
| 3500                   | 14                   |
| 4000                   | 16                   |
| 4500                   | 18                   |
| 5000                   | 20                   |
| 5500                   | 22                   |
| 6000                   | 24                   |
| 6500                   | 26                   |
'''
battery=np.array([2000,2500,3000,3500,4000,4500,5000,5500,6000,6500]).reshape(-1,1)
life=np.array([8,10,12,14,16,18,20,22,24,26])

X=battery
y=life

X_train,X_test,y_train,y_test=train_test_split(
    battery,
    life,
    train_size=0.2,
    random_state=42
)

model=LinearRegression()
model.fit(X_train,y_train)
predictions=model.predict(X_test)
print(model.coef_,"\n",model.intercept_)
print(X_test)
print(y_test)
print(predictions)
print(mean_squared_error(y_test,predictions))