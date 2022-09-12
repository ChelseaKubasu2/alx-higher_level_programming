#!/usr/bin/python3
""" module that contains the class definition of a City and an instance
"""

# related third party imports
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey

# local application imports
from model_state import Base


class City(Base):
    """ City class:
                inherits from Base (imported from model_state)
                links to the MySQL table cities
                class attribute id that represents a column of
                an auto-generated, unique integer, can’t be null and
                is a primary key class attribute name that represents
                a column of a string with maximum 128 characters
                and can’t be null
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
