# SELECT tweet_id FROM Tweets WHERE LENGTH(content) > 15;

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets[tweets["content"].str.len() > 15][["tweet_id"]]