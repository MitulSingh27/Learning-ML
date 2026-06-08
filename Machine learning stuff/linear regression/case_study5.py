#Laptop Price Prediction
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
'''
| RAM (GB) | Price (₹ Thousands) |
| -------- | ------------------- |
| 4        | 30                  |
| 8        | 45                  |
| 12       | 58                  |
| 16       | 72                  |
| 20       | 85                  |
| 24       | 100                 |
| 28       | 112                 |
| 32       | 128                 |
| 36       | 140                 |
| 40       | 155                 |
'''
ram=np.array([4,8,12,16,20,24,28,32,36,40]).reshape(-1,1)
price=np.array([30,45,58,72,85,100,112,128,140,155])
X=ram
y=price

X_train,X_test,y_train,y_test=train_test_split(
    ram,
    price,
    test_size=0.2,
    random_state=42
)

model=LinearRegression()
model.fit(X_train,y_train)
prediction=model.predict(X_test)
mae=mean_absolute_error(y_test,prediction)
print(mae)
print(model.coef_,"\n",model.intercept_)
print(X_test)
print(y_test)
print(prediction)