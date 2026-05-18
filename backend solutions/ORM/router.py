from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Employee
router=APIRouter()
@router.post("/details")
def add_details(name:str,department:str,salary:float,db:Session=Depends(get_db)):
    data=Employee(name=name,department=department,salary=salary)
    db.add(data)
    db.commit()
    db.refresh(data)
    return{"message":"Details added successfully","Data":data.id}
@router.get("/employees")
def get_details(db:Session=Depends(get_db)):
    details=db.query(Employee).all()
    return details
@router.get("/employees/{id}")
def getby_id(id:int,db:Session=Depends(get_db)):
    detail=db.query(Employee).filter(Employee.id==id).first()
    return detail
@router.get("/employee/{department}")
def getby_dept(department:str,db:Session=Depends(get_db)):
    detail=db.query(Employee).filter(Employee.department==department).all()
    return detail
@router.put("/update_details/{id}")
def update_details(id:int,name:str,dept:str,db:Session=Depends(get_db)):
    detail=db.query(Employee).filter(Employee.id==id).first()
    detail.name=name
    detail.department=dept
    db.commit()
    return {
        "message": "Updated successfully"
    }
