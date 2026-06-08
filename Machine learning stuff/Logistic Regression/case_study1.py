import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

import pandas as pd

df = pd.DataFrame({
    "income":[25,30,35,40,45,50,55,60,65,70],
    "credit_score":[500,520,550,580,600,650,680,700,720,750],
    "existing_loans":[3,3,2,2,2,1,1,1,0,0],
    "approved":[0,0,0,0,0,1,1,1,1,1]
})

x=df[['income','credit_score','existing_loans']]
y=df['approved']

x_train,x_test,y_train,y_test=train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)
model=LogisticRegression()
model.fit(x_train,y_train)
prediction=model.predict(x_test)
print(y_test)
print(prediction)
print(model.predict_proba(x_test))
accuracy=accuracy_score(y_test,prediction)
print(accuracy)

print(model.predict([[48,620,2]]))
print(model.predict_proba([[48,620,20]]))
print(model.predict_proba([[48,680,1]]))

