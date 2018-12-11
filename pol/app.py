import pandas as pd
import sqlalchemy

df = pd.read_csv('data/police-department-incidents.csv')


db = False
while not db:
    try:
        engine = sqlalchemy.create_engine('postgresql://user:user@db/tabela')
        con = engine.connect()
        df.to_sql('police_incidents', con)
    except:
        db = False
    else:
        db = True
