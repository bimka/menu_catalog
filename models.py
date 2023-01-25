import uuid

from sqlalchemy import Column, ForeignKey, Integer, Float, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from database import Base

class Menu(Base):
    __tablename__ = "menus"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    title = Column(String, unique=True, index=True)
    description = Column(String, index=True)

"""    submenus = relationship("Submenu", back_populates="menus")


class Submenu(Menu):
    __tablename__ = "submenus"

    id = Column(Integer, primary_key=True, integer=True)
    name = Column(String, unique=True, index=True)
    menu_id = Column(Integer, ForeignKey("menu.id"))

    foods = relationship("Food", back_populates="submenus")


class Food(Submenu):
    __tablename__ = "foods"

    id = Column(Integer, primary_key=True, integer=True)
    name = Column(Integer, unique=True, index=True)
    price = Column(Float, index=True)
    submenu_id = Column(Integer, ForeignKey("submenu.id"))"""