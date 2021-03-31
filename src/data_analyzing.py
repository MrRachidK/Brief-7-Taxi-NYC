# Import of all the libraries we need to analyze the data
import pandas as pd
import math
import sys

sys.path.insert(0, "/home/apprenant/Documents/Brief-7-Taxi-NYC")
sys.path.insert(0, "/home/apprenant/Documents/Brief-7-Taxi-NYC")

import src.separator as sp
import src.distance_calculation as dc

### 1 - Import and informations provided by the database ###

# Import of the databases
taxi_analyze = pd.read_csv('data/01_raw/train.csv')

# Some infos about the database (columns and shape of database)
print('Nous étudions une base de données de {} lignes et de {} colonnes.'.format(taxi_analyze.shape[0], taxi_analyze.shape[1]))
sp.separator()
print('Voici la liste des colonnes de notre base de données : {}'.format(taxi_analyze.columns.tolist()))
sp.separator()

# Display of the five first entries of the database
print(taxi_analyze.head())
sp.separator()

# Some comments about the database :
# - Id type is object whereas vendor_id type is int
# - Columns pickup_datetime and dropoff_datetime are stored as objects which must be converted to DateTime
# - Column store_and_fwd_flag is stored as object

### 2 - Let's check the columns ###

# Check if there are missing values in the columns

for i in taxi_analyze.columns.tolist():
    part_missing_values = (taxi_analyze[i].isnull().sum() / taxi_analyze.shape[0]) * 100
    print('Dans la colonne {}, nous avons {} % de valeurs manquantes'.format(i, part_missing_values))
sp.separator()

# Adding of a column which indicates the distance between the two geographic points of the entry

taxi_analyze['Distance'] = taxi_analyze.apply(lambda x: dc.calculate_distance_with_coordinates(x, 'pickup_latitude', 'pickup_longitude', 'dropoff_latitude','dropoff_longitude'), axis=1)

# Adding of a column which calculates the trip duration in hours

try:
    taxi_analyze['trip_duration_hours'] = taxi_analyze['trip_duration'].apply(lambda x : round(x / 3600, ndigits=4))
except KeyError:
    print('No KeyError')

# try: 
#     taxi_analyze_test['trip_duration_hours'] = taxi_analyze_test['trip_duration'].apply(lambda x : x / 3600)
# except KeyError:
#     print('No KeyError')

### 3 - Let's check the duplicated entries ###

print(taxi_analyze.duplicated().value_counts()) # Output : 'False 10000', so there are no perfect duplicated entries
print(taxi_analyze.id.duplicated().value_counts()) # Output : 'False 10000', so there are no duplicated entries
sp.separator()

### 4 - Let's check the missing values ###

# We checked previously that there are no missing values in each column, so we can move on to the next step

### 5 - Let's analyze the types of our datas

# Display of all the types of each variable
print(taxi_analyze.dtypes)
sp.separator()

# Conversion of the pickup_datetime and dropoff_datetime columns into datetime data type
taxi_analyze['pickup_datetime'] = pd.to_datetime(taxi_analyze['pickup_datetime'])
taxi_analyze['dropoff_datetime'] = pd.to_datetime(taxi_analyze['dropoff_datetime'])
print(taxi_analyze.dtypes)

### 6 - Let's analyze the relevance of our database ###

# Let's check the unique values of some columns

print(sorted(taxi_analyze['vendor_id'].unique()))
sp.separator()
print(sorted(taxi_analyze['passenger_count'].unique()))
sp.separator()
print(sorted(taxi_analyze['store_and_fwd_flag'].unique()))
sp.separator()


modified_taxi_trips_train = taxi_analyze.to_csv('/home/apprenant/Documents/Brief-7-Taxi-NYC/data/02_intermediate/modified_train.csv')
