from typing import Tuple, List


class DGFoodFetch:
    def fetch(self, addr: str) -> Tuple[bool, List[str]]:
        ...

    ...


if __name__ == '__main__':
    # https://www.daegufood.go.kr/kor/api/tasty.html?mode=json&addr={구이름}
    # 에서 데이터를 가져왔을 때 return 값으로 "data" 부분만 있어야 함.

    # 입력: 구이름(addr)
    # 출력: (성공 여부, 결과 목록)

    print("return: ", DGFoodFetch().fetch("북구"))
    # 예상 결과:
    # [
    #   {
    #     "cnt": "1",
    #     "OPENDATA_ID": "1730",
    #     "GNG_CS": "대구광역시 북구 서변동 1779",
    #     ...
