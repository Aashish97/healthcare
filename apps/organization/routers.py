from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from apps.organization import crud, schemas
from core.database import SessionLocal, get_db

router = APIRouter()


@router.post("/", response_model=schemas.Organization)
def create_organization(
    organization: schemas.OrganizationCreate, db: Session = Depends(get_db)
):
    return crud.create_organization(db=db, organization=organization)


@router.get("/", response_model=list[schemas.Organization])
def get_organizations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_organizations(db=db, skip=skip, limit=limit)


@router.put("/{org_id}", response_model=schemas.Organization)
def update_organization(
    org_id: int,
    name: str,
    address: str,
    phone_number: str,
    db: Session = Depends(get_db),
):
    updated_org = crud.update_organization(db, org_id, name, address, phone_number)
    if not updated_org:
        raise HTTPException(status_code=404, detail="Organization not found")
    return updated_org


@router.delete("/{org_id}", response_model=schemas.Organization)
def delete_organization(org_id: int, db: Session = Depends(get_db)):
    deleted_org = crud.delete_organization(db, org_id)
    if not deleted_org:
        raise HTTPException(status_code=404, detail="Organization not found")
    return deleted_org
