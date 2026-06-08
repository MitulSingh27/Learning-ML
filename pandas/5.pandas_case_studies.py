import pandas as pd

'''data = {
    "Name": ["Alice ", "bob", "CHARLIE", None, "David"],
    "Age": ["25", "30", None, "22", "twenty"],
    "Salary": ["50000", "60000", "not available", "45000", "70000"],
    "Department": ["HR", "tech", "Tech", "hr", None]
}

df = pd.DataFrame(data)
#clean text
df['Name']=df["Name"].str.title()
df['Department']=df['Department'].str.lower()
print(df)
#Handle missing values
df.dropna(subset=['Name'])
#i dont know how to fill missing department with 'unkown'
print(df)
#fix datatypes
df['salary']=df['salary'].astype(int)

#correct answers
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
print(df.groupby('customer')('amount').mean())
print(df)

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



data = {
    "product": ["Laptop", "laptop", "Phone", "Tablet", "Phone", None],
    "category": ["Electronics", "electronics", "Electronics", "Gadgets", "electronics", "Electronics"],
    "price": ["50000", "50000", "20000", "15000", "20000", "30000"],
    "quantity": [1, 1, 2, 1, 2, 1],
    "returned": ["No", "no", "Yes", "No", "yes", "No"]
}

df = pd.DataFrame(data)

#clean text
df['product']=df["product"].str.strip().str.title()
df['category']=df["category"].str.strip().str.lower()
df['returned']=df["returned"].str.strip().str.lower()
#dropping missing values
df=df.dropna(subset=['product'])
#fixing datatypes
df['price']=pd.to_numeric(df['price'],errors='coerce')
#dropping duplicates
df=df.drop_duplicates()
df['revenue']=df['price']*df['quantity']
df['valid_sales']=df['returned'].apply(lambda x: 'invalid' if 'returned'== 'yes' else 'valid')
df=df[df['valid_sales']=='valid']
print(df.groupby('product')['revenue'].sum().sort_values('revenue',ascending=False))



customers = {
    "customer_id": [1, 2, 3, 4],
    "name": ["Alice", "Bob", "Charlie", "David"],
    "city": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df_customers = pd.DataFrame(customers)

orders = {
    "order_id": [101, 102, 103, 104, 105],
    "customer_id": [1, 2, 1, 3, 5],  # notice: 5 doesn't exist in customers
    "amount": ["1000", "2000", "1500", "3000", "2500"],
    "status": ["delivered", "pending", "delivered", "delivered", "cancelled"]
}

df_orders = pd.DataFrame(orders)

df_orders['amount']=pd.to_numeric(df_orders['amount'],errors='coerce')
# merge the data, keep orders table
df=pd.merge(df_orders,df_customers,on="customer_id",how='left')
#filter delivered orders
df = df[df['status'] == 'delivered']
print(df)
#grouping and sorting
result = df.groupby('name')['amount'].sum().sort_values(ascending=False)
print(result)
'''
customers = {
    "customer_id": [1, 2, 3, 4],
    "name": ["Alice", "Bob", "Charlie", "David"],
    "city": ["New York", "Los Angeles", "Chicago", "Houston"]
}
orders = {
    "order_id": [101, 102, 103, 104, 105],
    "customer_id": [1, 2, 1, 3, 5],  # 5 is invalid
    "amount": ["1000", "2000", "1500", "3000", "2500"],
    "status": ["delivered", "pending", "delivered", "delivered", "cancelled"]
}
payments = {
    "order_id": [101, 102, 103, 106],  # 106 doesn't exist in orders
    "payment_method": ["card", "cash", "card", "upi"],
    "payment_status": ["paid", "failed", "paid", "paid"]
}
df_payments = pd.DataFrame(payments)
df_customers = pd.DataFrame(customers)
df_orders = pd.DataFrame(orders)


#merge
df_join1=pd.merge(df_orders,df_customers,on='customer_id',how='left')
df=pd.merge(df_join1,df_payments,on='order_id',how='left')
print(df)
#convert datatype
df['amount']=pd.to_numeric(df['amount'],errors='coerce')
#filling missing values and data
df['name']=df["name"].fillna('unknown')
df['payment_status']=df["payment_status"].fillna('unpaid')
df['revenue']=df['amount']
print(df.groupby('revenue')['name'].sum().sort_values(ascending=False))

