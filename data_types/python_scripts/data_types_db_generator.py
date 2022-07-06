import pandas as pd
from sqlalchemy import create_engine
import sqlite3
import numpy as np
from IPython.display import display


# We create the sqlite engine
last_name_engine = create_engine('sqlite:///players_last_name_h.db', echo=False)


# We populate the raw data for players in the NBA or ABA with last name
# beginning with a H, as of June 29, 2022
players_last_name_h = pd.read_excel('players_last_name_h.xls')


# We drop the 'Player-additional' column
players_last_name_h.drop(columns=['Player-additional'], inplace=True)


# We change column headers to lower-case
new_columns = {x: x.lower().replace(' ', '_')\
    for x in players_last_name_h.columns}
players_last_name_h.rename(columns=new_columns, inplace=True)


# We change the 'from' and 'to' columns to
# 'from_year' to 'to_year', respectively
players_last_name_h.rename(columns={'from': 'from_year', 'to': 'to_year'},\
    inplace=True)


# We fill in 'NaN' entries within the 'colleges' column with 'none'
players_last_name_h['colleges'] =\
    players_last_name_h['colleges'].fillna('none')


# We truncate the time portion of the datetime datatype in the 'birth_date'
# column
players_last_name_h['birth_date'] =\
    players_last_name_h['birth_date'].apply(lambda x: x.date())


# We set the index as a column and rename it 'player_id'
players_last_name_h.index = np.arange(1, players_last_name_h.shape[0]+1)
players_last_name_h.reset_index(inplace=True)
players_last_name_h.rename(columns={'index': 'player_id'}, inplace=True)


# We create a database with our cleaned data
players_last_name_h.to_sql('players_last_name_h',\
    last_name_engine, if_exists='replace', index=False)


# 
#with open('players_last_name_h_nominal_interval_ratio.tex', 'w') as file:
    #file.write(
        #_.to_latex()
        #)


points_rankings_engine = create_engine\
    ('sqlite:///players_points_rankings_21_22.db', echo=False)


# We populate the raw data of players ranked by total points for the
# 2021-2022 season
players_points_rankings_21_22 = pd.read_excel\
    ('players_points_rankings_21_22.xls')


# We drop all columns except for 'Player' and 'PTS'
players_points_rankings_21_22.drop(columns=\
    ['Pos', 'Age', 'Tm', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', \
    '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', \
    'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'Player-additional'], inplace=True)


new_columns = {x: x.lower().replace(' ', '_')\
    for x in players_points_rankings_21_22.columns}
players_points_rankings_21_22.rename(columns=new_columns, inplace=True)


# We create a database with our cleaned data
players_points_rankings_21_22.to_sql('players_points_rankings_21_22',\
    points_rankings_engine, if_exists='replace', index=False)


# 
#with open('players_points_rankings_21_22_nominal_ordinal_ratio.tex', 'w') as file:
    #file.write(_.to_latex())