from typing import List


class DGFoodConvert:
    dg_food_fetch: List[dict]

    def __init__(self, dg_food_fetch):
        self.dg_food_fetch = dg_food_fetch

    def convert_to_csv(self, x) -> List[List[str]]:
        dg_food_fetch: List[dict] = self.dg_food_fetch
        dgfoodcnt = x
        chart=[[] for x in range(dgfoodcnt)]
        for i in range(0, len(dg_food_fetch)):
            chart[i].append(list(dg_food_fetch[i].values()))
         #   for a in dg_food_fetch[i].keys(): # key리스트를 만들어 a에 옮긴 후
         #       chart[i].append(dg_food_fetch[i][a].split()) # fetch 파일에서 키값을 제외하고 저장
        return chart
        ... 

    ...


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

    dgFood = [[] for x in range(cnt)]

    dgFood = DGFoodConvert(_example_fetch).convert_to_csv(cnt)

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
