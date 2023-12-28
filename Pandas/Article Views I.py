# SELECT DISTINCT ON (author_id) author_id as id FROM Views WHERE author_id = viewer_id;
# SELECT author_id as id FROM Views WHERE author_id = viewer_id GROUP BY author_id;

import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return views[(views["author_id"] == views["viewer_id"])][["author_id"]].rename(columns={"author_id": "id"}).drop_duplicates(subset=["id"]).sort_values(by=["id"])