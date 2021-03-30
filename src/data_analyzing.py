# Import of all the libraries we need to analyze the data
import pandas as pd

### 1 - Import and informations provided by the database ###

# Import of the database
taxi_analyze = pd.read_csv('data/01_raw/train.csv').sample(n=10000)

# Some infos about the database (columns and shape of database)
print('Nous étudions une base de données de {} lignes et de {} colonnes.'.format(taxi_analyze.shape[0], taxi_analyze.shape[1]))
print('---------------------------')
print('Voici la liste des colonnes de notre base de données : {}'.format(taxi_analyze.columns.tolist()))
print('---------------------------')

# Display of the five first entries of the database
print(taxi_analyze.head())
print('---------------------------')

# Some comments about the database :
# - Id type is object whereas vendor_id type is int
# - Columns pickup_datetime and dropoff_datetime are stored as objects which must be converted to DateTime
# - Column store_and_fwd_flag is stored as object

### 2 - Let's check the columns ###

# Check if there are missing values in the columns

for i in taxi_analyze.columns.tolist():
    part_missing_values = (taxi_analyze[i].isnull().sum() / taxi_analyze.shape[0]) * 100
    print('Dans la colonne {}, nous avons {} % de valeurs manquantes'.format(i, part_missing_values))
print('---------------------------')

### 3 - Let's check the duplicated entries ###

print(taxi_analyze.duplicated().value_counts()) # Output : 'False 10000', so there are no perfect duplicated entries
print(taxi_analyze.id.duplicated().value_counts()) # Output : 'False 10000', so there are no duplicated entries
print('---------------------------')
### 4 - Let's check the missing values ###

# We checked previously that there are no missing values in each column, so we can move on to the next step

### 5 - Let's analyze the types of our datas

# Display of all the types of each variable
print(taxi_analyze.dtypes)
print('---------------------------')

# Conversion of the pickup_datetime and dropoff_datetime columns into datetime data type
taxi_analyze['pickup_datetime']=pd.to_datetime(taxi_analyze['pickup_datetime'])
taxi_analyze['dropoff_datetime']=pd.to_datetime(taxi_analyze['dropoff_datetime'])

### 6 - Let's analyze the relevance of our database ###

# Let's check the unique values of some columns

print(sorted(taxi_analyze['vendor_id'].unique()))
print('---------------------------')
print(sorted(taxi_analyze['passenger_count'].unique()))
print('---------------------------')
print(sorted(taxi_analyze['store_and_fwd_flag'].unique()))




# sampled_taxi_trips = taxi_analyze.to_csv('/home/apprenant/Documents/Brief-7-Taxi-NYC/data/02_intermediate/sampled_train.csv')
