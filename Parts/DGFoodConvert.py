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
    dgFood = DGFoodConvert(_example_fetch).convert_to_csv(cnt, "FD_CS") # 해당 키 값 가져오기

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
