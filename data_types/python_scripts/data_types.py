import pandas as pd
from sqlalchemy import create_engine
import sqlite3
from IPython.display import display


# We create the sqlite engine
engine = create_engine('sqlite:///player_last_name_h.db', echo=False)


# We populate the raw data for players in the NBA or ABA with last name
# beginning with a H, as of June 29, 2022
players_last_name_h = pd.read_excel('player_last_name_h.xls')


# We drop the 'Player-additional' column
players_last_name_h.drop(columns=['Player-additional'], inplace=True)


# We display the first 17 names, before resetting the index to 'Player', so
# that we know the name of the 17th player when we wish to display the first
# 17 players using the new 'Player' index in subsequent queries. This will
# also serve as a nominal data-type tabel
display(players_last_name_h.loc[:16]['Player'])
print('\n')


# Sending players_last_name_h.loc[:16]['Player'] data table to a .tex file
with open('players_last_name_h_nominal.tex', 'w') as file:
    file.write(players_last_name_h.loc[:16]['Player'].to_latex())


# Resetting the index to 'Player'
players_last_name_h = players_last_name_h.set_index('Player')


# Sorting the data by 'From', which is the year the player began their career
# in the NBA or ABA. This will serve to display the difference between nominal,
# interval, and ratio data-types
display(players_last_name_h.loc[:'Chick Halbert',\
    ['From', 'Wt']].sort_values('From'))
print('\n')


# Sending
# players_last_name_h.loc[:'Chick Halbert',\
#    ['From', 'Wt']].sort_values('From')
# data table to a .tex file
with open('players_last_name_h_nominal_interval_ratio.tex', 'w') as file:
    file.write(
        players_last_name_h.loc[:'Chick Halbert',\
        ['From', 'Wt']].sort_values('From').to_latex()
        )


# We populate the raw data of players ranked by total points for the
# 2021-2022 season
players_points_rankings = pd.read_excel('points_rankings.xls')


# We reset the index to the 'Rk' column
players_points_rankings = players_points_rankings.set_index('Rk')


# We drop all columns except for 'Player' and 'PTS', against the new 'Rk'
# index
players_points_rankings.drop(columns=\
    ['Pos', 'Age', 'Tm', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', \
    '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', \
    'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'Player-additional'], inplace=True)


# Display the top 20 ranked players in this table. This table will serve to
# display the difference between ordinal, nominal, and ratio data-types
display(players_points_rankings.loc[1:20])


# Sending players_points_rankings.loc[1:20] data table to a .tex file
with open('players_points_rankings_nominal_ordinal_ratio.tex', 'w') as file:
    file.write(players_points_rankings.loc[1:20].to_latex())