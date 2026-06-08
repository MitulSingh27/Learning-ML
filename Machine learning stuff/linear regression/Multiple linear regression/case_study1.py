#An EV startup wants to predict battery pack cost.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error,root_mean_squared_error,r2_score
'''
| Capacity (kWh) | Cells | Cooling Score | Cost (₹ Lakhs) |
| -------------- | ----- | ------------- | -------------- |
| 40             | 100   | 5             | 4.0            |
| 50             | 120   | 6             | 5.2            |
| 60             | 140   | 7             | 6.1            |
| 70             | 160   | 8             | 7.0            |
| 80             | 180   | 9             | 8.3            |
| 90             | 200   | 10            | 9.1            |
| 100            | 220   | 11            | 10.5           |
| 110            | 240   | 12            | 11.4           |
'''

capacity=np.array([[40,100,5],[50,120,6],[60,140,7],[70,160,8],[80,180,9],[90,200,10],
                    [100,220,11],[110,240,12]]).reshape(-1,3)
cost=np.array([4.0,5.2,6.1,7.0,8.3,9.1,10.5,11.4])
x=capacity
y=cost
print(x.shape)
print(y.shape)
print(x[:,0]) #first column
print(x[:,1]) #2nd column

x_train,x_test,y_train,y_test= train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)
model=LinearRegression()
model.fit(x_train,y_train)
predictions=model.predict(x_test)
print(x_test)
print(y_test)
print(predictions)
print(model.coef_)
print(model.intercept_)
print(mean_absolute_error(y_test,predictions),
      mean_squared_error(y_test,predictions),
      root_mean_squared_error(y_test,predictions),
      r2_score(y_test,predictions))

'''
The model learned approximately:

Cost=0.0214(Capacity)+0.0428(Cells)+0.00214(Cooling)−1.20  
'''