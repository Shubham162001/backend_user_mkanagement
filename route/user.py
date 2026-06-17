from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from db_utils.get_db import get_db
from controller.user import add_user,get_user_info, update_user, get_all_users, delete_employee
from fastapi import HTTPException
from models.pydantic_models import Employee,EmployeeVerify

user_router = APIRouter()
    

@user_router.post("/add_employee")
def add_employee(
    employee: Employee,
    db: Session = Depends(get_db)
):
    try:
        result = add_user(employee, db)
        return result
    except Exception as e:
        return {"message": f"Error occurred: {str(e)}"}
    
@user_router.post("/verify_employee")
def verify_employee(
    emp: EmployeeVerify):
    if emp.age < 18:
       raise HTTPException(status_code=400, detail="Employee must be at least 18 years old.")
    return{
        "status": "Verified",
        "message": "Employee eligible"
    }


@user_router.get("/get_user_by_id/{user_id}")
def get_user_by_id(
    user_id: int,
    db: Session = Depends(get_db)
):
    try:
        result = get_user_info(user_id, db)
        if result:

            
            return {"message": result}
        else:
            return {"message": f"User with id {user_id} not found.", "status_code": 404}
    except Exception as e:
        return {"message": f"Error occurred: {str(e)}", "status_code": 500}
    
@user_router.put("/update_user/{user_id}")
def update_employee(
    user_id: int,
    employee: Employee,
    db: Session = Depends(get_db)
):
    try:
        result = update_user(user_id, employee, db)
        return result
    except Exception as e:
        return {"message": f"Error occurred: {str(e)}"}
    
    
@user_router.get("/get_users")
def get_users(db: Session = Depends(get_db)):
    try:
        result = get_all_users(db)
        return {"message": result}
    except Exception as e:
        return {"message": f"Error occurred: {str(e)}"}
    
@user_router.delete("/delete_emloyee/{emp_id}")
def delete_employee_route(
    emp_id: int,
    db: Session = Depends(get_db)
):
    try:
        result = delete_employee(emp_id, db)
        return result
    except Exception as e:
        return {"message": "Error occured: {str(e)}"}



## Delete API which will delete all the data for given user id from bth employee and employee_address table try using SQL Alchemy Models dont use Simple SQL query
    
## Add Employe API : And if Similar Email ID is passed then it should return the message that email id is already exist and it should not add the data to database.