import datetime
from sqlalchemy import Column, ForeignKey, Integer, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


class User(Base):
	__tablename__ = 'user'

	id = Column(Integer, primary_key = True)
	name = Column(String(250), nullable = False)
	email = Column(String(250))
	picture = Column(String(250))


class Category(Base):
	__tablename__ = 'category'

	id = Column(Integer, primary_key = True)
	name = Column(String(250), nullable = False)
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)
	items = relationship('Items', cascade = 'all, delete-orphan')


	@property
	def serialize(self):
		# Return object data in easily serializable format
		return {
			'name': self.name,
			'id': self.id,
		}


class Items(Base):
	__tablename__ = 'items'

	id = Column(Integer, primary_key = True)
	name = Column(String(250), nullable = False)
	description = Column(String(250))
	date = Column(DateTime, nullable = False)
	category_id = Column(Integer, ForeignKey('category.id'))
	category = relationship(Category)
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)

	@property
	def serialize(self):
		# Return object data in easily serializeable format
		return {
			'name': self.name,
			'description': self.description,
			'id': self.id,
			'category': self.category,
		}


engine = create_engine('sqlite:///itemcatalog.db')


Base.metadata.create_all(engine)