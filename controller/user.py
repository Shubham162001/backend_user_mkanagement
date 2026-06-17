from sqlalchemy import text
from models.db_models import Employee, EmployeeDetails


def get_user_info_details(user):
    
    return {'message': f'Name is user is {user.name}, age is {user.age}, email is {user.email}, phone is {user.phone}'}


def add_user(employee, db):
    try:
        email_check_query = "SELECT * FROM employee WHERE TRIM(email) = :email"
        email = employee.email.strip()

        email_result = db.execute(
            text(email_check_query),
            {"email": email}
        ).fetchone()

        print("Email result =", email_result)

        if email_result:
            return {
                "message": "Email already exists"
            }
        
        query = """
        INSERT INTO employee
        (first_name, last_name, age, mobile, salary, post, email)
        VALUES
        (:first_name, :last_name, :age, :mobile, :salary, :post, :email)
        """

        params = {
            "first_name": employee.first_name,
            "last_name": employee.last_name,
            "age": employee.age,
            "mobile": employee.mobile,
            "salary": employee.salary,
            "post": employee.post,
            "email": employee.email
        }
        
        result = db.execute(
            text(query),
            params=params
        )

        emp_id = result.lastrowid
        print("Generated ID:", emp_id)

        details_query = """
        INSERT INTO employee_details
        (emp_id, emp_address, emp_college)
        VALUES
        (:emp_id, :emp_address, :emp_college)
        """

        details_params = {
            "emp_id": emp_id,
            "emp_address": employee.emp_address,
            "emp_college": employee.emp_college
        }

        db.execute(
            text(details_query),
            details_params
        )

        db.commit()

        return {
            "message": "Employee added successfully",
            "employee_id": emp_id
        }

    except Exception as e:
        db.rollback()
        return {
            "message": f"Error occurred: {str(e)}"
        }


def get_user_info(user_id, db):
    try:
        query = "SELECT * FROM employee WHERE id = :user_id"
        result = db.execute(text(query), {"user_id": user_id}).fetchone()
        if result:
            user_info = dict(result._mapping)
            return user_info
        else:
            return None
    except Exception as e:
        raise e
    
def update_user(user_id, employee, db):
    try:
        query = """
        UPDATE employee 
        SET first_name = :first_name, 
        last_name = :last_name,
         age = :age, 
         mobile = :mobile, 
         salary = :salary, 
         post = :post,
         email = :email
         where id = :user_id"""
        
        params = {
            "user_id":user_id,
            "first_name":employee.first_name,
            "last_name":employee.last_name,
            "age":employee.age,
            "mobile":employee.mobile,
            "salary":employee.salary,
            "post":employee.post,
            "email":employee.email
        }
        db.execute(text(query), params=params)
        db.commit()

        return{"message": "Employee updated successfully"}
    
    except Exception as e:
        return{"message": f"Error occurred: {str(e)}"}
    

def get_all_users(db):
    try:
        query = "SELECT * FROM employee"
        result = db.execute(text(query)).fetchall()
        users = [dict(row._mapping) for row in result]

        return users

    except Exception as e:
        return {"message": f"Error occurred: {str(e)}"}
    
def delete_employee(emp_id, db):
    try:
        employee_Details = db.query(EmployeeDetails).filter(
            EmployeeDetails.emp_id == emp_id).first()
        
        if employee_Details:
                
                db.delete(employee_Details)
                db.commit()

        employee = db.query(Employee).filter(Employee.id == emp_id).first()

        if not employee:
            return {"message": f"Employee with id {emp_id} not found."}
        
        db.delete(employee)
        db.commit()

        return {"message": "Employee deleted successfully."}
    
    except Exception as e:
        db.rollback()
        return {"message": f"Error occurred: {str(e)}"}
                
        