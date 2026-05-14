#LINEAR REGRESSION FROM SCRATCH
'''
We are goint to implement
prediction
loss (MSE)
gradient descent
parameter updates
these are the things librarires like sklearn do internally 
'''
#STEP 0-- SET UP DATA

import numpy as np
#data
X=np.array([1,2,3,4,5]).reshape(-1,1)
y=np.array([42,48,65,69,78])

#STEP 1: INITIALISE PARAMETERS
m=0 #slope
b=0 #intercept  
learning_rate=0.01
epochs=1000 #the model will go through our data 1000 times to learn
#too few epochs- underfitting, too many- overfitting
n=len(X)

#STEP 2: PREDICTION FUNCTION
def predict(X,m,b):
    return m*X+b

#STEP 3: LOSS FUNCTIONS (MSE)
def compute_loss(y,y_pred):
    return np.mean((y-y_pred)**2)

#STEP 4: GRADIENT DESCENT LOOP