# coding: utf-8
from sqlalchemy import CheckConstraint, Column, DateTime, ForeignKey, Integer, Numeric, String, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, server_default=text("nextval('users_id_seq'::regclass)"))
    login = Column(String(32), unique=True)
    password = Column(String(32))


class Augmentation(Base):
    __tablename__ = 'augmentations'
    __table_args__ = (
        CheckConstraint('(angle_rotation >= 0) AND (angle_rotation <= 45)'),
        CheckConstraint("(brightness >= '-255'::integer) AND (brightness <= 255)"),
        CheckConstraint('(contrast >= 0.5) AND (contrast <= 1.5)'),
        CheckConstraint('(noise >= 0) AND (noise <= 50)'),
        CheckConstraint('(percentage_generation >= 5) AND (percentage_generation <= 50)')
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('augmentations_id_seq'::regclass)"))
    user_id = Column(ForeignKey('users.id', ondelete='CASCADE'))
    percentage_generation = Column(Integer)
    angle_rotation = Column(Integer)
    noise = Column(Integer)
    contrast = Column(Numeric)
    brightness = Column(Integer)
    datetime = Column(DateTime)

    user = relationship('User')