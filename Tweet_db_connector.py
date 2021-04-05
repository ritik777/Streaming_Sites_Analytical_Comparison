from sqlalchemy import create_engine

import pymysql

import pandas as pd

#replace password with db password
cnx = create_engine('mysql+pymysql://root:<password>/streaming_analytics_db') 
dbConnection    = cnx.connect()

sample_dataframe = pd.read_csv("sample_tweets.csv")
# testing tweet_df created in the tweet_collector in the database straming_analytics_db
tableName = "sample_tweets_to_check"

try:
    frame = sample_dataframe.to_sql(tableName, dbConnection, if_exists='fail')
except ValueError as vx:
    print(vx)
except Exception as ex:   
    print(ex)
else:
    print("Table %s created successfully."%tableName);   
finally:
    dbConnection.close()
