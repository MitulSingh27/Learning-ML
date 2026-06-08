#predict battery health from charge cycles
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score,root_mean_squared_error

'''
| Cycles | Health |
| ------ | ------ |
| 100    | 99     |
| 200    | 97     |
| 300    | 95     |
| 400    | 92     |
| 500    | 88     |
| 600    | 83     |
| 700    | 77     |
| 800    | 70     |
| 900    | 62     |
| 1000   | 53     |
'''

Charge_Cycles = np.array([100,200,300,400,500,600,700,800,900,1000]).reshape(-1,1)
Battery_Health = np.array([99,97,95,92,88,83,77,70,62,53])
x=Charge_Cycles
y=Battery_Health

#linear regression
model=LinearRegression()
x_train,x_test,y_train,y_test=train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)
model.fit(x_train,y_train)
predictions=model.predict(x_test)
print(y_test,predictions)
print(mean_absolute_error(y_test,predictions))
print(mean_squared_error(y_test,predictions))
print(root_mean_squared_error(y_test,predictions))
print(r2_score(y_test,predictions))

#Poly
model=LinearRegression()
poly=PolynomialFeatures(degree=2)
x_train_poly,x_test_poly,y_train_poly,y_test_poly=train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)
x_tranfsorm=poly.fit_transform(x_train_poly)
x_fit=poly.transform(x_test_poly)
model.fit(x_tranfsorm,y_train_poly)
predictions=model.predict(x_fit)
print(y_test_poly,predictions)
print(mean_absolute_error(y_test_poly,predictions))
print(mean_squared_error(y_test_poly,predictions))
print(root_mean_squared_error(y_test_poly,predictions))
print(r2_score(y_test_poly,predictions))