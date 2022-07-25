import camelot 
from IPython.display import display
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
import sqlite3


# Initiating the database
engine =\
    create_engine('sqlite:///csu_enrollment_by_ethnic_origin_17_21.db',\
        echo=False)


# Peeling from the pdf
pdf =\
    camelot.read_pdf('../csu_enrollment_by_ethnic_origin_17_21.pdf',\
        pages='1')


# Taking what was peeled from the pdf and placing its first object
# into a datafame
df = pd.DataFrame(pdf[0].df)


# Dropping unnecessary rows
df.drop([0, 1], inplace=True)


# Reindexing
df.index = np.arange(0, df.shape[0])


# Assigning new column names to avoid duplicate axes
df.rename(columns={0: 'zero', 1: 'one', 2: 'two', 3: 'three'}, inplace=True)


# Removing all of the line break characters
df = df.apply(lambda x: x.str.split('\n'))


# The dataframe 'df' is partitioned into its respective columns
df_zero_raw = df['zero']
df_one_raw = df['one']
df_two_raw = df['two']
df_three_raw = df['three']


# Partitioning 'zero' column into 
# 'Undergraduate', 'Graduate', 'Combine' lists
df_zero_raw_undergraduate = df_zero_raw[0]
df_zero_raw_graduate = df_zero_raw[1]
df_zero_raw_combined = df_zero_raw[2]


# Removing the partition name 
# ('Undergraduate', 'Graduate', 'Combine') from each list

# Undergraduate
df_zero_undergraduate = df_zero_raw_undergraduate
del df_zero_undergraduate[0]

# Graduate
df_zero_graduate = df_zero_raw_graduate
del df_zero_graduate[0]

# Combined
df_zero_combined = df_zero_raw_combined
del df_zero_combined[0]


# Changing all row values in 'Undergraduate', 'Graduate', 'Combine' lists
# to lowercase
for i in range(10):
    df_zero_undergraduate[i] =\
        df_zero_undergraduate[i].lower().replace(' ', '_').replace('-', '_')
    df_zero_graduate[i] =\
        df_zero_graduate[i].lower().replace(' ', '_').replace('-', '_')
    df_zero_combined[i] =\
        df_zero_combined[i].lower().replace(' ', '_').replace('-', '_')
    
    
# Partitioning 'one' column into year 
# '2017', '2018', '2019', '2020', '2021' per 
# 'Undergraduate', 'Graduate', 'Combine' lists

# Undergraduate by year
df_one_undergraduate_17 = df_one_raw.loc[0][0:50:5]
df_one_undergraduate_18 = df_one_raw.loc[0][1:50:5]
df_one_undergraduate_19 = df_one_raw.loc[0][2:50:5]
df_one_undergraduate_20 = df_one_raw.loc[0][3:50:5]
df_one_undergraduate_21 = df_one_raw.loc[0][4:50:5]

# Graduate by year
df_one_graduate_17 = df_one_raw.loc[1][0:50:5]
df_one_graduate_18 = df_one_raw.loc[1][1:50:5]
df_one_graduate_19 = df_one_raw.loc[1][2:50:5]
df_one_graduate_20 = df_one_raw.loc[1][3:50:5]
df_one_graduate_21 = df_one_raw.loc[1][4:50:5]

# Combined by year
df_one_combined_17 = df_one_raw.loc[2][0:50:5]
df_one_combined_18 = df_one_raw.loc[2][1:50:5]
df_one_combined_19 = df_one_raw.loc[2][2:50:5]
df_one_combined_20 = df_one_raw.loc[2][3:50:5]
df_one_combined_21 = df_one_raw.loc[2][4:50:5]


# Change the 'NA' row value in position 5 of 'Combined'
#year 2017 column to '12'
df_one_combined_17[5] = '12'


# Partitioning 'two' column into 
# 'Undergraduate', 'Graduate', 'Combined' lists
df_two_undergraduate = df_two_raw.loc[0][0:10]
df_two_graduate = df_two_raw.loc[1][0:10]
df_two_combined = df_two_raw.loc[2][0:10] 


# Changing the '' at position 5 in 'Combined' to '-7'
df_two_combined[5] = '3'


# Partitioning 'three' column into 
# 'Undergraduate', 'Graduate', 'Combined' lists
df_three_undergraduate = df_three_raw.loc[0][0:10]
df_three_graduate = df_three_raw.loc[1][0:10]
df_three_combined = df_three_raw.loc[2][0:10] 


# Changing the '' at position 8 in 'Undergraduate' and 'Graduate' to 0.0
df_three_undergraduate[8] = np.nan
df_three_graduate[8] = np.nan


