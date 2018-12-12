import pandas as pd
import sqlalchemy

db = False
while not db:
    try:
        engine = sqlalchemy.create_engine('postgresql://user:user@db/tabela')
        con = engine.connect()
        for item in pd.read_csv('data/police-department-incidents.csv', chunksize=1000):
            item.to_sql('police_incidents', con, if_exists='append')
    except Exception as e:
        db = False
    else:
        db = True
