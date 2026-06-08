import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

engine_size = np.array([1,2,3,4,5,6])
horsepower = np.array([100,400,900,1600,2500,3600])

x=engine_size.reshape(-1,1)
y=horsepower

poly=PolynomialFeatures(degree=2)
x_poly=poly.fit_transform(x)
print(x_poly)
print(x_poly.shape)#(1,x,x^2)

model=LinearRegression()
model.fit(x_poly,y)
predictions=model.predict(x_poly)
print(y)
print(predictions)


