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
"""Start link class to table in the database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(sys.argv[1], sys.argv[2], sys.argv[3]))
        Base = declarative_base(bind=engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        list_State = session.query(State).order_by(State.id).all()

        if not list_State:
            print("No records found.")
        else:
            for instance in list_State:
                print(f"{instance.id}:  {instance.name}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()
