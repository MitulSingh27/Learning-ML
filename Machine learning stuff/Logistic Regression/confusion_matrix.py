'''
accuracy can be misleading

imagine a disease detection model

Dataset-
| Person | Disease |
| ------ | ------- |
| 1      | No      |
| 2      | No      |
| 3      | No      |
| 4      | No      |
| 5      | No      |
| 6      | No      |
| 7      | No      |
| 8      | No      |
| 9      | No      |
| 10     | Yes     |

only 1 person has a disease

suppose predictions are-
No
No
No
No
No
No
No
No
No
No

accuracy is 90%, but the model failed to detect the only sick person in the group
'''

#this is where confusion matrix steps in 

'''
confusion matrix allows us to categorize answers instead of just counting them 

            predicted 0                 predicted 1
actual 0        TN                          FP
actual 1        FN                          TP

1.True Positive (TP)
    actual-1
    predicted-1
2.True Negative (TN)
    acutal-0
    predicted-0
3.False positive (FP)
    actual-0
    predicted-1
4.False negative (FN)
    actual-1
    predicted-0
'''

#from sklearn.metrics import confusion_matrix
