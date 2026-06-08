#Linear regression
#simplest, most important idea in ML
#predicting a number

#at its heart, linear regression is- a function that maps input and gives an output based on that
#finding the best straight line that predicts something
#For linear regression, its y=mx+b
#ex- input=hours studied
#   -output=marks
#the model learns, marks=m*hours+b

'''But how does the model “learn”?

This is where things get interesting.

The model:

Guesses values of m and b
Checks error
Improves guess
Repeats'''

# there is a formula to check errors, called mean squared error, bigger error- bad model, smaller error-good model
#model improves using gradient descent

#first real something-
from sklearn.linear_model import LinearRegression 
import numpy as np
model=LinearRegression()
hours = np.array([1,2,3,4,5]).reshape(-1,1)
marks = np.array([42,48,65,69,78])
model.fit(hours,marks)
#print(model.predict([[6]]),model.coef_,model.intercept_)
#this means the model is y=9.1x+33
#on putting x=6, we get 88.3

#Understand Inputs and Outputs

# 1.X----> features
'''hours = [[1],
            [2],
            [3],
            [4],
            [5]]'''
#5 data points-(rows), 1 feature (column), hence shape is 5,1

# 2.y--->target (what you wanna predict)
#marks = [42,48,65,69,120]
# shape = (5,)
'''
⚡ Relationship between them

Each row maps like:

X (hours)	y (marks)
1	            42
2	            48
3	            65
4	            69
5	            78
'''
# 3.Reshape(-1,1)   -1---> figure out rows automatically, 1---> force 1 column

# 4.Single vs Multiple features- single vs multiple columns
#single- y=mx+c 
#multiple-y= w1+x1 + w2+x2 + w3+x3...... 

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
model=LinearRegression()
hours = np.array([[1,2,3,4,5,6],[4,5,6,5,4,8]]).reshape(-1,2)
marks = np.array([42,48,65,69,72,88])
model.fit(hours,marks)
print(model.predict([[6,7]]),model.coef_,model.intercept_)  #6 hours of study and 7 hours of sleep, we r predicting that
# marks=1.56⋅(hours)+6.89⋅(sleep)+23.55


# LOSS FUNCTION
#most imp func-mean squared error (MSE)
# in short,it is summation of error=(actual-predicted)^2 for each data point,^2 because +ve
# now avg this
'''⚡ Example (your level)
Actual(y)	Predicted (ŷ)	Error	Squared
42	            40	          2	       4
48	            50	         -2	       4
65	            60	          5	       25
MSE=avg of square errors
'''
#squared because it punishes big mistakes more and doesnt give negative values
#model.fit(X,y) tries to find the best values of m and b so that MSE is as small as possible
preds=model.predict(hours)
print(mean_squared_error(marks,preds))
'''
Imagine:

Each line = a guess
MSE = score of that guess

Model tries:

many lines
picks the one with lowest score
'''

# GRADIENT DESCENT
#it is a method to find the best weights by reducing errorr step by step
#systematic way to reduce mse
#incremental steps towards lowest point (minimum error)
'''🧠 What’s happening step-by-step
Start with random m, b
Calculate predictions
Compute MSE
Compute gradient (how wrong)
Update m, b
Repeat'''
#This is what the model is doing mathematically
#alfa-learning rate
#m = m - α * derivative_of_error_wrt_m
#b = b - α * derivative_of_error_wrt_b

#EVALUATION
# 3 major metrics
'''
📉 1. Mean Squared Error (MSE)
MSE=summation of error=(actual-predicted)^2 for each data point
👉 Meaning:
Average squared error
Lower = better

2. Mean Absolute Error (MAE)
MAE=summation of error=|actual-predicted|
👉 Meaning:
Average absolute difference
Easier to interpret than MSE

3.R score
👉 Meaning:
How well your model explains the data

⚡ R² Interpretation
R² Score	    Meaning
1.0	            Perfect fit 🔥
0.9+	        Very good
~0.5	        Meh
0	            Useless
< 0	            Worse than guessing ❌
'''
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

