from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

#Machine learning visuals-

#REGRESSION LINE
X=np.array([1,2,3,4,5]).reshape(-1,1)
y=np.array([2,4,5,4,5])

model=LinearRegression()
model.fit(X,y)

pred=model.predict(X)

plt.scatter(X,y,label="Actual")
plt.plot(X,pred,color='red',label='Prediction')

plt.legend()
plt.show()
#the most imp visualization

#TRAIN TEST COMPARISON
'''
plt.scatter(Y_test,test_preds)
plt.xlabel("Actual")
plt.ylabel("predicted")
plt.title("actual vs predicted)
plt.show()
'''

#RESIDUAL PLOT (error visualization)
'''
residuals=Y_test-test_preds
plt.scatter(test_preds,residuals)   
plt.axhline(y=0,linestyle='--') #creates a horizontal reference line accross the entire plot
plt.xlabel("predicted")
plt.ylabel("residuals")
plt.show()
'''

#LOSS CURVE
'''
loss=[10,8,6,5,3,2]
plt.plot(loss)
plt.title("loss overtime")
plt.xlabel("epochs")
plt.ylabel("loss")
plt.show()
'''

#HISTOGRAM
plt.hist(y, bins=5)
plt.show()

#BAR CHARTS
labels = ["A", "B", "C"]
values = [10, 20, 15]

plt.bar(labels, values)
plt.show()