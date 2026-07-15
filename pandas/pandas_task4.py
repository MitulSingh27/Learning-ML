import pandas as pd

data = {
    "order_id": [101, 102, 103, 104, 105, 106],
    "customer": ["Alice", "Bob", "alice", "David", None, "Bob"],
    "order_date": ["2024-01-01", "2024/01/02", "01-01-2024", "2024-01-04", "2024-01-05", "2024-01-02"],
    "amount": ["500", "1500", "500", "2000", "3000", "1500"],
    "status": ["Delivered", "delivered", "Pending", "Cancelled", "Delivered", None]
}

df = pd.DataFrame(data)
df['customer']=df['customer'].str.strip().str.title()
df['status']=df['status'].str.lower()

df=df.dropna(subset=['customer'])
df['status']=df['status'].fillna('unknown')

df['amount']=pd.to_numeric(df['amount'],errors="coerce")
df['order_date']=pd.to_datetime(df['order_date'],errors='coerce')

df=df.drop_duplicates()

#df['order_type']=df['amount']>=1500 wrong
df['order_type']=df['amount'].apply(lambda x:'high' if x>1500 else 'low')

df=df.sort_values("amount")
print(df[df['status']=='delivered'])
print(df.groupby('customer')['amount'].sum())
print(df)
