import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy import create_engine
import datetime

Base = declarative_base()

association_table = Table('signups', Base.metadata,
    Column('person_id', Integer, ForeignKey('person.id')),
    Column('event_id', Integer, ForeignKey('event.id'))
)

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    events = relationship(
        "Event",
        secondary=association_table,
        back_populates="signups")

    def __repr__(self):
        return self.name


class Event(Base):
    __tablename__ = 'event'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    description = Column(String(250))
    date = Column(DateTime, nullable=False)
    created_by_id = Column(Integer, ForeignKey('person.id'))
    created_by = relationship(Person)
    likes = Column(Integer, nullable=False, default=0)
    signups = relationship(
        "Person",
        secondary=association_table,
        back_populates="events")

    def __repr__(self):
        return 'Title: {0}, Date: {1}, Created by: {2}'.format(self.title, self.date, self.created_by)




# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///events/events.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
