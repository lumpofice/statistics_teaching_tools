import camelot 
from IPython.display import display
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
import sqlite3


# Initiating the database
engine =\
    create_engine('sqlite:///csu_enrollment_by_ethnic_origin_03_07.db',\
        echo=False)


# Bringing in the table(s) from the pdf using camelot
pdf =\
    camelot.read_pdf('../csu_enrollment_by_ethnic_origin_03_07.pdf',\
        pages='1,2', flavor='stream')


# We have two tables in our 'pdf' object. So, we bring in each, separately
# then combine with pandas and reindex
df_0 = pdf[0].df
df_1 = pdf[1].df
df = pd.concat([df_0, df_1], axis=0)
df.index = np.arange(0, df.shape[0])


# We separate the three different categories 
# 'Undergraduate', 'Graduate', 'Combined'

# Undergraduate dataframe
df_undergraduate = df.loc[0:19]

# Graduate dataframe
df_graduate = pd.concat([df.loc[0:2], df.loc[20:36]], axis=0)
df_graduate.index = np.arange(0, df_graduate.shape[0])

# Combined dataframe
df_combined = pd.concat([df.loc[0:2], df.loc[37:53]], axis=0)
df_combined.index = np.arange(0, df_combined.shape[0])


def drop_and_rename(i):
    '''This function will drop rows, change the names of row values, change
    column names and reindex our dataframe, for each of our three dataframes'''
    
    
    # Drop the two 'title/subtitle' rows
    i = i.drop([0, 3])
    i.index = np.arange(0, i.shape[0])
    
    
    # Changing the column names
    single_year_column_names =\
        {i.loc[1][j]: f'fall_{i.loc[1][j]}' for j in range(1, 6)}
    multi_year_column_names =\
        {i.loc[1][j]: f'4_year_{i.loc[1][j].lower().replace(" ", "_")}'\
            for j in range(6, 8)}
    new_columns = {**single_year_column_names, **multi_year_column_names}
    new_column_names = {j+1: list(new_columns.values())[j] for j in range(0,7)}
    
    
    # Changing ethnic origin (column 0) row values
    student_ethnic_origin =\
        {i[0][j]: i[0][j].lower().replace(' ', '_').replace('-', '_')\
            for j in range(2, 18, 2)}
    
    
    # Dropping non-quantitative data rows
    for j in range(2, 18, 2):
        i.drop(j, inplace=True)
        
        
    # Dropping superfluous rows
    i.drop([0, 1], inplace=True)
    
    
    # Bringing in new_column_names
    i.drop(columns=0, inplace=True)
    i.rename(columns=new_column_names, inplace=True)
    
    
    # Inserting 'student_ethnic_origin' column
    i.insert(0, 'student_ethnic_origin', list(student_ethnic_origin.values()))
    
    
    # Re-index
    i.index = np.arange(0, i.shape[0])
    
    
    # Removing the percentage symbol from the '4_year_%_change' column
    # and changing the quantitative data in this column to floats.
    # Then changing all other quantitative data to integers
    i['4_year_%_change'] =\
        i['4_year_%_change'].replace('\%', '', regex=True).astype(float)
    i['4_year_#_change'] = i['4_year_#_change'].astype(int)
    i['fall_2003'] = i['fall_2003'].replace('\,', '', regex=True).astype(int)
    i['fall_2004'] = i['fall_2004'].replace('\,', '', regex=True).astype(int)
    i['fall_2005'] = i['fall_2005'].replace('\,', '', regex=True).astype(int)
    i['fall_2006'] = i['fall_2006'].replace('\,', '', regex=True).astype(int)
    i['fall_2007'] = i['fall_2007'].replace('\,', '', regex=True).astype(int)
    
    
    return i


df_undergraduate = drop_and_rename(df_undergraduate)
df_graduate = drop_and_rename(df_graduate)
df_combined = drop_and_rename(df_combined)


# Putting the 'undergraduate', 'graduate', and 'combined' tables into the
# database
df_undergraduate.to_sql('source_undergraduate', engine, if_exists='replace',\
    index=False)
df_graduate.to_sql('source_graduate', engine, if_exists='replace',\
    index=False)
df_combined.to_sql('source_combined', engine, if_exists='replace',\
    index=False)