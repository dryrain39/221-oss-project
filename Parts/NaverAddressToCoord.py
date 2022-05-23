import json

import dotenv

dotenv.load_dotenv()
import requests
import os
from typing import *
from diskcache import FanoutCache

cache = FanoutCache(directory="./.cache/memoize/", shards=4)


@cache.memoize(tag="geo", expire=2592000)  # 2592000 == 30일. 주소정보는 바뀌지 않으므로 길게 설정
def request_geo(address: str):
    response = requests.get("https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode", params={
        "query": address,
    }, headers={
        "X-NCP-APIGW-API-KEY-ID": os.environ.get("NCP_CLIENT_ID"),
        "X-NCP-APIGW-API-KEY": os.environ.get("NCP_CLIENT_SECRET")
    })

    return response


def get_lat_lng_from_address(address: str) -> Tuple[bool, str, str]:
    response = request_geo(address=address)
    print(json.dumps(response.json(), ensure_ascii=False))

    if response.status_code != 200:
        return False, "", ""

    response_dict = response.json()

    if len(response_dict["addresses"]) == 0:
        return False, "", ""

    return True, response_dict["addresses"][0]["y"], response_dict["addresses"][0]["x"]




if __name__ == '__main__':
    print(get_lat_lng_from_address("대구 중구 공평로 88"))
