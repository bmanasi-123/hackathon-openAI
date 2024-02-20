import pandas as pd

# read source and sample files
source_df = pd.read_csv('dumbscmap.csv')
print(source_df)
sample_df = pd.read_csv('sample1.csv')

# create target dataframe
target_df = pd.DataFrame()

# ID column
target_df['id'] = source_df['id']

# Full Name column
target_df['full_name'] = source_df['first_name'] + ' ' + source_df['last_name']

# Birthdate column
target_df['birthdate'] = pd.to_datetime(source_df['birthdate'], format='%m/%d/%Y').dt.strftime('%m/%d/%Y')

# Gender column
target_df['gender'] = source_df['gender'].map({'Male': 'M', 'Female': 'F'})

# Race column
target_df['race'] = source_df['race']

# Department column
target_df['department'] = source_df['department']

# Job Title column
target_df['jobtitle'] = source_df['jobtitle']

# Location column
target_df['location'] = source_df['location']

# Hire Date column
target_df['hire_date'] = pd.to_datetime(source_df['hire_date'], format='%m/%d/%Y').dt.strftime('%m/%d/%Y')

# Term Date column
target_df['termdate'] = pd.to_datetime(source_df['termdate']).dt.strftime('%Y-%m-%d %H:%M:%S UTC')

# Location City column
target_df['location_city'] = source_df['location_city']

# Location State column
target_df['location_state'] = source_df['location_state']

# save target to csv
target_df.to_csv('target.csv', index=False)