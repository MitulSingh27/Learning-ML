import pandas as pd
data = {
    "customer": ["Alice", "Bob", "alice", "Charlie", "Bob", None],
    "date": ["2024-01-01", "01/02/2024", "2024/01/01", "2024-03-01", "01-02-2024", "2024-04-01"],
    "amount": ["1000", "2000", "1000", "not available", "2000", "3000"],
    "city": ["NY", "la", "NY", "Chicago", "LA", None]
}

df = pd.DataFrame(data)
#clean text
df['customer']=df['customer'].str.strip().str.title()
df['city']=df['city'].str.strip().str.lower()
#handle missing values
df=df.dropna(subset='customer')
df['city']=df['city'].fillna('unknown')
#fix datatype
df['amount']=pd.to_numeric(df['amount'],errors='coerce') 
df['date']=pd.to_timedelta(df["date"],errors="coerce")
df=df.drop_duplicates()
#feature engineering
df['high_value']=df['amount']>1500
#Group by
print(df.groupby('customer')['amount'].mean())
print(df)
