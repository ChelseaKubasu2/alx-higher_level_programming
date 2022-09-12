#!/usr/bin/python3
""" script that lists all State objects that contain the
    letter a from the database hbtn_0e_6_usa
"""

if __name__ == '__main__':
    # Standard Library imports
    import sys

    # related third party imports
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    # local application imports
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State)\
                    .filter(State.name.like('%a%'))\
                    .order_by(State.id)

    for state in states:
        print("{}: {}".format(state.id, state.name))
