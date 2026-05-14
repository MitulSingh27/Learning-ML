import numpy as np

# rows = students, columns = subjects
marks = np.array([
    [85, 78, 92],
    [60, 65, 70],
    [90, 88, 95],
    [50, 55, 60],
    [75, 80, 85]
])

print(marks)

#student avg
student_avg=np.mean(marks,axis=1)
print(student_avg)

#subject avg
subject_avg=np.mean(marks,axis=0)
print(subject_avg)

#overall topper
overall_topper=np.mean(marks,axis=1)
print(np.max(overall_topper))

#subject topper
subject_topper=np.argmax(student_avg)
print(marks[subject_topper])

#passing
print(np.all(marks>=60,axis=1))

#bonusmarks
print(marks+5)

#normalization