# Changing the '' at positions 5 and 8 in 'Combined' to '-36.8' and 0.0 respectively
df_three_combined[5] = '25.0'
df_three_combined[8] = np.nan


# Creating the dataframes

# Column names
column_names = [
    'student_ethnic_origin',
    'fall_2017',
    'fall_2018',
    'fall_2019',
    'fall_2020',
    'fall_2021',
    '4_year_#_change',
    '4_year_%_change'
    ]


# Undergraduate lists
undergraduate_list_of_lists = [
    df_zero_undergraduate,
    df_one_undergraduate_17,
    df_one_undergraduate_18,
    df_one_undergraduate_19,
    df_one_undergraduate_20,
    df_one_undergraduate_21,
    df_two_undergraduate,
    df_three_undergraduate
    ]

# Undergraduate dataframe
df_undergraduate =\
    pd.DataFrame(list(zip(*undergraduate_list_of_lists)), columns=column_names)


# Graduate lists
graduate_list_of_lists = [
    df_zero_graduate,
    df_one_graduate_17,
    df_one_graduate_18,
    df_one_graduate_19,
    df_one_graduate_20,
    df_one_graduate_21,
    df_two_graduate,
    df_three_graduate
    ]

# Graduate dataframe
df_graduate =\
    pd.DataFrame(list(zip(*graduate_list_of_lists)), columns=column_names)


# Combined lists
combined_list_of_lists = [
    df_zero_combined,
    df_one_combined_17,
    df_one_combined_18,
    df_one_combined_19,
    df_one_combined_20,
    df_one_combined_21,
    df_two_combined,
    df_three_combined
    ]

# Combined dataframe
df_combined =\
    pd.DataFrame(list(zip(*combined_list_of_lists)), columns=column_names)


# Changing each row value in the '4_year_%_change' column,
# for each 'Undergraduate', 'Graduate', and 'Combined' table, to a float
df_undergraduate['4_year_%_change'] =\
    df_undergraduate.iloc[np.r_[0:8, 9:10], 7].replace('\%', '',\
    regex=True).astype(float) 
df_graduate['4_year_%_change'] =\
    df_graduate.iloc[np.r_[0:8, 9:10], 7].replace('\%', '',\
    regex=True).astype(float)
df_combined['4_year_%_change'] =\
    df_combined.iloc[np.r_[0:8, 9:10], 7].replace('\%', '',\
    regex=True).astype(float)


# Changing each row value in 
# 'fall_2017', 'fall_2018, 'fall_2019', 'fall_2020', 'fall_2021', 
# '4_year_#_change',  
# for each 'Undergraduate', 'Graduate', and 'Combined' table, to an integer  
for i in range(1, 7):
    df_undergraduate.iloc[0:10, i] =\
        df_undergraduate.iloc[0:10, i].replace('\,', '',\
        regex=True).astype(int)
    df_graduate.iloc[0:10, i] =\
        df_graduate.iloc[0:10, i].replace('\,', '',\
        regex=True).astype(int)
    df_combined.iloc[0:10, i] =\
        df_combined.iloc[0:10, i].replace('\,', '',\
        regex=True).astype(int)
    
    
# Finally, we change the row names for 'student_ethnic_origin' column
# and reorder the rows
new_origin_names =\
    ['american_indian', 'asian', 'african_american', 'hispanic',\
    'international_students',\
    'native_hawaiian_or_pacific_islander', 'multi_racial', 'white',\
    'race_and_ethnicity_unknown',\
    'total']

# Undergraduate
df_undergraduate['student_ethnic_origin'] =\
    df_undergraduate['student_ethnic_origin']\
    .replace(list(df_undergraduate['student_ethnic_origin']), new_origin_names)
df_undergraduate = df_undergraduate.reindex([4, 1, 2, 3, 0, 6, 7, 5, 8, 9])

# Graduate
df_graduate['student_ethnic_origin'] =\
    df_graduate['student_ethnic_origin']\
    .replace(list(df_graduate['student_ethnic_origin']), new_origin_names)
df_graduate = df_graduate.reindex([4, 1, 2, 3, 0, 6, 7, 5, 8, 9])

# Combined
df_combined['student_ethnic_origin'] =\
    df_combined['student_ethnic_origin']\
    .replace(list(df_combined['student_ethnic_origin']), new_origin_names)
df_combined = df_combined.reindex([4, 1, 2, 3, 0, 6, 7, 5, 8, 9])


# Putting the 'undergraduate', 'graduate', and 'combined' tables into the
# database
df_undergraduate.to_sql('source_undergraduate', engine, if_exists='replace',\
    index=False)
df_graduate.to_sql('source_graduate', engine, if_exists='replace',\
    index=False)
df_combined.to_sql('source_combined', engine, if_exists='replace',\
    index=False)