from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from apps.report import crud, schemas

router = APIRouter()


@router.post("/", response_model=schemas.CategoryCreate)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db=db, category=category)


@router.get("/", response_model=list[schemas.Category])
def get_category(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_category(db=db, skip=skip, limit=limit)


@router.put("/{category_id}", response_model=schemas.Category)
def update_category(
    category_id: int,
    name: str,
    description: str,
    db: Session = Depends(get_db),
):
    updated_category = crud.update_category(db, category_id, name, description)
    if not updated_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return updated_category


@router.delete("/{category_id}", response_model=schemas.Category)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    deleted_category = crud.delete_category(db, category_id)
    if not deleted_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return deleted_category


@router.post("/{category_id}/test", response_model=schemas.TestCreate)
def create_test(category_id, test: schemas.TestCreate, db: Session = Depends(get_db)):
    test = crud.create_test(db=db, test=test, category_id=category_id)
    if not test:
        raise HTTPException(status_code=400, detail="Category not found")

    return test


@router.get("/{category_id}/test", response_model=list[schemas.Test])
def get_test(
    category_id, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return crud.get_test(db=db, category_id=category_id, skip=skip, limit=limit)


@router.put("/{category_id}", response_model=schemas.Category)
def update_category(
    category_id: int,
    name: str,
    description: str,
    db: Session = Depends(get_db),
):
    updated_category = crud.update_category(db, category_id, name, description)
    if not updated_category:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_category


@router.delete("/{category_id}", response_model=schemas.Category)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    deleted_category = crud.delete_category(db, category_id)
    if not deleted_category:
        raise HTTPException(status_code=404, detail="User not found")
    return deleted_category
