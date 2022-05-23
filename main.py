import json
import re

from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every
from starlette.responses import JSONResponse, RedirectResponse
from starlette.staticfiles import StaticFiles

from Chain.DGFood import DGFood
from Exception.Project221ossException import Project221ossException
from Parts.Search import MatjipSearch

app = FastAPI()
search_engine: MatjipSearch = None

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.exception_handler(Project221ossException)
async def validation_exception_handler(request, exc: Project221ossException):
    print(exc)
    return JSONResponse(
        status_code=exc.get_code(),
        content=exc.get_json(),
    )


@app.get("/")
async def root():
    return RedirectResponse("/static/map.html")


@app.get("/search/")
async def search(gu: str, keyword: str = ""):
    global search_engine

    keyword = re.sub(r'[\[\]{};:\'",/.<>?!@#$%^&*()_+|~\\\-=`\\\\]', '', keyword)

    def filter_gu(x):
        if gu.lower() in ["모두", "전체", "all", "다"]:
            return True
        else:
            if gu == x[1]:
                return True
            else:
                return False

    if keyword == "" or len(keyword) <= 1:
        # 구별 결과 로드
        result = DGFood().fetch_cache(gu)
        return result[:110]
    else:
        # 검색 결과 로드
        search_result = search_engine.search(query=keyword, limit_each=9999)
        search_result = list(filter(filter_gu, search_result))
        search_result = list(map(lambda x: json.loads(x[2], strict=False), search_result))
        return search_result


@app.on_event("startup")
@repeat_every(seconds=60 * 60 * 5)  # 5 hour
def renew_search_engine() -> None:
    global search_engine
    for x in ["중구", "동구", "서구", "남구", "북구", "수성구", "달서구", "달성군"]:
        DGFood().fetch_cache(x)
    se = MatjipSearch()
    search_engine = se
