import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    username = Column(String(250), unique = True, nullable= False)
    password = Column (String(250), nullable = False)
    email = Column(String(250), unique = True, nullable= False)
    cel = Column(String(250), unique = True, nullable = False)

    class Login(Base):
        __tablename__ = 'login'
        id = Column(Integer, primary_key = True)
        username = Column(String(250), ForeignKey('user.username'))
        password = Column(String(250), ForeignKey('user.password'))

        login = relationship('User')

    class Post (Base):
        __tablename__ = 'post'


        id = Column(Integer, primary_key = True)
        user_id = Column(Integer, ForeignKey('user.id'))
        
        user_post = relationship('User')

    class Photo (Base):

        __tablename__ = 'photo'


        id = Column(Integer, primary_key = True)
        description = Column(String(250), nullable = False)
        postId = Column(Integer, ForeignKey('post.id'))
        userId = Column(Integer, ForeignKey('user.id'))

        photo = relationship('Post')


    class Like (Base):
        __tablename__ = 'like'

        id = Column(Integer, primary_key = True)
        usarname = Column(String(250), ForeignKey('user.username'))

        like = relationship('Photo')
    class Comments (Base):
        __tablename__ = 'comments'

        id = Column(Integer, primary_key = True)
        comment = Column(String(250), nullable = False)
        userId = Column (Integer, ForeignKey('user.id'))
        username = Column(String(250), ForeignKey('user.username'))

        comments = relationship('Photo')


        class Followers (Base):

            __tablename__ = 'followers'
            

            id = Column(Integer, primary_key = True)
            username = Column(String(250), unique = True)
            userId = Column(Integer, ForeignKey('user.id'))

            user_followers = relationship('User')


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
