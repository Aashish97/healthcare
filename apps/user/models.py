from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from core.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    address = Column(String)
    age = Column(Integer)

    user_reports = relationship("UserReport", back_populates="user")


class UserReport(Base):
    __tablename__ = "user_reports"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))  # Changed to Integer type
    user = relationship("User", back_populates="user_reports")

    # Relationship to UserTest
    user_tests = relationship("UserTest", back_populates="report")


class UserTest(Base):
    __tablename__ = "user_tests"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    user_report_id = Column(
        Integer, ForeignKey("user_reports.id")
    )  # Changed to Integer type

    # Relationship to UserReport
    report = relationship("UserReport", back_populates="user_tests")
