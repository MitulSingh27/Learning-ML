#Matplotlib + ML Case Study
'''
Goal:

Load data
Visualize it
Train a model
Plot predictions
Analyze errors
Build intuition for BOTH ML and Matplotlib
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_squared_error

hours=np.array([1,2,3,4,5,6,7,8]).reshape(-1,1)
marks=np.array([35,40,50,55,60,69,75,82])

plt.scatter(hours,marks)
plt.title("hours vs marks")
plt.xlabel("hours")
plt.ylabel("marks")
plt.show()

model=LinearRegression()
model.fit(hours,marks)
pred=model.predict(hours)

#plot regression line
plt.scatter(hours,marks,label='actual data')
plt.plot(hours,pred,label='regression line')

plt.title("actual vs model")
plt.xlabel("hours")
plt.ylabel("marks")
plt.legend()
plt.show()

predictions=model.predict(([[10]]))
print(predictions)

#Residual visualization
residual=marks-pred

plt.scatter(pred,residual)
plt.axhline(y=0,linestyle='--')
plt.title("residual plot")
plt.xlabel("predictions")
plt.ylabel("residual")
plt.show()

'''
Why Residuals Matter

Perfect model:

all residuals close to 0
points randomly scattered

Bad model:

patterns appear
huge spread appears

Residual plots help diagnose:

underfitting
weird trends
bias
'''

plt.scatter(marks,pred)
plt.show()