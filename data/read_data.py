from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from create_tables import Base, PlatformType, DataType, Reactor, RecipeType, Category, SampleStock, SampleData

if __name__ == '__main__':

    engine = create_engine('sqlite:///data.db') #
    Session = sessionmaker(bind=engine)
    session = Session()

    #read all platform types and reactor link to them
    query_result = session.query(PlatformType, Reactor).join(Reactor).all()

    print('List of platform types:')
    for platform_type, reactor in query_result:
        print(f"Réacteur ID: {reactor.id} | Nom: {reactor.name} | Type de plateforme: {platform_type.name}")
