import pandas as pd
import langchain as lc

# Load the dataset
data = pd.read_csv('sample1.csv')
print(data)

# 1. Get the number of rows in the table
num_rows = lc.count(data)

# 2. Get the column names and datatypes
column_names = lc.get_column_names(data)
column_datatypes = lc.get_column_datatypes(data)

# 3. Display a few lines of the table
lc.head(data)

# 4. Determine the count of null values and empty row values
null_count = lc.count_null_values(data)
empty_row_count = lc.count_empty_rows(data)

# 5. Perform analysis based on data types
numeric_columns = lc.get_numeric_columns(data)
string_columns = lc.get_string_columns(data)

# For numeric data
max_values = lc.get_max_values(data, numeric_columns)
min_values = lc.get_min_values(data, numeric_columns)
# For string columns
unique_value_counts = lc.get_unique_value_counts(data, string_columns)
lc.plot_bar(unique_value_counts)

# 6. Write a paragraph about the dataset
paragraph = "When visualizing the data, the first thing that comes to mind is that it contains multiple columns with different types of data. The dataset seems to be related to a specific field or area, though it is not explicitly mentioned. Based on the data, it appears that the dataset could have been collected from a survey or data collection process. An overview of the data indicates that it contains information about various attributes and their corresponding values. The analysis performed on the data helps in understanding the distribution and characteristics of the data, making the work easier for further analysis."

print(paragraph)