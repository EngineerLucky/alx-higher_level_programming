#!/usr/bin/python3
"""
This function lists all State objects and corresponding City objects contained in the DB
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    u_name = sys.argv[1]
    u_pass = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(u_name, u_pass, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    st = session.query(State).outerjoin(City).order_by(State.id, City.id).all()

    for state in st:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
