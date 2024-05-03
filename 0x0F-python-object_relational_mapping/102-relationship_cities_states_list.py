#!/usr/bin/python3
"""
The function lists all City objects from the database hbtn_0e_101_usa
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

    Session = sessionmaker(bind=engine)
    session = Session()

    st = session.query(State).join(City).order_by(City.id).all()

    for state in st:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
