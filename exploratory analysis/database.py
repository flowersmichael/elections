import json
import pandas as pd
import numpy as np
import re
from sqlalchemy import create_engine
from config import db_password
from sqlalchemy import create_engine
import psycopg2
import io
import time

independent_df = pd.read_csv('resources/fec-independent-expenditures.csv', low_memory=False)
db_string = f'postgresql://postgres:{db_password}@127.0.0.1:5433/G5' #SQL port
engine = create_engine(db_string)
independent_df.to_sql(name='fec_independent_expenditures', con=engine, if_exists ='replace')

senate_df = pd.read_csv('senate_dataset.csv', low_memory=False)
db_string = f'postgresql://postgres:{db_password}@127.0.0.1:5433/G5' #SQL port
engine = create_engine(db_string)
senate_df.to_sql(name='Senate_Elections_1976_2020', con=engine, if_exists ='replace')