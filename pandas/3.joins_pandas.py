import pandas as pd 
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

#basic join
df = pd.merge(df_orders, df_customers, on='customer_id')
print(df)
#only matching customer id are kept, custid=5 is removed 

#left join 
df = pd.merge(df_orders, df_customers, on='customer_id', how='left')
print(df)
#left table is completely intact and kept, missing values filled with NaN
#customer id 5 stays, name and city are nan

#right join
df = pd.merge(df_orders, df_customers, on='customer_id', how='right')
#right table is completely intact and kept, missing values filled with NaN

#outer join
df = pd.merge(df_orders, df_customers, on='customer_id', how='outer')
#keeps everything from both tables 

#can merge on different column names
pd.merge(df_customers,df_orders,left_on='id1',right_on='id2')