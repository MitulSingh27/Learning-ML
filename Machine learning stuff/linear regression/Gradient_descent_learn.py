#GRADIENT DESCENT LOGIC AND UNDERSTANDING
import numpy as np
X=[1,2,3]
y=[2,4,6]
m=0
b=0
learning_rate=0.1
n=3

#step 1, predictions
y_pred=m*X+b #since m and b=0, x=0
#therefore, y_pred=[0,0,0,0]

#step 2: errors
#y-y_pred=[2,4,6]

#step 3, computing gradients
dm=(-2/n)*sum(X*(y-y_pred))
'''
Let’s compute step by step:

X * error = [1*2, 2*4, 3*6] = [2, 8, 18]
sum = 28

So:

dm = (-2/3) * 28 = -18.67
🔹 Gradient for b
db = (-2/n) * sum(y - y_pred)
sum(error) = 2 + 4 + 6 = 12

So:

db = (-2/3) * 12 = -8

🧠 What do these mean?
dm = -18.67 → slope needs to increase a lot
db = -8 → intercept needs to increase

👉 Negative gradient = “go in positive direction”
'''

#STEP 4: UPDATE
#m=m-learning_rate*b
#b=b-learning_rate*b
'''Substitute:

m = 0 - 0.1 * (-18.67) = 1.867
b = 0 - 0.1 * (-8) = 0.8'''

#new model= y=1.867X + 0.8
#now, the model is closer to the y=2x goal, so it does the entire process again, to get more updated
#the upcoming losses are smaller, which makes the model more accurate over time
