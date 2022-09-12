#!/usr/bin/python3
""" script that prints all City objects
   from the database hbtn_0e_14_usa
"""

if __name__ == '__main__':
    # Standard Library imports
    import sys

    # related third party imports
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    # local application imports
    from model_state import Base, State
    from model_city import City

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    allcities = session.query(State, City).join(City).order_by(City.id).all()

    for state, city in allcities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
