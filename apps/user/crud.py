from sqlalchemy.orm import Session
from apps.user import models, schemas


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        first_name=user.first_name,
        last_name=user.last_name,
        address=user.address,
        age=user.age,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()


def update_user(
    db: Session,
    user_id: int,
    first_name: str,
    last_name: str,
    address: str,
    age: int,
):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()

    if db_user:
        db_user.first_name = first_name
        db_user.last_name = last_name
        db_user.address = address
        db_user.age = age

        db.commit()
        db.refresh(db_user)  # Refresh the instance to reflect changes
        return db_user
    return None


def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()

    if db_user:
        db.delete(db_user)
        db.commit()
        return db_user
    return None


def create_user_report(db: Session, user_id: int, name: str):
    db_user_report = models.UserReport(name=name, user_id=user_id)
    db.add(db_user_report)
    db.commit()
    db.refresh(db_user_report)
    return db_user_report


def get_user_report(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    return (
        db.query(models.User)
        .filter(models.User.id == user_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_user_test(db: Session, user_report_id: int, name: str):
    db_user_test = models.UserTest(name=name, user_report_id=user_report_id)
    db.add(db_user_test)
    db.commit()
    db.refresh(db_user_test)
    return db_user_test
