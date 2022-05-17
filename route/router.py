from fastapi import APIRouter

# import package as package_router
from route.test.dgfood import router as dgfood_router

api_router = APIRouter()

api_router.include_router(dgfood_router, prefix='/test/dgfood', tags=['test/dgfood'])
