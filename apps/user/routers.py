from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from apps.user import crud, schemas

router = APIRouter()


@router.post("/", response_model=schemas.UserList)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


@router.get("/", response_model=list[schemas.UserList])
def get_user(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_user(db=db, skip=skip, limit=limit)


@router.put("/{user_id}", response_model=schemas.UserList)
def update_user(
    category_id: int,
    name: str,
    address: str,
    phone_number: str,
    db: Session = Depends(get_db),
):
    updated_user = crud.update_user(db, category_id, name, address, phone_number)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user


@router.delete("/{user_id}", response_model=schemas.User)
def delete_user(category_id: int, db: Session = Depends(get_db)):
    deleted_user = crud.delete_user(db, category_id)
    if not deleted_user:
        raise HTTPException(status_code=404, detail="User not found")
    return deleted_user


@router.post("/user_reports/", response_model=schemas.UserReport)
def create_user_report(user_id: int, name: str, db: Session = Depends(get_db)):
    return crud.create_user_report(db=db, user_id=user_id, name=name)


@router.get("/user_reports/", response_model=schemas.UserReport)
def get_user_report(
    user_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return crud.get_user_report(db=db, skip=skip, limit=limit)


@router.post("/user_tests/")
def create_user_test(user_report_id: int, name: str, db: Session = Depends(get_db)):
    return crud.create_user_test(db=db, user_report_id=user_report_id, name=name)
