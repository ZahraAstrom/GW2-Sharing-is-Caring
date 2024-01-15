from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, func

Base = declarative_base()
metadata = Base.metadata

class User(Base):
  __tablename__="user"

  id = Column(Integer, primary_key=True)
  api_key = Column(String(72))
  user_name = Column(String(30))

  def __repr__(self):
    return f"id: {self.id}, name: {self.user_name}"