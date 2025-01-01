from pydantic import BaseModel


class OrganizationBase(BaseModel):
    name: str
    address: str
    phone_number: str


class OrganizationCreate(OrganizationBase):
    pass


class Organization(OrganizationBase):
    id: int

    class Config:
        from_attributes = True
