import logging
from typing import List
from Parts.DGFoodConvert import DGFoodConvert
from Parts.DGFoodFetch import DGFoodFetch
from Parts.FileCache import FileCache


class DGFood:
    def __init__(self):
        self.cache = FileCache(name="DGFood", namespace="DGFood")
        ...

    @staticmethod
    def gu_name_validation(gu: str) -> List[str]:
        # 전체 구 목록
        gu_names = ["중구", "동구", "서구", "남구", "북구", "수성구", "달서구", "달성군"]

        # 입력받은 구가 str 형식이 아니면 전체 구 목록 반환
        if type(gu) != str:
            return gu_names

        # 입력받은 구가 모두 또는 전체 또는 all 또는 다 이면 전체 구 목록 반환
        if gu.lower() in ["모두", "전체", "all", "다"]:
            return gu_names

        # 입력받은 구가 전체 구 목록중에 없을 경우 (없는 구(지역)의 경우) 전체 구 목록 반화
        if gu not in gu_names:
            return gu_names
        else:
            # 입력받은 구가 올바르면 반환
            return [gu]

    def _fetch(self, matjip_gu: str):
        gu_name = self.gu_name_validation(matjip_gu)
        fetch = DGFoodFetch()

        result_matjip_list = []

        for gu in gu_name:
            success, matjip_data = self.cache.get_or_call(fun=fetch.fetch, args=(gu,), key=gu)

            if not success:
                self.cache.rm(key=gu)
                continue

            result_matjip_list.extend(matjip_data)

        return result_matjip_list

    def get_csv(self, matjip_gu: str):
        fetch_result = self._fetch(matjip_gu=matjip_gu)
        convert = DGFoodConvert(dg_food_fetch=fetch_result)
        return convert.convert_to_csv(x=len(fetch_result))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    d = DGFood()
    print(d.get_csv("북구"))
