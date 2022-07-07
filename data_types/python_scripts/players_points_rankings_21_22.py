import numpy as np
from IPython.display import display
import pandas as pd


# We bring the cleaned data from the players_points_rankings_21_22.csv file
# in the schema folder
players_points_rankings_21_22 =\
    pd.read_csv('sql_db_files/schema/players_points_rankings_21_22.csv')


# We generate .tex files containing some rows from our table
with open(
    '../python_generated_tables/'\
    'players_points_rankings_21_22_ordinal_nominal_ratio.tex', 'w')\
    as file:\
    file.write(
        players_points_rankings_21_22[:17].to_latex()
        )