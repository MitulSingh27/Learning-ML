#predict 0 to 100 time

import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score,root_mean_squared_error
Horsepower = np.array([150,200,250,300,400,500,600,700])
Weight = np.array([1300,1350,1400,1450,1500,1550,1600,1650])
ZeroTo100 = np.array([9.5,8.2,7.4,6.6,5.2,4.2,3.6,3.1])

#Linear model
model=LinearRegression()
x=np.column_stack((Horsepower,Weight))
y=ZeroTo100
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

#Poly model
model=LinearRegression()
poly=PolynomialFeatures(degree=2)
x_train_poly,x_test_poly,y_train_poly,y_test_poly=train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)
poly_train=poly.fit_transform(x_train_poly)
poly_test=poly.transform(x_test_poly)

model.fit(poly_train,y_train_poly)

predictions=model.predict(poly_test) #poly_test is the already transformed value
print(y_test_poly,predictions)
print(mean_absolute_error(y_test_poly,predictions))
print(mean_squared_error(y_test_poly,predictions))
print(root_mean_squared_error(y_test_poly,predictions))
print(r2_score(y_test_poly,predictions))
