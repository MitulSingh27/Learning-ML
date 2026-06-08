import pandas as pd

#Core data structures

# Series (1D)- single column
print(pd.Series([10,20,30],index=['a','b','c']), #with index
      pd.Series([10,20,30]))                   #without index

#DataFrame (2D)- Table(Rows+Columns)
data={
    "name":["A","B","C"],
    "age":[20,25,30]
    }
print(pd.DataFrame(data))

#importing data
#df=pd.read_csv("")  #filename.csv
#df=pd.read_excel("")#filename.xlsx

data = {
    "Name": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "Age": [21, 22, 23, 24, 25, 26, 27, 28],
    "Salary": [30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000],
    "Department": ["HR", "IT", "IT", "Finance", "HR", "Finance", "IT", "HR"]
}

df = pd.DataFrame(data)
print(df)               #Full dataframe
print(df.head())        #First 5 rows
print(df.head(3))       #First 3 rows
print(df.tail())        #Last 5  
print(df.tail(2))       #Last 2 rows
print(df.describe())    #Statistics loke mean,count,std deviation,min,man,etc etc


#Selecting Data
print(df["Age"])            #Columns
print(df[["Name","Age"]])   #Multiple columns
print(df.iloc[0])           #Rows, by index
print(df.loc[0])            #Rows, by location

#Condition Filtering
print(df[df['Age']>20])     #Give me only the rows there condition is true
print(df[(df['Age']>20)&(df["Salary"]>35000)])    #multiple conditions- give me the rows where both conditions are true

#Modifying Data
df["City"]=['blr','mumbai','delhi','blr','mumbai','delhi','blr','mumbai'] #add column
df.loc[0,"Age"]=50                              #update value as 50 on 0th row in age column
df["Age"]=df["Age"].apply(lambda x:x+1)        #Take this function, and apply it to everything in this column.
print(df)

#Data cleaning
data = {
    "Name": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "Age": [21, 22,None, 24, 25, None, 27, 28],
    "Salary": [30000, 35000, 40000, None, 50000, 55000, None, 65000],
    "Department": ["HR", "IT", "IT", "Finance", None, "Finance", "IT", "HR"]
}   
df = pd.DataFrame(data)
print(df.isnull())                  #Returns True if value is missing--> (na/NONE)
print(df.isnull().sum())            #Counts how many Missing Null values are present
print(df.dropna())                  #drops rows with ANY missing value
print(df.dropna(how="all"))         #drops rows only if all values are missing
print(df.dropna(subset=["Age"]))    #drops rows based on null values in subset chosen column
print(df.fillna(0))                #Replaces all missing values with 0
print(df.fillna('anythinghere')) 
print(df["Age"].fillna(df["Age"].mean())) #fills all gaps in age with mean value
#different values per column
print(df.fillna({
    'Age':df["Age"].mean(),
    "Salary":0,
    "Department":"unkown"
}))
df.drop_duplicates()                #Removes Duplicates

#Sorting
print(df.sort_values("Age"),                #sorts ascending acc to age
df.sort_values("Salary",ascending=False))   #sorts descending acc to salary

#Group by- split the data into groups,apply a function, and combine it into a new table
df = pd.DataFrame({
    "department": ["IT", "HR", "IT", "HR", "Finance"],
    "salary": [50000, 40000, 60000, 45000, 70000],
    "age": [25, 30, 28, 35, 40]
})

print(df.groupby("department")['salary'].mean())    #Groups elements, and does things, and makes a new table
print(df.groupby("department")['salary'].agg(['mean','max','min'])) #multiple things on diff grps
print(df.groupby("department").agg({
    "salary":"mean",
    "age":"max"
}))

#Merging
#pd.merge(df1, df2, on="id") using id, merge dataframe1 and dataframe2

#indexing
#df.set_index() #sets whatever u want as the index, instead of 0,1,2,3
#df.resample()  #resets index

#plotting
