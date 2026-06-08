#A real estate company wants to predict house prices based on house size.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
'''
| Area (sq ft) | Price (Lakhs ₹) |
| ------------ | --------------- |
| 800          | 40              |
| 900          | 45              |
| 1000         | 50              |
| 1100         | 55              |
| 1200         | 60              |
| 1300         | 66              |
| 1400         | 70              |
| 1500         | 76              |
| 1600         | 82              |
| 1700         | 88              |
| 1800         | 93              |
| 1900         | 99              |
| 2000         | 104             |
| 2100         | 110             |
| 2200         | 116             |

'''

Area=np.array([800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,2100,2200]).reshape(-1,1)
price=np.array([40,45,50,55,60,66,70,76,82,88,93,99,104,110,116])

X=Area
y=price

X_train,X_test,y_train,y_test = train_test_split(
    Area,
    price,
    test_size=0.2,
    random_state=42 #this makes the train test split the same every time u run
    #otherwise, you will get different sets of training and testing data each time u run the program
) 

model=LinearRegression()
model.fit(X_train,y_train)
predictions=model.predict(X_test)
print(model.coef_,"\n",model.intercept_)
print(X_test,"\n",y_test)
print(predictions)