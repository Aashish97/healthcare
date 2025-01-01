from sqlalchemy.orm import Session
from . import models, schemas


def create_organization(db: Session, organization: schemas.OrganizationCreate):
    db_organization = models.Organization(
        name=organization.name,
        address=organization.address,
        phone_number=organization.phone_number,
    )
    db.add(db_organization)
    db.commit()
    db.refresh(db_organization)
    return db_organization


def get_organizations(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Organization).offset(skip).limit(limit).all()


def update_organization(
    db: Session, org_id: int, name: str, address: str, phone_number: str
):
    # Find the organization by ID
    db_org = (
        db.query(models.Organization).filter(models.Organization.id == org_id).first()
    )

    if db_org:
        db_org.name = name
        db_org.address = address
        db_org.phone_number = phone_number

        db.commit()
        db.refresh(db_org)  # Refresh the instance to reflect changes
        return db_org
    return None


def delete_organization(db: Session, org_id: int):
    db_org = (
        db.query(models.Organization).filter(models.Organization.id == org_id).first()
    )

    if db_org:
        db.delete(db_org)
        db.commit()
        return db_org
    return None
