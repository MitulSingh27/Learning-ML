import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#step 1- load the dataset
df=pd.read_csv('housing.csv')

#step 2- first look
print(df.head())
print(df.tail())
print(df.sample(5))
'''
identify whats the target
what does one row represent
'''
#step 3- shape
print(df.shape)

#step 4- column names
print(df.columns)

#step 5- info
print(df.info())
'''
gives datatypes, columns, number of null values, etc
'''

#step 6- missing values
print(df.isnull().sum())

#step 7- duplicates
print(df.duplicated().sum())
#if they exist
#df.drop_duplicates()

#step 8- summary statistics
print(df.describe())

#step 9- categorical columns
print(df['ocean_proximity'].value_counts())
print(df['ocean_proximity'].unique())
print(df['ocean_proximity'].nunique())


#output-
'''
   longitude  latitude  housing_median_age  total_rooms  total_bedrooms  population  households  median_income  median_house_value ocean_proximity

0    -122.23     37.88                41.0        880.0           129.0       322.0       126.0         8.3252            452600.0        NEAR BAY

1    -122.22     37.86                21.0       7099.0          1106.0      2401.0      1138.0         8.3014            358500.0        NEAR BAY

2    -122.24     37.85                52.0       1467.0           190.0       496.0       177.0         7.2574            352100.0        NEAR BAY

3    -122.25     37.85                52.0       1274.0           235.0       558.0       219.0         5.6431            341300.0        NEAR BAY

4    -122.25     37.85                52.0       1627.0           280.0       565.0       259.0         3.8462            342200.0        NEAR BAY

       longitude  latitude  housing_median_age  total_rooms  total_bedrooms  population  households  median_income  median_house_value ocean_proximity

20635    -121.09     39.48                25.0       1665.0           374.0       845.0       330.0         1.5603             78100.0          INLAND

20636    -121.21     39.49                18.0        697.0           150.0       356.0       114.0         2.5568             77100.0          INLAND

20637    -121.22     39.43                17.0       2254.0           485.0      1007.0       433.0         1.7000             92300.0          INLAND

20638    -121.32     39.43                18.0       1860.0           409.0       741.0       349.0         1.8672             84700.0          INLAND

20639    -121.24     39.37                16.0       2785.0           616.0      1387.0       530.0         2.3886             89400.0          INLAND

       longitude  latitude  housing_median_age  total_rooms  total_bedrooms  population  households  median_income  median_house_value ocean_proximity

2306     -119.77     36.83                16.0       2360.0           355.0      1034.0       359.0         5.0635            108500.0          INLAND

13160    -121.40     36.84                40.0       2352.0           536.0      1430.0       535.0         3.0912            155300.0          INLAND

7436     -118.19     33.94                45.0       1871.0           371.0      1315.0       382.0         3.3661            160800.0       <1H OCEAN

1697     -122.26     38.00                 5.0       6265.0           908.0      3326.0       872.0         6.2073            272900.0        NEAR BAY

3218     -119.68     36.32                26.0        592.0           121.0       268.0       116.0         1.7596            120800.0          INLAND

(20640, 10)

Index(['longitude', 'latitude', 'housing_median_age', 'total_rooms',

       'total_bedrooms', 'population', 'households', 'median_income',

       'median_house_value', 'ocean_proximity'],

      dtype='object')

<class 'pandas.core.frame.DataFrame'>

RangeIndex: 20640 entries, 0 to 20639

Data columns (total 10 columns):

 #   Column              Non-Null Count  Dtype  

---  ------              --------------  -----  

 0   longitude           20640 non-null  float64

 1   latitude            20640 non-null  float64

 2   housing_median_age  20640 non-null  float64

 3   total_rooms         20640 non-null  float64

 4   total_bedrooms      20433 non-null  float64

 5   population          20640 non-null  float64

 6   households          20640 non-null  float64

 7   median_income       20640 non-null  float64

 8   median_house_value  20640 non-null  float64

 9   ocean_proximity     20640 non-null  object 

dtypes: float64(9), object(1)

memory usage: 1.6+ MB

None

longitude               0

latitude                0

housing_median_age      0

total_rooms             0

total_bedrooms        207

population              0

households              0

median_income           0

median_house_value      0

ocean_proximity         0

dtype: int64

0

          longitude      latitude  housing_median_age   total_rooms  total_bedrooms    population    households  median_income  median_house_value

count  20640.000000  20640.000000        20640.000000  20640.000000    20433.000000  20640.000000  20640.000000   20640.000000        20640.000000

mean    -119.569704     35.631861           28.639486   2635.763081      537.870553   1425.476744    499.539680       3.870671       206855.816909

std        2.003532      2.135952           12.585558   2181.615252      421.385070   1132.462122    382.329753       1.899822       115395.615874

min     -124.350000     32.540000            1.000000      2.000000        1.000000      3.000000      1.000000       0.499900        14999.000000

25%     -121.800000     33.930000           18.000000   1447.750000      296.000000    787.000000    280.000000       2.563400       119600.000000

50%     -118.490000     34.260000           29.000000   2127.000000      435.000000   1166.000000    409.000000       3.534800       179700.000000

75%     -118.010000     37.710000           37.000000   3148.000000      647.000000   1725.000000    605.000000       4.743250       264725.000000

max     -114.310000     41.950000           52.000000  39320.000000     6445.000000  35682.000000   6082.000000      15.000100       500001.000000

ocean_proximity

<1H OCEAN     9136

INLAND        6551

NEAR OCEAN    2658

NEAR BAY      2290

ISLAND           5

Name: count, dtype: int64

['NEAR BAY' '<1H OCEAN' 'INLAND' 'NEAR OCEAN' 'ISLAND']

5
'''

