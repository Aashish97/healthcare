from pydantic import BaseModel
from typing import List, Optional


# User schema
class UserBase(BaseModel):
    first_name: str
    last_name: str
    age: int
    address: str


class UserCreate(UserBase):
    pass


class UserList(UserBase):
    pass


class User(UserBase):
    id: int
    user_reports: List["UserReport"] = (
        []
    )  # This will be filled with related user reports

    class Config:
        from_attributes = True


# UserReport schema
class UserReportBase(BaseModel):
    name: str
    user_id: int  # The user who created the report


class UserReportCreate(UserReportBase):
    pass


class UserReport(UserReportBase):
    id: int
    user_tests: List["UserTest"] = []  # This will be filled with related user tests

    class Config:
        from_attributes = True


# UserTest schema
class UserTestBase(BaseModel):
    name: str
    user_report_id: int  # The report associated with this test


class UserTestCreate(UserTestBase):
    pass


class UserTest(UserTestBase):
    id: int

    class Config:
        from_attributes = True
