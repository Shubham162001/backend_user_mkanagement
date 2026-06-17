from fastapi import FastAPI, Depends
from fastapi import APIRouter 
from db_utils.get_db import get_db
from sqlalchemy.orm import Session
from sqlalchemy import text

test_routes = APIRouter()

@test_routes.get("/test")
def test(db: Session =  Depends(get_db)):
    test = db.execute(text("select * from students;")).fetchall()
    return {"message": f"Database connection successful! {test}"}