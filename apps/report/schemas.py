from pydantic import BaseModel
from typing import List, Optional


class CategoryBase(BaseModel):
    name: str
    description: Optional[str]


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int
    tests: List["Test"] = []

    class Config:
        from_attributes = True


class TestBase(BaseModel):
    name: str
    description: Optional[str]

    code: Optional[str]
    unit: Optional[str]
    reference_range: Optional[str]


class TestCreate(TestBase):
    pass


class Test(TestBase):
    id: int

    class Config:
        from_attributes = True
