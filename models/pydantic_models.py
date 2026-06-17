from pydantic import BaseModel
from typing import Optional
class UserClass(BaseModel):
    name: str
    age: int
    email: str
    phone: int

class Employee(BaseModel):
    first_name: str
    last_name: str
    age: int
    mobile: int
    salary: int
    post: str
    email: Optional[str]

    emp_address: str
    emp_college: str

class EmployeeVerify(BaseModel):
    age: int
    mobile: int