import numpy as np
import numpy.linalg as la #linear algebra library

a=np.array([1,2,3,5,7],dtype='i')

b=np.array((1,2,3,5,6)) #tuple 
print(a,
      b,
      type(a),
      type(b),
      a.dtype)

c=np.array([[1,2,3,4], [4,5,6,7]]) #array of two different arrays
print(c[0,1])

d=np.array([[[1,2,3,4], [4,5,6,7]],[[1,2,3,4],[5,6,7,8]]])
print(d[1,1,3])
print(d.shape) 
print(d.size) #total no of elements
print(d.nbytes) #storage taken


np.arange
np.random.permutation
np.reshape

A=np.arange(100)
B=print(np.arange(20,100,2))
C=print(np.random.permutation(np.arange(10)))
print("reshape func")
D=print(np.arange(100).reshape(5,20))

E=np.arange(100)


F=E[3:10]
F[3]=-1200
print(F)
print("gap")
print(E)

F=E[3:10].copy() #now it doesnt affect a, b becomes a separate list

#we need to find the index of -1200
idx=np.argwhere(E==-1200) #array format
index=np.argwhere(E==-1200)[0][0] #normal
print(idx)
print(index)

E[index]=6

G=np.round(10*np.random.rand(5,4))
print(G)
print(G[3,2])
print("accesing entire row",G[1,:])
print("accesing entire column",G[:,1])
print("accessing sub matrix",G[1:3,2:4])#(row:row,column:column)
print(G.T)#transpose   
print(la.inv(np.random.rand(3,3)))
print(G.sort(axis=0))#sorts the columns in size 
print(G.sort(axis=1))#sorts the rows

#Numpy(More indexing)-Masking

#A[index_array]
#A[[1,4,6]] index 1,4,6
#a[a,8] #all values of all elements smaller than 8

#a[a<8 & a>4]       & used when both are arrays, and   used when both sides are single objects, because each array has multiple true and false values
#a[a<8 and  a>4]
#

#slicing gives a view, you will need to externally copy, index array can give you a copy from the start

#advanced indexing
B=print(G[[1,4]])

#masking
C=print(G[G<8])
D=print(G[(G<8) & (G>4)])
'''

#NUMPY BROADCASTING 

#let A be a 2x2 matrix, if i do A=A+5, numpy automatically scales 5 into a 2x2 matrix with all 4 values 5
#it can also duplicate rows or columns
#symmetry must be mantained keeping expansion in mind


np.hstack -concatinating arrays horizontally
np.vstack -concatination arrays vertically
np.sort -
these are called universal functions
these are called vectorized function
'''

M=np.round(10*np.random.rand(3,3))
print(M)
print(M+3)
B=np.round(10*np.random.rand(3,2))
C=np.hstack((M,B)) #give it in a tuple
print(C)


