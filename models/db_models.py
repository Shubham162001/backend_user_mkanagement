from sqlalchemy import Column, Integer, String, Float, ForeignKey
from db_utils.database import Base
class Employee(Base):

    __tablename__ = 'employee'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    mobile = Column(Integer, nullable=False)
    salary = Column(Float, nullable=False)
    post = Column(String(50), nullable=False)
    email = Column(String(100), nullable=True)

class EmployeeDetails(Base):
    __tablename__ = 'employee_details'
    
    
    emp_id = Column(Integer, ForeignKey('employee.id'), primary_key=True)
    emp_address = Column(String(200), nullable=False)
    emp_college = Column(String(100), nullable=False)