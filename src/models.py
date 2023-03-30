import uuid

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.session import Base


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

    menu = relationship("Menu", back_populates="submenus")
    # foods = relationship("Food", back_populates="submenu")


"""
class Food(Submenu):
    __tablename__ = "foods"

    id = Column(Integer, primary_key=True, integer=True)
    name = Column(Integer, unique=True, index=True)
    price = Column(Float, index=True)
    submenu_id = Column(Integer, ForeignKey("submenu.id"))"""