preds = model.predict(hours)

print("MSE:", mean_squared_error(marks, preds))
print("MAE:", mean_absolute_error(marks, preds))
print("R2:", r2_score(marks, preds))

'''
🧠 What each metric tells you
MSE
Punishes big mistakes heavily
Sensitive to outliers
MAE
Straightforward error
“On average, how wrong am I?”
R²
Overall quality of fit
Most commonly asked in interviews
⚠️ CRITICAL CONCEPT (don’t skip)

👉 A model can have:

low error on training data
but still be bad in real life

Why?

Because it might just be memorizing

⚡ Real-world intuition

Imagine:

MSE → “How bad are my worst mistakes?”
MAE → “How wrong am I on average?”
R² → “How much of the pattern did I capture?”
'''

#REAL WORLD PROBLEMS
#The 3 big enemies:
#Overfitting
#Underfitting
#Noisy data

#OVERFITTING
'''
model learns data too well, it memorizes instead of picking patterns
works perfect on training data and shit on new data

visually-Instead of a straight line
Model creates a wiggly curve to pass through every point

Why it happens
Too complex model
Too little data
Too many features
'''

#UNDERFITTING
'''
model is too simple
cant capture pattern and even training performance is bad

visually-data is curved but model line is straight

Why it happens
model is too simple
not enough features
poor training
'''

#NOISY DATA
'''
Real data is messy and inconsistent

ex-[42, 48, 65, 69, 120]
120 is an outlier
but, model shifts towards it and predictions become worse
'''

#HOW TO DETECT THE 3 
'''
How to detect these (IMPORTANT)
Compare:
Metric	        Training	    Testing
Overfitting	    Very good	    Bad
Underfitting	    Bad	        Bad
Good model	        Good	    Good
'''
#How to check for the 3 using code
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(hours,marks,test_size=0.2)
model.fit(X_train,Y_train)

train_preds=model.predict(X_train)#predictions on training data
test_preds=model.predict(X_test)#predictions on testing data
print(train_preds,test_preds,"predictions")
print(Y_train,Y_test,"actual answers")

#test_size=0.2 20% data testing,80% for training, 4 points training 1 for testing 
#if you train all data, the model just memorizes data and overfits, splitting helps it actually learn
#[69.16666667 60.66666667 72. 52.16666667] [35.16666667 69.16666667] predictions
#[65 69 72 48]                             [42 88] actual answers
#now, mean absolute error and mean squared error can be calculated using the formulas and side
#by side prediction comparisons

#SOLUTIONS FOR THE 3
#overfitting
'''
more data
simple model
remove useless features
'''
#underfitting
'''
add more features
more complex model
'''
#Noise
'''
clean data
remove outliers
use robust metrics
'''

#MULTIVARIABLE LINEAR REGRESSION
#instead of using one input, we use many
#before--> hours->> marks
#now--> hours,sleep,attendence-->> marks

#the new model= y=w1x1+w2x2+w3x3+.....+b
#now its not a simple line anymore, it is a multi dimensional plane

#correct data format
X = [
  [hours, 'sleep', 'attendance'],
  [hours, 'sleep', 'attendance'],
  [hours, 'sleep', 'attendance']
]
#example
X = [               #all the different features
  [2, 6, 80],
  [4, 7, 90],
  [6, 8, 95],
  [8, 5, 85]
]

y = [50, 65, 75, 70] #marks

#shape matters a lot
#X.shape-->(4,3)
#Y.shape-->(1,4)

#what the model learns
#model.coeff(5.2,2.1,0.3) it got this by trial and error, refer to gradient descent

#full example
from sklearn.linear_model import LinearRegression
X = [               #all the different features
  [2, 6, 80],
  [4, 7, 90],
  [6, 8, 95],
  [8, 5, 85]
]

Y = [50, 65, 75, 70] #marks
model=LinearRegression()
model.fit(X,Y)
print(model.coef_)
print(model.predict([[7,7,89]]))
