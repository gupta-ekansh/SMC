import pandas as pd
from sqlalchemy import create_engine

database_name = 'merged_data'
username = 'root'
password = '1234'
host = 'localhost'

csv_file_path = 'merged.csv'
df = pd.read_csv(csv_file_path)

engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@{host}/{database_name}')

df.to_sql('merged', engine, if_exists='append', index=False)


engine.dispose()

                         