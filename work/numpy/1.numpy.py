#numpy=numeric python
#used for fast maths and arrays
#python lists too slow and not vectorised
#numpy is fast (backed by C), supports matrix operations

#Numpy arrays
import numpy as np
import random

a=np.array([1,2,3])
print(a)

print(a.shape) #prints shape

print(a.ndim)  #returns number of dimensions,  n dimensions

print(a.dtype) #prints datatype

#2d arrays
b=np.array([[1,2,3],[4,5,6]])
print(b)


#Array creation methods
np.array([1,2,3])   #basic

np.zeros((2,3))     #zeros matrix

np.ones((2,3))      #fully one matrix

np.eye(3)           #identity matrix



#Indexing and slicing- same as list for 1d
#2d
c=np.array([[1,2],[3,4]])
#[rows,columns]
print(c[0,1])   #2
print(c[:,0])   #First column-[1,3]
# all rows from column 0


#Array operation between rows
d=np.array([1,2,3])
print(d+2)  #all elements added to 2
print(d*2)  #all elements multiplied by 2
print(d**2) #all elements power to 2


#Array operation between arrays
d=np.array([1,2,3])
e=np.array([1,2,3])
print(a+b)  #[5,7,9]
print(a*b)  #[4,10,18]


#Mathematical functions
e = np.array([1,4,9])
print(
    np.sqrt(e),
    np.sin(e),
    np.tan(e),
    np.log(e),
    np.exp(e)
)

#Broadcasting
f = np.array([[1,2,3],
              [4,5,6]])

g = np.array([1,1,1])
print(f + g) #[[2 3 4],[5 6 7]]

#Shape manipulation
h=np.arange(9)
h.reshape(3,3)  #converts one dimensional array to 3x3 format
h.flatten()     #converts back to one dimensional 
np.transpose(h)           #transpose


#Aggregate functions
h=np.array([1,2,3,4,5])
print(np.sum(h),
      np.mean(h),
      np.min(h),
      np.max(h),
      np.std(h) #standard deviation-tandard deviation tells you how spread out the values are from the average (mean).
      )
i = np.array([[1,2],[3,4]])
print(np.sum(i,axis=0), #sum columnwise
    np.sum(i,axis=1)) #sum rowise

#linear Algebra
j = np.array([[1,2],[3,4]])
k = np.array([[5,6],[7,8]])
    #matrix multiplication
print(np.dot(j,k))
#OR
print(j @ k)
    #determinant
np.linalg.det(j)
    #inverse
np.linalg.inv(k)
    #Eigenvalues
np.linalg.eig(j)

#Random Module
print(np.random.rand(2,3),     # 0 to 1
np.random.randn(2,3),    # normal distribution
np.random.randint(1,10, size=(2,3)))

np.random.seed(42) #important for reproducability
