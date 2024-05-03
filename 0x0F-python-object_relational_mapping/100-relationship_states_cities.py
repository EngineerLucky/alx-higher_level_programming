#!/usr/bin/python3
"""
The function creates the State "California" with the City "San Francisco" from a DB
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# This script does not execute when imported.
if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    n_State = State(name='California')
    n_city = City(name='San Francisco')
    n_State.cities.append(n_city)
    session.add(n_State)
    session.add(n_city)
    session.commit()
