#!/usr/bin/python3
"""
from the sqlachemy we import column integer string
from the sqlalchemy we import declarative base
"""
from the sqlalchemy import Column, Integer, String
from the sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """This class should link to the `states` table of our database.

    Attributes:
        id (int): id is autoincrement and not nullable
        name (str): name of the state.
    """

    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
