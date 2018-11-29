import pandas as pd
import sqlalchemy

df = pd.read_csv('data/restaurant-scores-lives-standard.csv')
engine = sqlalchemy.create_engine('postgresql://user:user@kaggle_db/tabela')
con = engine.connect()

df.to_sql('restaurant2', con)
