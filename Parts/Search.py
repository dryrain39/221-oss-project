import json
import time

import dotenv

from Parts.SearchBuilder import search_builder

dotenv.load_dotenv()
import requests
import os
from typing import *
from diskcache import FanoutCache
import sqlite3


# 기 개발한 소스코드에서 가져옴
class MatjipSearch:
    COL = "idx, gu, json, tags"
    COL_VALUES = "?,?,?,?"
    csv_data: List[str]

    def __init__(self):
        # todo 지금은 인스턴스를 실행 할 때마다 csv 를 만들지만 옵션값을 줘야 함.
        self.csv_data = search_builder()
        self.db = sqlite3.connect(':memory:', check_same_thread=False)
        self.cur = self.db.cursor()
        self.cur.execute('create virtual table imdb using '
                         f'fts5({self.COL}, tokenize="porter unicode61");')

        self.cur.executemany(f"insert into imdb({self.COL}) values ({self.COL_VALUES})", self.csv_data)

    def match_search(self, query, limit=100):
        return self.cur.execute(f"""
        select *, rank
        from imdb
        where imdb MATCH "{query}"
        ORDER BY rank
        LIMIT {limit}""").fetchall()

    def like_search(self, query, limit=100):
        return self.cur.execute(f"""
        select *, rank
        from imdb
        where {query}
        ORDER BY rank
        LIMIT {limit}""").fetchall()

    def search(self, query, limit_each=200):
        inp = query.strip().split(" ")
        inp = list(map(lambda x: None if len(x.replace("%", "")) <= 1 else x.replace("%", ""), inp))
        inp = list(filter(None, inp))

        search_result = []
        idx_set = set()

        match_query = " AND ".join(inp)
        for result in self.match_search(match_query, limit_each):
            if result[0] in idx_set:
                continue
            idx_set.add(result[0])
            search_result.append(result)

        like_query = f'tags LIKE "%{inp[0]}%" '
        for keyword in inp[1:]:
            like_query += f'AND tags LIKE "%{keyword}%"'
        for result in self.like_search(like_query, limit_each):
            if result[0] in idx_set:
                continue
            idx_set.add(result[0])
            search_result.append(result)

        return search_result


if __name__ == '__main__':
    sch = MatjipSearch()

    s = time.time()
    for x in sch.search("한우"):
        print(x)
    print(time.time() - s, "secs")
