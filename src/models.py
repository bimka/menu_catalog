import uuid

from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID

from src.session import Base

"""
menus = Table(
    "menus", 
    metadata, 
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4), 
    Column("title", String, unique=True), 
    Column("description", String, index=True),
    Column("submenus_count", Integer, default=0),
    Column("dishes_count", Integer, default=0)
)

"""
class Menu(Base):
    __tablename__ = "menus"
    #metadata = MetaData()

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, unique=True)
    description = Column(String)
    submenus_count = Column(Integer, default=0)
    dishes_count = Column(Integer, default=0)

    # submenus = relationship("Submenu", back_populates="menus")


# class Submenu(Base):
#     __tablename__ = "submenus"
#     #metadata = MetaData(bind=engine)
#
#     id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     title = Column(String, unique=True)
#     description = Column(String)
#     menu_id = Column(Integer, ForeignKey("menu.id"))

    # foods = relationship("Food", back_populates="submenus")

"""
class Food(Submenu):
    __tablename__ = "foods"

    id = Column(Integer, primary_key=True, integer=True)
    name = Column(Integer, unique=True, index=True)
    price = Column(Float, index=True)
    submenu_id = Column(Integer, ForeignKey("submenu.id"))"""