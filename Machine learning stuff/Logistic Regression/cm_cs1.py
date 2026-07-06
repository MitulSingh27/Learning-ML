import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix


df = pd.DataFrame({
    "temperature":[40,42,45,48,50,70,72,75,78,80],
    "vibration":[0.2,0.3,0.3,0.4,0.5,1.2,1.3,1.5,1.6,1.8],
    "current":[10,11,10,12,11,18,19,20,21,22],
    "failure":[0,0,0,0,0,1,1,1,1,1]
})
x=df[['temperature','vibration','current']]
y=df['failure']
model=LogisticRegression()

x_train,x_test,y_train,y_test=train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

model.fit(x_train,y_train)
predictions=model.predict(x_test)
print(y_test)
print(predictions)
accuracy=accuracy_score(
    y_test,
    predictions
)
print(accuracy)
print(confusion_matrix(y_test,predictions))
print(model.predict_proba([[55,0.7,14]]))
print(model.predict_proba([[68,1.0,17]]))