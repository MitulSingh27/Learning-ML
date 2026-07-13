from sklearn.tree import DecisionTreeClassifier

#training data
X= [
    [25,30000],
    [35,60000],
    [45,80000],
    [20,25000],
    [50,90000],
    [23,28000]
]

#target
y=["No", "Yes", "Yes", "No", "Yes", "No"]

#create the model
model=DecisionTreeClassifier(random_state=42)   #reproducable result

#train the model
model.fit(X,y)
'''
this line is where the gini impurity stuff happens
'''

#make a prediction
prediction=model.predict([[30,50000]])

'''
the data traverses through the tree, and then conditions are matched accordingly
'''
print(prediction)

