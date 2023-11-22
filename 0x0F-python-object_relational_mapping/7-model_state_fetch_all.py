# #!/usr/bin/python3
# """Start link class to table in database
# """
# import sys
# from model_state import Base, State
# from sqlalchemy import (create_engine)
# from sqlalchemy.orm import sessionmaker

# if __name__ == "__main__":
#     engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
#                            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
#                            pool_pre_ping=True)
#     Base.metadata.create_all(engine)
#     Session = sessionmaker(bind=engine)
#     session = Session()

#     list_State = session.query(State).order_by(State.id).all()

#     for instance in list_State:
#         print(f"{instance.id}:  {instance.name}")
#     session.close()
#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sys import argv

    if (len(argv) != 4):
        print('Use: username, password database_name')
        exit(1)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id)

    for row in states:
        print(f'{row.id}: {row.name}')
    session.close()