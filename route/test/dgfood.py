import json
import logging

from fastapi import APIRouter
from starlette.requests import Request

from Exception.Project221ossException import ValueOrValidateException
from Parts.DGFoodConvert import DGFoodConvert
from Parts.DGFoodFetch import DGFoodFetch

router = APIRouter()


@router.get("/convert/convert_to_csv")
async def convert_to_csv(request: Request, fetch_json: str):
    return_dict = {
        "log": []
    }

    def add_log(msg: str):
        logging.info(msg)
        return_dict["log"].append(msg)

    add_log(f"fetch_json 값을 받았습니다: {fetch_json}")

    try:
        fetch_dict = json.loads(fetch_json)
        add_log(f"json 을 잘 파싱했습니다.")
        return_dict["result"] = DGFoodConvert(dg_food_fetch=fetch_dict).convert_to_csv()
        add_log(f"실행이 완료되었습니다.")
    except Exception as e:
        add_log(f"오류 발생: " + str(e))
        raise ValueOrValidateException(message="실행 중 에러 발생.", extra=return_dict)

    return return_dict


@router.get("/fetch/fetch")
async def fetch(request: Request, gu_name: str):
    return_dict = {
        "log": []
    }

    def add_log(msg: str):
        logging.info(msg)
        return_dict["log"].append(msg)

    add_log(f"gu_name 값을 받았습니다: {gu_name}")

    try:
        return_dict["result"] = return_dict["result"] = DGFoodFetch().fetch(gu_name)
        add_log(f"실행이 완료되었습니다.")
    except Exception as e:
        add_log(f"오류 발생: " + str(e))
        raise ValueOrValidateException(message="실행 중 에러 발생.", extra=return_dict)

    return return_dict
