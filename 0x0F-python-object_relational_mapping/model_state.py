#!/usr/bin/python3
"""Definition of the State class"""
from sqlalchemy import Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State (Base):
    """class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                nullable=False, unique=True)
    name = Column(String(128), ForeignKey('states.id'), nullable=False)
