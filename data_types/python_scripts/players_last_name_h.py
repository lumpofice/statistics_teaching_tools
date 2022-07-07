import numpy as np
from IPython.display import display
import pandas as pd


# We bring in the cleaned data from the players_last_name_h.csv file
# in the schema folder
players_last_name_h =\
    pd.read_csv('sql_db_files/schema/players_last_name_h.csv')


# We generate .tex files containing some rows from our table
with open('../python_generated_tables/players_last_name_h_nominal.tex', 'w')\
    as file:\
    file.write(
        players_last_name_h['player_name'][:17].to_latex()
        )


with open(
        '../python_generated_tables/players_last_name_h_nominal_interval_ratio'\
        '.tex', 'w') as file:\
    file.write(
        players_last_name_h[
            ['player_name', 'weight', 'birth_date']
            ][:17].to_latex()
        )