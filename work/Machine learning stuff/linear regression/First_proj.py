import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score

#STEP 1: RAW DATA
data = {
    "hours": [1,2,3,4,5,6,7,8,9,10],
    "sleep": [6,7,5,8,6,7,5,6,7,8],
    "phone_usage": [5,4,6,3,4,3,5,6,2,1],
    "marks": [42,48,50,65,69,72,78,85,88,95]
}

df = pd.DataFrame(data)
print(df)
#STEP 2: CLEANING DATA
df=df.dropna()
df=df.astype(float)

#STEP 3: DEFINE X AND Y
X=df[['hours','sleep','phone_usage']]
Y=df['marks']

#STEP 4:TRAIN TEST SPLIT
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42) #random state ensures results r reproducile every time

#STEP 5: TRAIN MODEL
model=LinearRegression()
model.fit(X_train,Y_train)

#EVALUATE MODEL
train_preds=model.predict(X_train)
test_preds=model.predict(X_test)
print("train test r2: ",r2_score(Y_train,train_preds))
print("test r2: ",r2_score(Y_test,test_preds))
print("mean_squared_error: ",mean_squared_error(Y_test,test_preds))
print("Weights:", model.coef_)
print("Intercept:", model.intercept_)
new_data=pd.DataFrame([[7,7,2]],columns=['hours','sleep','phone_usage'])
print(model.predict(new_data))

