import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
'''
| Age of Car (Years) | Price (Lakhs ₹) |
| ------------------ | --------------- |
| 1                  | 8.5             |
| 2                  | 7.8             |
| 3                  | 7.2             |
| 4                  | 6.5             |
| 5                  | 5.9             |
| 6                  | 5.1             |
| 7                  | 4.7             |
| 8                  | 4.1             |
| 9                  | 3.8             |
| 10                 | 3.2             |
'''

price=np.array([8.5,7.8,7.2,6.5,5.9,5.1,4.7,4.1,3.8,3.2])
age=np.array([1,2,3,4,5,6,7,8,9,10]).reshape(-1,1)

model=LinearRegression()
model.fit(age,price)    #given an age, predict price

predictions=model.predict(age)
print(model.predict([[12]]),
model.predict([[3.5]]),
model.coef_,model.intercept_)
plt.scatter(age,price)
plt.plot(age,predictions,color='red')
plt.show()