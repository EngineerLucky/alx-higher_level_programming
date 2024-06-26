#!/usr/bin/python3
"""
The function changes the name of a State in the database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    s_Updated = session.query(State).filter(State.id == 2).first()

    if s_Updated:
        s_Updated.name = 'New Mexico'
        session.commit()
