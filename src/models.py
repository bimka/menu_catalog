import uuid

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Float, select, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, declarative_base, backref, column_property

from src.session import Base, engine


class Menu(Base):
    __tablename__ = "menus"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, unique=True)
    description = Column(String)
    submenus_count = Column(Integer, default=0)
    dishes_count = Column(Integer, default=0)

    # submenus = relationship("Submenu",
    #                         back_populates="menu",
    #                         cascade="all, delete")


class Dish(Base):
    __tablename__ = "dishes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, unique=True)
    description = Column(String)
    price = Column(Float, index=True)
    submenu_id = Column(UUID(as_uuid=True), ForeignKey("submenus.id"))

    submenu = relationship('Submenu', back_populates='dishes')


class Submenu(Base):
    __tablename__ = "submenus"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, unique=True)
    description = Column(String)

    # menu_id = Column(UUID(as_uuid=True), ForeignKey("menus.id"))

    # menu = relationship("Menu", back_populates="submenus")
    dishes_count = column_property(
        select(func.count(Dish.id))
        .where(Dish.submenu_id == id)
        .correlate_except(Dish)
        .scalar_subquery()
    )
    dishes = relationship("Dish",
                          back_populates='submenu',
                          cascade="all,delete", passive_deletes=True)

# Submenu.dishes = relationship("Dish", order_by=Dish.id, back_populates="submenu")

Base.metadata.create_all(engine)
