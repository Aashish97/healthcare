from sqlalchemy.orm import Session
from apps.report import models, schemas


def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(name=category.name, description=category.description)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def get_category(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Category).offset(skip).limit(limit).all()


def update_category(db: Session, category_id: int, name: str, description: str):
    db_category = (
        db.query(models.Category).filter(models.Category.id == category_id).first()
    )

    if db_category:
        db_category.name = name
        db_category.description = description

        db.commit()
        db.refresh(db_category)  # Refresh the instance to reflect changes
        return db_category
    return None


def delete_category(db: Session, category_id: int):
    db_category = (
        db.query(models.Category).filter(models.Category.id == category_id).first()
    )

    if db_category:
        db.delete(db_category)
        db.commit()
        return db_category
    return None


def create_test(db: Session, test: schemas.TestCreate, category_id: int):
    db_category = (
        db.query(models.Category).filter(models.Category.id == category_id).first()
    )

    if not db_category:
        return None

    db_test = models.Test(
        name=test.name,
        description=test.description,
        code=test.code,
        unit=test.unit,
        reference_range=test.reference_range,
    )
    db.add(db_test)
    db.commit()
    db.refresh(db_test)
    return db_test


def get_test(db: Session, category_id: int, skip: int = 0, limit: int = 10):
    return (
        db.query(models.Test)
        .filter(models.Category.id == category_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


def update_category(db: Session, category_id: int, name: str, description: str):
    db_category = (
        db.query(models.Category).filter(models.Category.id == category_id).first()
    )

    if db_category:
        db_category.name = name
        db_category.description = description

        db.commit()
        db.refresh(db_category)  # Refresh the instance to reflect changes
        return db_category
    return None


def delete_category(db: Session, category_id: int):
    db_category = (
        db.query(models.Category).filter(models.Category.id == category_id).first()
    )

    if db_category:
        db.delete(db_category)
        db.commit()
        return db_category
    return None
