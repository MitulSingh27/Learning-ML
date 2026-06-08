#A factory wants to predict daily production based on machine operating hours.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error,root_mean_squared_error,r2_score

#R^2 answers-"How much of the variation in the data did the model explain?"
'''
| Hours Studied | Marks |
| ------------- | ----- |
| 1             | 20    |
| 2             | 95    |
| 3             | 40    |
| 4             | 80    |

r^2 will be close to 0 because the data is almost random, a linear model cannot explain anything
'''

'''
| Machine Hours | Units Produced |
| ------------- | -------------- |
| 2             | 110            |
| 3             | 125            |
| 4             | 145            |
| 5             | 160            |
| 6             | 178            |
| 7             | 195            |
| 8             | 210            |
| 9             | 228            |
| 10            | 245            |
| 11            | 262            |
| 12            | 280            |
| 13            | 295            |

'''

hours=np.array([2,3,4,5,6,7,8,9,10,11,12,13]).reshape(-1,1)
units=np.array([110,125,145,160,178,195,210,228,245,262,280,295])
x=hours
y=units

x_test,x_train,y_test,y_train=train_test_split(
    hours,
    units,
    test_size=0.8,
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
print(r2_score(y_test,predictions))