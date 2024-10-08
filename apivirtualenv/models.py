from sqlalchemy import Column , Integer, String,Boolean,ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__="poststable"

    id =Column(Integer, primary_key=True, nullable=False)
    title=Column(String,nullable=False)
    content=Column(String,nullable=False)
    published=Column(Boolean,server_default='True', nullable=False)
    created_at=Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    owner_id=Column(Integer,ForeignKey("userstable.id", ondelete="CASCADE"), nullable =False)

    owner= relationship("User")

class User(Base):
    __tablename__="userstable"

    id =Column(Integer, primary_key=True, nullable=False)
    name=Column(String,nullable=False)
    email=Column(String,nullable=False,unique=True)
    password=Column(String, nullable=False)
    created_at=Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

class Vote(Base):
    __tablename__="votestable"
    user_id=Column(Integer,ForeignKey("userstable.id", ondelete="CASCADE"),primary_key=True)
    post_id=Column(Integer,ForeignKey("poststable.id", ondelete="CASCADE"),primary_key=True)   
