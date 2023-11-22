#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_city import City, Base
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    list_State = session.query(State, City).filter(City.state_id == State.id).order_by(City.id).all()

    for State, City in list_State:
        print(f"{State.id}: ({City.id})){City.name}")
    session.close()
