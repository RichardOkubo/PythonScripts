from sqlalchemy import create_engine, engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///test.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Pessoa(Base):
    __tablename__ = "pessoas"

    id = Column(Integer, primary_key=True)
    nome = Column(String)


Base.metadata.create_all(engine)

p1 = Pessoa(nome='pessoa1')
p2 = Pessoa(nome='pessoa2')
p3 = Pessoa(nome='pessoa3')
p4 = Pessoa(nome='pessoa4')
p5 = Pessoa(nome='pessoa5')

session.add(p1)
session.add_all([p2, p3, p4])

session.commit()  # Persists in the database

session.add(p5)
session.flush()  # Clears the session
