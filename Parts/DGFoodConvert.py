import json
import copy
from typing import List
import csv

class DGFoodConvert:
    dg_food_fetch: List[dict]

    def __init__(self, dg_food_fetch):
        self.dg_food_fetch = dg_food_fetch

   def convert_to_csv(self, x, key =  None) -> List[List[str]]:
      dg_food_fetch: List[dict] = self.dg_food_fetch
      dgfoodcnt = x
      chart=[[] for k in range(dgfoodcnt)]

      if key == None:
          for i in range(0, len(dg_food_fetch)):
              chart[i].append(dg_food_fetch[i].values())
          return chart
      else:
          for i in range(0, len(dg_food_fetch)):
              chart[i].append(dg_food_fetch[i][key])
          return chart

    def convert_to_db_csv(self, gu_info, cnt_start_from=0):
        dg_food_fetch: List[dict] = self.dg_food_fetch

        def filter_loc(x):
            return x["coord_available"]

        def convert(z):
            x = copy.deepcopy(z)
            if not hasattr(convert, "count"):
                convert.count = cnt_start_from - 1

            del x["cnt"]
            del x["OPENDATA_ID"]
            del x["SEAT_CNT"]
            del x["PKPL"]
            x["TLNO"] = x["TLNO"].replace("-", "")
            del x["PSB_FRN"]
            x["BKN_YN"] = "예약" if not x["BKN_YN"] == "불가능" else ""
            x["INFN_FCL"] = "놀이방 키즈존 키즈 놀이시설" if not x["INFN_FCL"] == "불가능" else ""
            x["BRFT_YN"] = "아침 조식" if not x["BRFT_YN"] == "불가능" else ""
            x["DSSRT_YN"] = "후식 디저트" if not x["DSSRT_YN"] == "불가능" else ""

            x["SBW"] = x["SBW"].replace("주변에 가까운 지하철역이 없습니다.", "")
            x["SBW"] = x["SBW"].replace("거리", "").replace("도보로 약", "")
            x["SBW"] = x["SBW"].replace("지하철", "").replace("1호선", "").replace("2호선", "").replace("3호선", "").strip()
            x["BUS"] = x["BUS"].replace("버스 정류장은", "").replace("정류장이 가장 가깝습니다.", "")

            if x["coord_available"]:
                del x["lat"]
                del x["lng"]

            del x["coord_available"]

            convert.count += 1
            vals = (" ".join(list(filter(lambda a: type(a) == str, x.values())))).replace("<br />", " ")
            return convert.count, gu_info, json.dumps(z, ensure_ascii=False), vals

        filter_result = list(filter(filter_loc, dg_food_fetch))
        convert_result = list(map(convert, filter_result))
        return convert_result
      

if __name__ == '__main__':
    # https://www.daegufood.go.kr/kor/api/tasty.html?mode=json&addr={구이름}
    # 에서 가져온 데이터를 csv 형태로 가공해야 함.

    # 입력값: 없음
    # 출력값: 배열 형태의 값
    _example_fetch = [
        {
            "cnt": "1",
            "OPENDATA_ID": "1730",
            "GNG_CS": "대구광역시 북구 서변동 ****",
            "FD_CS": "디저트/베이커리",
        },
        {
            "cnt": "2",
            "OPENDATA_ID": "1234",
            "GNG_CS": "대구광역시 북구 구암동 ****",
            "FD_CS": "중화요리",
        },
        {
            "cnt": "3",
            "OPENDATA_ID": "4567",
            "GNG_CS": "대구광역시 북구 대학로 ****",
            "FD_CS": "일식",
        },
        {
            "cnt": "4",
            "OPENDATA_ID": "7789",
            "GNG_CS": "대구광역시 북구 고성로 ****",
            "FD_CS": "카페",
        },
        {
            "cnt": "5",
            "OPENDATA_ID": "7789",
            "GNG_CS": "대구광역시 북구 고성로 ****",
            "FD_CS": "카페",
        },
        {
            "cnt": "6",
            "OPENDATA_ID": "7789",
            "GNG_CS": "대구광역시 북구 고성로 ****",
            "FD_CS": "카페",
        }
    ]

    cnt = len(_example_fetch)

    dgFood = [[] for k in range(cnt)]

    # dgFood = DGFoodConvert(_example_fetch).convert_to_csv(cnt) # 전체 값 가져오기
    dgFood = DGFoodConvert(_example_fetch).convert_to_csv(cnt, "FD_CS")  # 해당 키 값 가져오기

    for i in range(0, len(dgFood)):
        print("return: ", dgFood[i])
    # 예상 출력:
    # [
    #   [
    #      "1",
    #      "1730",
    #      "대구광역시 북구 서변동 ****",
    #      "디저트/베이커리"
    #   ],
    #   [
    #      "2",
    #      "1234",
    #      "대구광역시 북구 구암동 ****",
    #      "중화요리"
    #   ]
    # ]
