import pandas as pd
from IPython.display import display
import numpy as np
from sqlalchemy import create_engine
import sqlite3


# Creating the engine for our tables
engine = create_engine('sqlite:///steph_curry_game_stats.db', echo=False)


# 2009-2010 statistics
df_09 = pd.read_excel('raw_steph_curry_game_stats/regular_season_09_10.xls')

# Cleaning 2009-2010 statistics
df_09['Unnamed: 5'].fillna('none', inplace=True)

df_09['away_game'] = df_09['Unnamed: 5'].map({'@': 1, 'none': 0})

df_09 = df_09.loc[df_09['G'].notnull()]

df_09.drop(columns=['G', 'Tm', 'Rk', 'Unnamed: 5', 'MP'], inplace=True)

df_09.index = np.arange(1, df_09.shape[0] + 1)

df_09.reset_index(inplace=True)

df_09.rename(columns={'index': 'game_id'}, inplace=True)

# Sending df_09 cleaned data to database
df_09.to_sql('season_09_10', engine, if_exists='replace', index=False)


# 2010-2011 statistics
df_10 = pd.read_excel('raw_steph_curry_game_stats/regular_season_10_11.xls')

# Cleaning 2010-2011 statistics
df_10['Unnamed: 5'].fillna('none', inplace=True)

df_10['away_game'] = df_10['Unnamed: 5'].map({'@': 1, 'none': 0})

df_10 = df_10.loc[df_10['G'].notnull()]

df_10.drop(columns=['G', 'Tm', 'Rk', 'Unnamed: 5', 'MP'], inplace=True)

df_10.index = np.arange(1, df_10.shape[0] + 1)

df_10.reset_index(inplace=True)

df_10.rename(columns={'index': 'game_id'}, inplace=True)

# Sending df_10 cleaned data to database
df_10.to_sql('season_10_11', engine, if_exists='replace', index=False)


# 2011-2012 statistics
df_11 = pd.read_excel('raw_steph_curry_game_stats/regular_season_11_12.xls')

# Cleaning 2011-2012 statistics
df_11['Unnamed: 5'].fillna('none', inplace=True)

df_11['away_game'] = df_11['Unnamed: 5'].map({'@': 1, 'none': 0})

df_11 = df_11.loc[df_11['G'].notnull()]

df_11.drop(columns=['G', 'Tm', 'Rk', 'Unnamed: 5', 'MP'], inplace=True)

df_11.index = np.arange(1, df_11.shape[0] + 1)

df_11.reset_index(inplace=True)

df_11.rename(columns={'index': 'game_id'}, inplace=True)

# Sending df_11 cleaned data to database
df_11.to_sql('season_11_12', engine, if_exists='replace', index=False)


# 2012-2013 statistics
df_12 = pd.read_excel('raw_steph_curry_game_stats/regular_season_12_13.xls')

# Cleaning 2012-2013 statistics
df_12['Unnamed: 5'].fillna('none', inplace=True)

df_12['away_game'] = df_12['Unnamed: 5'].map({'@': 1, 'none': 0})

df_12 = df_12.loc[df_12['G'].notnull()]

df_12.drop(columns=['G', 'Tm', 'Rk', 'Unnamed: 5', 'MP'], inplace=True)

df_12.index = np.arange(1, df_12.shape[0] + 1)

df_12.reset_index(inplace=True)

df_12.rename(columns={'index': 'game_id'}, inplace=True)

# Sending df_12 cleaned data to database
df_12.to_sql('season_12_13', engine, if_exists='replace', index=False)


# 2013-2014 statistics
df_13 = pd.read_excel('raw_steph_curry_game_stats/regular_season_13_14.xls')

# Cleaning 2013-2014 statistics
df_13['Unnamed: 5'].fillna('none', inplace=True)

df_13['away_game'] = df_13['Unnamed: 5'].map({'@': 1, 'none': 0})

df_13 = df_13.loc[df_13['G'].notnull()]

df_13.drop(columns=['G', 'Tm', 'Rk', 'Unnamed: 5', 'MP'], inplace=True)

df_13.index = np.arange(1, df_13.shape[0] + 1)

df_13.reset_index(inplace=True)

df_13.rename(columns={'index': 'game_id'}, inplace=True)

# Sending df_13 cleaned data to database
df_13.to_sql('season_13_14', engine, if_exists='replace', index=False)


# 2014-2015 statistics
df_14 = pd.read_excel('raw_steph_curry_game_stats/regular_season_14_15.xls')

# Cleaning 2014-2015 statistics
df_14['Unnamed: 5'].fillna('none', inplace=True)

df_14['away_game'] = df_14['Unnamed: 5'].map({'@': 1, 'none': 0})

df_14 = df_14.loc[df_14['G'].notnull()]

df_14.drop(columns=['G', 'Tm', 'Rk', 'Unnamed: 5', 'MP'], inplace=True)

df_14.index = np.arange(1, df_14.shape[0] + 1)

df_14.reset_index(inplace=True)

df_14.rename(columns={'index': 'game_id'}, inplace=True)

# Sending df_14 cleaned data to database
df_14.to_sql('season_14_15', engine, if_exists='replace', index=False)


# 2015-2016 statistics
df_15 = pd.read_excel('raw_steph_curry_game_stats/regular_season_15_16.xls')

# Cleaning 2015-2016 statistics
df_15['Unnamed: 5'].fillna('none', inplace=True)

df_15['away_game'] = df_15['Unnamed: 5'].map({'@': 1, 'none': 0})

