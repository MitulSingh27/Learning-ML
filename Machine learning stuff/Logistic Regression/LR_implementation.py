import pandas as pd

'''
| Hours | Pass |
| ----- | ---- |
| 1     | 0    |
| 2     | 0    |
| 3     | 0    |
| 4     | 0    |
| 5     | 1    |
| 6     | 1    |
| 7     | 1    |
| 8     | 1    |

'''

df = pd.DataFrame({
    'hours':[1,2,3,4,5,6,7,8],
    'pass':[0,0,0,0,1,1,1,1]
})

#print(df)

#training
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

x=df[['hours']] #sklearn needs 2d X
y=df['pass']

x_train,x_test,y_train,y_test=train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)
model=LogisticRegression()
model.fit(x_train,y_train)
predictions=model.predict(x_test)
print(y_test)
print(predictions)
print(model.predict_proba(x_test)) #returns probability
accuracy=accuracy_score(
    y_test,
    predictions
)
print(model.predict([[5.5]]))
print(model.predict_proba([[5.5]]))

'''
[[0.93626066 0.06373934]
 [0.20070991 0.79929009]]

 each row means-
 [Probability of 0, Probability of 1]
'''