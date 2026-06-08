import pandas as pd

#1 Multi indexing-hierarchical indexing
data=[
    ["India","Delhi",30],
    ["India","Mumbai",30],
    ["USA","NYC",25]
]
df=pd.DataFrame(data,columns=["Country","city","temp"])
df=df.set_index(["Country","city"])
print(df)   #basically, multiple indexes
print(df.loc["India"],
df.loc[("India","Delhi")]) #accessing the elements

#2 pivot tables
df = pd.DataFrame({
    "name": ["A", "B", "A", "B", "A"],
    "subject": ["Math", "Math", "Science", "Science", "Math"],
    "marks": [90, 80, 85, 70, 95]
})
pivot=df.pivot_table(
    values="marks",
    index="name",
    columns="subject",
    aggfunc="mean"
)
print(pivot) #presents data in a clean format

#3 time series
df=pd.DataFrame({
    "date":pd.date_range(start="2024-01-01",periods=5),     #creates a sequence of data
    "sales":[100,200,300,400,500]
})
df.set_index("date",inplace=True)       #sets date as index
df.resample("d").mean()                 #can be used to change bw daily,monthly,yearly etc etc
print(df.index.year,df.index.month)     #extracting only the year part, or only the month part 
#you can also extract day,weekday,day_name(),hour using the same syntax, day_name() is the only one with () brackets


df = pd.DataFrame({
    "name": ["A", "B", "A", "B", "A"],
    "subject": ["Math", "Math", "Science", "Science", "Math"],
    "marks": [90, 80, 85, 70, 95]
})
#apply vs map vs applymap
#map-only one column
#apply- flexible, row or column
#applymap-each element throughout the entire df

#map-only one column
print(df["marks"].apply(lambda x:x+2)) #this adds +2 to only one column, the marks column

#apply- flexible, row or column
print(df.apply(lambda col:col.nunique()))    #prints number of unique values, takes each column as a whole and applies function
print(df.apply(lambda row:row["marks"]+2,axis=1))#takes each row, accesses multiple columns if needed

#applymap
print(df[["marks"]].applymap(lambda x:x+2)) #goes cell by cell and applies the function

#Window functions
sales = [100, 200, 300, 400]
df=pd.DataFrame(sales,columns=["sales"])
#rolling/sliding windows
print(df["sales"].rolling(window=2).mean())     #window size=2, take cxurrent and previous value, this smoothens data(removes noise), fixed window size
#what happened recently

#expanding window
print(df["sales"].expanding().mean())           #take everything from the start, till now, increasing window size, used for long term trends
#what has happened till now

#MERGE vs JOIN vs CONCAT
df1 = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["A", "B", "C"]
})

df2 = pd.DataFrame({
    "id": [1, 2, 4],
    "marks": [90, 80, 70]
})

#Use merge when:
#“Match rows based on a column (SQL mindset)”
pd.merge(df1,df2,on='id')

#Use join when:
#“Match rows based on index”
df1.join(df2)

#Use concat when:
#“Just stack data (no matching logic)”
pd.concat([df1,df2])

#Advanced cleaning 
#renaming columnns
df.rename(columns={"old":"new"})
#change type
df["age"]=df["age"].astype(int)
#string ops
df["name"].str.upper()
df["name"].str.contains("A")

#creating a pipeline
df=(   
    df.dropna()
      .assign(new_marks=lambda x:x["marks"]*2)
      .query("marks >50")
)