df_15 = df_15.loc[df_15['G'].notnull()]

df_15.drop(columns=['G', 'Tm', 'Rk', 'Unnamed: 5', 'MP'], inplace=True)

df_15.index = np.arange(1, df_15.shape[0] + 1)

df_15.reset_index(inplace=True)

df_15.rename(columns={'index': 'game_id'}, inplace=True)

# Sending df_15 cleaned data to database
df_15.to_sql('season_15_16', engine, if_exists='replace', index=False)


# 2016-2017 statistics
df_16 = pd.read_excel('raw_steph_curry_game_stats/regular_season_16_17.xls')

# Cleaning 2016-2017 statistics
df_16['Unnamed: 5'].fillna('none', inplace=True)

df_16['away_game'] = df_16['Unnamed: 5'].map({'@': 1, 'none': 0})

df_16 = df_16.loc[df_16['G'].notnull()]

df_16.drop(columns=['G', 'Tm', 'Rk', 'Unnamed: 5', 'MP'], inplace=True)

df_16.index = np.arange(1, df_16.shape[0] + 1)

df_16.reset_index(inplace=True)

df_16.rename(columns={'index': 'game_id'}, inplace=True)

# Sending df_16 cleaned data to database
df_16.to_sql('season_16_17', engine, if_exists='replace', index=False)


# 2017-2018 statistics
df_17 = pd.read_excel('raw_steph_curry_game_stats/regular_season_17_18.xls')

# Cleaning 2017-2018 statistics
df_17['Unnamed: 5'].fillna('none', inplace=True)

df_17['away_game'] = df_17['Unnamed: 5'].map({'@': 1, 'none': 0})

df_17 = df_17.loc[df_17['G'].notnull()]

df_17.drop(columns=['G', 'Tm', 'Rk', 'Unnamed: 5', 'MP'], inplace=True)

df_17.index = np.arange(1, df_17.shape[0] + 1)

df_17.reset_index(inplace=True)

df_17.rename(columns={'index': 'game_id'}, inplace=True)

# Sending df_17 cleaned data to database
df_17.to_sql('season_17_18', engine, if_exists='replace', index=False)


# 2018-2019 statistics
df_18 = pd.read_excel('raw_steph_curry_game_stats/regular_season_18_19.xls')

# Cleaning 2018-2019 statistics
df_18['Unnamed: 5'].fillna('none', inplace=True)

df_18['away_game'] = df_18['Unnamed: 5'].map({'@': 1, 'none': 0})

df_18 = df_18.loc[df_18['G'].notnull()]

df_18.drop(columns=['G', 'Tm', 'Rk', 'Unnamed: 5', 'MP'], inplace=True)

df_18.index = np.arange(1, df_18.shape[0] + 1)

df_18.reset_index(inplace=True)

df_18.rename(columns={'index': 'game_id'}, inplace=True)

# Sending df_18 cleaned data to database
df_18.to_sql('season_18_19', engine, if_exists='replace', index=False)


# 2019-2020 statistics
df_19 = pd.read_excel('raw_steph_curry_game_stats/regular_season_19_20.xls')

# Cleaning 2019-2020 statistics
df_19['Unnamed: 5'].fillna('none', inplace=True)

df_19['away_game'] = df_19['Unnamed: 5'].map({'@': 1, 'none': 0})

df_19 = df_19.loc[df_19['G'].notnull()]

df_19.drop(columns=['G', 'Tm', 'Rk', 'Unnamed: 5', 'MP'], inplace=True)

df_19.index = np.arange(1, df_19.shape[0] + 1)

df_19.reset_index(inplace=True)

df_19.rename(columns={'index': 'game_id'}, inplace=True)

# Sending df_19 cleaned data to database
df_19.to_sql('season_19_20', engine, if_exists='replace', index=False)


# 2020-2021 statistics
df_20 = pd.read_excel('raw_steph_curry_game_stats/regular_season_20_21.xls')

# Cleaning 2020-2021 statistics
df_20['Unnamed: 5'].fillna('none', inplace=True)

df_20['away_game'] = df_20['Unnamed: 5'].map({'@': 1, 'none': 0})

df_20 = df_20.loc[df_20['G'].notnull()]

df_20.drop(columns=['G', 'Tm', 'Rk', 'Unnamed: 5', 'MP'], inplace=True)

df_20.index = np.arange(1, df_20.shape[0] + 1)

df_20.reset_index(inplace=True)

df_20.rename(columns={'index': 'game_id'}, inplace=True)

# Sending df_20 cleaned data to database
df_20.to_sql('season_20_21', engine, if_exists='replace', index=False)


# 2021-2022 statistics
df_21 = pd.read_excel('raw_steph_curry_game_stats/regular_season_21_22.xls')

# Cleaning 2021-2022 statistics
df_21['Unnamed: 5'].fillna('none', inplace=True)

df_21['away_game'] = df_21['Unnamed: 5'].map({'@': 1, 'none': 0})

df_21 = df_21.loc[df_21['G'].notnull()]

df_21.drop(columns=['G', 'Tm', 'Rk', 'Unnamed: 5', 'MP'], inplace=True)

df_21.index = np.arange(1, df_21.shape[0] + 1)

df_21.reset_index(inplace=True)

df_21.rename(columns={'index': 'game_id'}, inplace=True)

# Sending df_21 cleaned data to database
df_21.to_sql('season_21_22', engine, if_exists='replace', index=False)