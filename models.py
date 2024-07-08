from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, declarative_base, relationship, sessionmaker

dbl_url = "sqlite:///database.db"

engine = create_engine(dbl_url)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__        = "users"
    __allow_unmapped__  = True

    id = Column(Integer, primary_key=True)

    username = Column(String)

    following_id = Column(Integer, ForeignKey('users.id'))
    following = relationship('User', remote_side=[id], uselist=True)

    def __repr__ (self):
        return f"<User(id={self.id}, Username='{self.username}, following={self.following}')>"
        
Base.metadata.create_all(engine)




'''
class Address(BaseModel):
    __tablename__ = "addresses"

    city = Column(String)
    state = Column(String)
    zip_code = Column(Integer)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__ (self):
        return f"<Address(id={self.id}, city='{self.city}')>"
        
class User(BaseModel):
    __tablename__ = "users"

    name = Column(String)
    age = Column(Integer)
    addresses: Mapped[list["Address"]] = relationship()

    def __repr__ (self):
        return f"<Address(id={self.id}, username='{self.name}')>"
        
'''

'''
class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    activities = Column(String)
'''
