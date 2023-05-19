import uuid

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, declarative_base

from .session import engine

Base = declarative_base()


class Menu(Base):
    __tablename__ = "menus"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, unique=True)
    description = Column(String)
    submenus_count = Column(Integer, default=0)
    dishes_count = Column(Integer, default=0)

    submenus = relationship(
        "Submenu", back_populates="menu", passive_deletes=True
    )
    dishes = relationship("Dish", back_populates="menu", passive_deletes=True)


class Submenu(Base):
    __tablename__ = "submenus"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, unique=True)
    description = Column(String)
    dishes_count = Column(Integer, default=0)
    menu_id = Column(
        UUID(as_uuid=True),
        ForeignKey("menus.id", ondelete="CASCADE"),
        nullable=False,
    )

    menu = relationship("Menu", back_populates="submenus")
    dishes = relationship(
        "Dish", back_populates="submenu", passive_deletes=True
    )


class Dish(Base):
    __tablename__ = "dishes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, unique=True)
    description = Column(String)
    price = Column(String, index=True)
    menu_id = Column(
        UUID(as_uuid=True),
        ForeignKey("menus.id", ondelete="CASCADE"),
        nullable=False,
    )
    submenu_id = Column(
        UUID(as_uuid=True),
        ForeignKey("submenus.id", ondelete="CASCADE"),
        nullable=False,
    )

    menu = relationship("Menu", back_populates="dishes")
    submenu = relationship("Submenu", back_populates="dishes")


Base.metadata.create_all(engine)
