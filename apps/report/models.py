from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from core.database import Base


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    description = Column(String)

    tests = relationship("Test", back_populates="category")


class Test(Base):
    __tablename__ = "tests"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    description = Column(String)

    code = Column(String)
    unit = Column(String, nullable=True)
    reference_range = Column(String, nullable=True)

    category_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship("Category", back_populates="tests")
