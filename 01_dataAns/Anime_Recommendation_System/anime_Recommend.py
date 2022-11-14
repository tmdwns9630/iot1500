INPUT_DIR = '/kaggle'
# !ls {INPUT_DIR}

#C:\iot1500\Anime_Recommendation_System\kaggle\input\anime-recommendation-database-2020
import numpy as np
import pandas as pd

rating_df = pd.read_csv(INPUT_DIR + '/animelist.csv', 
                        low_memory=False, 
                        usecols=["user_id", "anime_id", "rating"]
                        #, nrows=90000000
                        )
rating_df.head(4)
