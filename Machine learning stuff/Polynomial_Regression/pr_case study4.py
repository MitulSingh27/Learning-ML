#predicting fuel burn using weight and speed

import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score,root_mean_squared_error
Aircraft_Weight = np.array([20,25,30,35,40,45,50,55,60,65])
Cruise_Speed = np.array([300,320,340,360,380,400,420,440,460,480])
Fuel_Burn = np.array([180,220,270,330,400,480,570,670,780,900])

x=np.column_stack((Aircraft_Weight,Cruise_Speed))
y=Fuel_Burn

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
print(mean_squared_error(y_test,predictions))
print(mean_absolute_error(y_test,predictions))
print(root_mean_squared_error(y_test,predictions))
print(r2_score(y_test,predictions))

#polynomial regression
model=LinearRegression()
poly=PolynomialFeatures(degree=2)
x_train_poly,x_test_poly,y_train_poly,y_test_poly=train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)
x_fit_transform=poly.fit_transform(x_train_poly)
x_fit=poly.transform(x_test_poly)
model.fit(x_fit_transform,y_train_poly)
prediction=model.predict(x_fit)
print(y_test_poly,prediction)
print(mean_squared_error(y_test_poly,prediction))
print(mean_absolute_error(y_test_poly,prediction))
print(root_mean_squared_error(y_test_poly,prediction))
print(r2_score(y_test_poly,prediction))