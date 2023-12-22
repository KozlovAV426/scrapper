
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Repository:
    def __init__(self, connection_url):
        self.engine = create_engine(connection_url)
        self.engine.connect()
        self.session_maker = sessionmaker(bind=self.engine)

    def insert(self, item):
        session = self.session_maker()
        session.add(item)
        session.commit()
        session.close()




