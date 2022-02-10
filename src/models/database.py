from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, Boolean
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

from defaults import DATABASE_URL

Base = declarative_base()


class Payment(Base):
    __tablename__ = 'payment'
    id = Column(Integer, primary_key=True)
    last_payment = Column(DateTime, default=datetime.now())
    has_sent_email = Column(Boolean, default=False)


class Database():
    TABLES_HOOK = {
        'PAYMENT': Payment,
    }

    def _database_is_empty(
        self,
        session: sessionmaker
    ) -> bool:
        query = session.execute(
            ('SELECT CASE WHEN EXISTS(SELECT 1 FROM payment)'
             'THEN 0 ELSE 1 END;'))
        if query.one()[0] == 1:
            return True
        return False

    def _insert_data(
        self,
        session: sessionmaker
    ) -> None:
        # TODO: pydantic serializer
        first_payment = self.TABLES_HOOK.get('PAYMENT')(
            id=None,
            last_payment=None,
            has_sent_email=None,)
        session.add(first_payment)
        session.commit()

    def connect_db(self) -> sessionmaker:
        engine = create_engine(DATABASE_URL)
        if not database_exists(engine.url):
            create_database(engine.url)
        session = sessionmaker()
        session.configure(bind=engine)
        _session = session()
        Base.metadata.create_all(engine)
        if self._database_is_empty(_session):
            self._insert_data(_session)
        return _session
