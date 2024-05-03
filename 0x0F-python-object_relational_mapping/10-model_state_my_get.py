#!/usr/bin/python3
"""
The script should print the `State` object in `hbtn_0e_0_usa`
where `name` matches the argument `state name to search`.

Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
    state name to search (str)
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    mySql_u = sys.argv[1]
    mySql_p = sys.argv[2]
    db_name = sys.argv[3]

    sta_name = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(mySql_u, mySql_p, db_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == sta_name).first()
    print("Not found" if not state else state.id)
