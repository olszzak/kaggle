import pandas as pd
import sqlalchemy

df = pd.read_csv('data/restaurant-scores-lives-standard.csv')


db = False
while not db:
    try:
        engine = sqlalchemy.create_engine('postgresql://user:user@db/tabela')
        con = engine.connect()
        df.to_sql('restaurant_scores', con)
    except:
        db = False
    else:
        db = True
        con.close()
