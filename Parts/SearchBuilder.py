import json

import dotenv

from Chain.DGFood import DGFood
from Parts.DGFoodConvert import DGFoodConvert

dotenv.load_dotenv()
import requests
import os
from typing import *
from diskcache import FanoutCache


def search_builder():
    result_csv = []

    for gu in ["중구", "동구", "서구", "남구", "북구", "수성구", "달서구", "달성군"]:
        fetch_data = DGFood().fetch_cache(matjip_gu=gu)
        convert_data = DGFoodConvert(dg_food_fetch=fetch_data).convert_to_db_csv(gu_info=gu, cnt_start_from=len(result_csv))
        result_csv.extend(convert_data)


    return result_csv



search_builder()