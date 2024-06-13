from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from create_tables import Base, PlatformType, DataType, Reactor, RecipeType, Category, SampleStock, SampleData

if __name__ == '__main__':

    engine = create_engine('sqlite:///data.db') #
    Session = sessionmaker(bind=engine)
    session = Session()

    # add data
    # #create reactor link to Platform A
    reactor_A = Reactor(name='Reactor A', platform_type_id=1)
    session.add(reactor_A)
    # #create reactor link to Platform B
    reactor_PTB = Reactor(name='Reactor B', platform_type_id=2)
    session.add(reactor_PTB)

    #--------
    # Validation and commit change to database
    session.commit()