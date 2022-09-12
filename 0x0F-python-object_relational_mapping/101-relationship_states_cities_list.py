#!/usr/bin/python3
""" script that lists all State objects, and corresponding
    City objects, contained in the database hbtn_0e_101_usa
"""

if __name__ == '__main__':
    # Standard Library imports
    import sys

    # related third party imports
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    # local application imports
    from relationship_state import Base, State
    from relationship_city import City

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()
    i = 1
    for count, state in enumerate(states):
        print("{}: {}".format(count + 1, state.name))
        for city in state.cities:
            print("    {}: {}".format(i, city.name))
            i = i + 1
