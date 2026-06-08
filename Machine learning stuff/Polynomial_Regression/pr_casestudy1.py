#flight time prediction

import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score,root_mean_squared_error

Battery = np.array([100,120,120,150,180,180,220,250])
Payload = np.array([1,1,2,2,2,3,3,4])
Flight_Time = np.array([42,50,38,48,58,45,55,52])

x=np.column_stack((Battery,Payload))
y=Flight_Time

x_train,x_test,y_train,y_test=train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)
#baseline linear model and metrics
model=LinearRegression()
model.fit(x_train,y_train)
prediction=model.predict(x_test)
mae=mean_absolute_error(y_test,prediction)
mse=mean_squared_error(y_test,prediction)
r2=r2_score(y_test,prediction)
rmse=root_mean_squared_error(y_test,prediction)
print(mae,'\n',mse,'\n',r2,'\n',rmse)

#polynomial stuff
poly=PolynomialFeatures(degree=2)
x_train_poly=poly.fit_transform(x_train)
x_test_poly=poly.transform(x_test)
poly_model=LinearRegression()
poly_model.fit(
    x_train_poly,
    y_train
)
poly_predictions=poly_model.predict(x_test_poly)

mae=mean_absolute_error(y_test,poly_predictions)
mse=mean_squared_error(y_test,poly_predictions)
r2=r2_score(y_test,poly_predictions)
rmse=root_mean_squared_error(y_test,poly_predictions)
print(mae,'\n',mse,'\n',r2,'\n',rmse)

#in this case, overfitting has happened in case of polynomial regression
#how do we know this, the model went from 8 rows, 2 cooumns to 8 rows, 6 columns, and had too much freedom 
#thats why it was overfitting 
#the model learns patterns and noise instead of just patterns
