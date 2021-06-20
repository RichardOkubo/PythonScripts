from pprint import pprint

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine("sqlite:///test.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Produto(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    pessoa_id = Column(Integer, ForeignKey("pessoas.id"))
    pessoa = relationship("Pessoa")

    def __repr__(self):
        return f"Produto(id={self.id}, nome={self.nome}, pessoa={self.pessoa})"


class Pessoa(Base):
    __tablename__ = "pessoas"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)
    produtos = relationship(Produto, backref="pessoas")

    def __repr__(self):
        return f"Pessoa(id={self.id}, nome={self.nome}, idade={self.idade}, " \
            f"produtos={[produto.nome for produto in self.produtos]})"


Base.metadata.create_all(engine)


#p1 = Pessoa(nome="Richard", idade="24")
#p2 = Pessoa(nome="Xpto", idade="99")
#pd1 = Produto(nome="Livro", pessoa=p1)
#pd2 = Produto(nome="CD", pessoa=p1)
#pd3 = Produto(nome="CD", pessoa=p2)

#session.add_all([pd1, pd2, p1, p2, pd3])

#session.commit()

pprint(
    session.query(Pessoa) \
        .filter(Pessoa.nome == 'Richard') \
        .first()
)

pprint(
    session.query(Produto) \
        .filter_by(nome='CD') \
        .filter(Pessoa.nome == 'Richard') \
        .all()
)
