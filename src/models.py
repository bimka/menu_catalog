import uuid

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.session import Base, engine


class Menu(Base):
    __tablename__ = "menus"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, unique=True)
    description = Column(String)
    submenus_count = Column(Integer, default=0)
    dishes_count = Column(Integer, default=0)


class Submenu(Base):
    __tablename__ = "submenu"

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    description = Column(String)
    dishes_count = Column(Integer, default=0)
    menu_id = Column(ForeignKey("menus.id"), nullable=False)

    menu = relationship("Menu", backref="submenus", cascade="all,delete")
    dishes = relationship("Dish", back_populates="submenu", passive_deletes=True)


class Dish(Base):
    __tablename__ = "dish"

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    description = Column(String)
    price = Column(String, index=True)
    # menu_id = Column(ForeignKey("menus.id"), nullable=False)
    # submenu_id = Column(ForeignKey("submenus.id"), nullable=False)
    #
    # menu = relationship("Menu", backref="dishes")
    # submenu = relationship("Submenu", backref="dishes", cascade="all,delete")
    submenu_id = Column(Integer,
                        ForeignKey("submenu.id", ondelete="CASCADE"),
                        nullable=False)
    submenu = relationship("Submenu", back_populates="dishes")


Base.metadata.create_all(engine)
