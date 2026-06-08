import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,3,4,5])
y=np.array([2,4,6,8,10])

#LINE PLOT
plt.plot(x,y)   #draws the line
plt.show()      #displays the line

#SCATTER PLOT   #use this for actual vs predicted
plt.scatter(x,y)
plt.show()

#CUSTOMIZING
plt.plot(x,y,   color='red', linestyle='--',marker='o')
plt.title("First graph")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid(True)
plt.show()

#FIGURES AND AXES
#these methods usually used for more control
#figure  - full sheet of paper, contains all graphs,titles,subplots,etc
#Axes    - Individual graph area, where the actual data is plotted
#Axis    - X/Y measuring lines
#plot    - The actual plot

#creating a figure
fig=plt.figure()
plt.title("empty figure")
plt.show

#creating figure and axes together
fig, ax=plt.subplots()#standard way of creating plots, creates one figure,one axes
plt.title("figure and axes")
plt.show()

#plotting on axes

x=[1,2,3,4]
y=[10,20,25,30]
fig,ax=plt.subplots()
ax.plot(x,y)
plt.show()

#one figure can have many axes
import matplotlib.pyplot as plt

fig, ax = plt.subplots(2,2) #creates 4 plots in one figure

ax[0,0].plot([1,2,3],[1,4,9])
ax[0,1].plot([1,2,3],[1,2,3])
ax[1,0].plot([1,2,3],[9,4,1])
ax[1,1].plot([1,2,3],[3,2,1])

plt.show()

#REAL ML EXAMPLE
import matplotlib.pyplot as plt

epochs = [1,2,3,4,5]
loss = [0.9,0.7,0.5,0.35,0.2]

fig, ax = plt.subplots(figsize=(8,5))

ax.plot(epochs, loss)

ax.set_title("Training Loss")
ax.set_xlabel("Epoch")
ax.set_ylabel("Loss")

ax.grid(True)

plt.show()  


