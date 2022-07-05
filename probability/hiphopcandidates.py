from sqlalchemy import create_engine
import pandas as pd
import sqlite3
from IPython.display import display


engine = create_engine('sqlite:///hiphopcandidates.db', echo=False)


raw_data = pd.read_csv('genius_hip_hop_lyrics.csv')


raw_data.to_sql('rapper_candidate_map', engine, if_exists='replace',\
    index=False)