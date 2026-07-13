from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

X=[
    [25,30000],
    [35,60000],
    [45,80000],
    [20,25000],
    [50,90000],
    [23,28000]
]
y=["No", "Yes", "Yes", "No", "Yes", "No"]
model=DecisionTreeClassifier(random_state=42)
model.fit(X,y)

plt.figure(figsize=(10,6))
plot_tree(
    model,
    feature_names=["Age", "Income"],
    class_names=["No", "Yes"],
    filled=True
)
plt.show()