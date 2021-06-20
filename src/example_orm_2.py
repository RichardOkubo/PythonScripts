from pprint import pprint

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
    idade = Column(Integer)

    def __repr__(self):
        return f'Pessoa(nome={self.nome}, idade={self.idade})'


Base.metadata.create_all(engine)

#xpto1 = Pessoa(nome='xpto_1', idade=26)
#xpto2 = Pessoa(nome='xpto_2', idade=30)
#xpto3 = Pessoa(nome='xpto_3', idade=36)

#session.add_all([xpto1, xpto2, xpto3])

#session.commit()

#pprint(session.query(Pessoa).first())
pprint(session.query(Pessoa).all())
