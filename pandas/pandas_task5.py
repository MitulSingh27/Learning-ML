import pandas as pd

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


