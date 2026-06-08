import pandas as pd
data = {
    "name": ["A", "B", "A", "B", "A"],
    "subject": ["Math", "Math", "Science", "Science", "Math"],
    "marks": [90, 80, 85, 70, 95],
    "prev_marks":[90, 80, 85, 70, 95],
    "date": ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05"]
}
df=pd.DataFrame(data)
print(df)
print(df.sort_values("date",ascending=True))
print(df["marks"].rolling(window=2).mean())
df["prev_marks"]=df["marks"].shift(1)
print(df)
pivot=df.pivot_table(
    values="marks",
    index="name",
    columns='subject',
    aggfunc="mean"
)
print(df.groupby("subject")["marks"].mean().max())

df=(
    df.dropna(),
    df.query("marks>50"),
    df.describe()
)
print(df)


