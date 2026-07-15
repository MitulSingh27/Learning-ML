import pandas as pd
'''
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

