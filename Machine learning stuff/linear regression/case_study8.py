#A company wants to predict daily energy production from solar panel area.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error,root_mean_squared_error

'''
| Solar Panel Area (m²) | Energy Produced (kWh/day) |
| --------------------- | ------------------------- |
| 5                     | 18                        |
| 10                    | 35                        |
| 15                    | 50                        |
| 20                    | 68                        |
| 25                    | 84                        |
| 30                    | 102                       |
| 35                    | 118                       |
| 40                    | 135                       |
| 45                    | 150                       |
| 50                    | 168                       |
'''

area=np.array([5,10,15,20,25,30,35,40,45,50]).reshape(-1,1)
energy=np.array([18,35,50,68,84,102,118,135,150,168])

x=area
y=energy

x_train,x_test,y_train,y_test= train_test_split(
    area,
    energy,
    test_size=0.2,
    random_state=42
)

model=LinearRegression()
model.fit(x_train,y_train)
predictions=model.predict(x_test)
print(model.coef_,'\n',model.intercept_)
print(x_test)
print(y_test)
print(predictions)
print(mean_squared_error(y_test,predictions))
print(mean_absolute_error(y_test,predictions))
print(root_mean_squared_error(y_test,predictions))