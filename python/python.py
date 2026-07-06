"""filename=open("filename.txt","mode")
text files-.txt

r-read
w-write
a-append

filename.write("text here")
filename.read() - reads the entire file  big string
filename.readlines()- each single line is a different element in a list  list of strings
filename.readline()- reads one singlular line one small string
"""

file=open("drishti.txt","w")
n=input("enter text:")
file.write(n)
file.close()

#to read a file and print

file=open("drishti.txt","r")
s=file.read()
l=s.split()
print(l)
file.close()
#
file=open("drishti.txt","r")
s=file.readlines()
print(s)
file.close()




"""
huge
ass
text
"""