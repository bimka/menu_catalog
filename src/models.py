import uuid

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:postgres@0.0.0.0:5432/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()


class Menu(Base):
    __tablename__ = "menus"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, unique=True)
    description = Column(String)
    submenus_count = Column(Integer, default=0)
    dishes_count = Column(Integer, default=0)

    submenus = relationship("Submenu",
                            back_populates="menu",
                            cascade="all, delete")


class Submenu(Base):
    __tablename__ = "submenus"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, unique=True)
    description = Column(String)
    dishes_count = Column(Integer, default=0)
    menu_id = Column(UUID(as_uuid=True), ForeignKey("menus.id"))

    menu = relationship("Menu", back_populates="submenus")
    # foods = relationship("Food", back_populates="submenu")


"""
class Food(Submenu):
    __tablename__ = "foods"

    id = Column(Integer, primary_key=True, integer=True)
    name = Column(Integer, unique=True, index=True)
    price = Column(Float, index=True)
    submenu_id = Column(Integer, ForeignKey("submenu.id"))"""

Base.metadata.create_all(engine)