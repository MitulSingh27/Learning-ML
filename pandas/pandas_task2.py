import pandas as pd
data = {
    "Name": ["Alice ", "bob", "CHARLIE", None, "David"],
    "Age": ["25", "30", None, "22", "twenty"],
    "Salary": ["50000", "60000", "not available", "45000", "70000"],
    "Department": ["HR", "tech", "Tech", "hr", None]
}

df = pd.DataFrame(data)
#cleant text
df['Name']=df["Name"].str.title()
df['Department']=df['Department'].str.lower()
print(df)
#Handle missing values
df=df.dropna(subset=['Name'])
df["Department"]=df["Department"].fillna('unkown')
print(df)
#fix datatypes
df['Salary']=pd.to_numeric(df["Salary"],errors="coerce")
df['Age']=pd.to_numeric(df["Age"],errors="coerce")
#feature engineering
df['Salary_After_Tax']=df['Salary']*0.9
print(df)


