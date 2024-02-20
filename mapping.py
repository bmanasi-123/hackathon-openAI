import pandas as pd
import re

# read the source and sample csv
source = pd.read_csv('source.csv')
sample = pd.read_csv('sample.csv')

# create an empty dataframe with columns similar to the sample
target = pd.DataFrame(columns=sample.columns)

# copy over data where the column names match exactly
for col in source.columns:
    if col in target.columns:
        target[col] = source[col]

# Map source column names to sample column names based on the content
target['ID'] = source['PatientID']
target['Full Name'] = source['FirstName'] + ' ' + source['LastName']
target['DOB'] = pd.to_datetime(source['DateOfBirth'], format='%d-%m-%Y').dt.strftime('%Y-%m-%d')

# apply transformations
target['Mobile'] = source['Phone'].apply(lambda x: re.sub(r'\D', '', x)).apply(lambda x: '{}-{}-{}'.format(x[0:3], x[3:6], x[6:]))
target['Email'] = source['Email']

# save the transformed dataframe to csv
target.to_csv('target.csv', index = False)