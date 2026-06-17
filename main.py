from fastapi import FastAPI
from route.test_db import test_routes
from route.user import user_router
import uvicorn

app = FastAPI()

app.include_router(test_routes)

app.include_router(user_router)



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)