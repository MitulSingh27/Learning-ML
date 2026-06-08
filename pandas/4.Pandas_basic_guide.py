import pandas as pd
data={
    "name":["A","B","C","D","E"],
    "marks":[90,79,87,93,100]
}
attendence={
    "name": ["A", "B", "C", "D", "E"],
    "attendance": [85, 90, 78, 92, 88]
}
dfa=pd.DataFrame(attendence)
df=pd.DataFrame(data)
print(df)
print(df["marks"])
print(df[df["marks"]>80])
df["grade"]=["A","B","A","C","C"]
print(df.sort_values("marks",ascending=False))
print(df.groupby("grade")['marks'].mean())
df.loc[df["marks"]>50,"marks"]=0
print(df)
print(pd.merge(df,dfa,on='name'))

#how to sort data   
# 1. Clean column names
# 2. Handle missing values
# 3. Convert datatypes
# 4. Filter rows
# 5. Create new features

#Instead of thinking in functions, think in actions:

#Goal	                What you use
#Clean text	            .str, .replace, .strip

#Handle missing	        .isna(), .fillna()

#Filter data	        .loc[], .query()

#Transform columns	    .apply(), .map()

#Combine data	        .merge(), .concat()

#Group logic	        .groupby()

#Sort	                .sort_values()