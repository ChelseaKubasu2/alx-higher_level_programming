#!/usr/bin/python3
""" script that prints the State object with the name passed
    as argument from the database hbtn_0e_6_usa
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

    ui = sys.argv[4].split("'")  # ui = user input
    ni = ui[0]  # ni = new input
    onestate = session.query(State)\
                      .filter(State.name == ni)\
                      .first()
    if onestate:
        print("{}".format(onestate.id))
    else:
        print("Not found")
