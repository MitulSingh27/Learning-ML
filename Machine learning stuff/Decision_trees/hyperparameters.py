from sklearn.tree import DecisionTreeClassifier

"""
trees can become too powerful and memorize values and data instead of patterns 
these are the hyper parameters you will be using often-
"""
#hyperparameters are external configuration variables that you set before training an ML model
model=DecisionTreeClassifier(
    max_depth=3,            #limits how deep the tree can grow
    min_samples_split=2,    #minimum number of samples required before a node is allowed to split
    min_samples_leaf=1,     #minimum number of samples thst must remain in every leaf
    random_state=42         
)