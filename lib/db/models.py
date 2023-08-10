from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)

    cities = relationship('City', back_populates='user')
    weather_preferences = relationship('WeatherPreference', back_populates='user')

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    region = Column(String)
    country = Column(String)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='cities')
    weather_preferences = relationship('WeatherPreference', back_populates='city')
    def __str__(self):
        return self.name

class WeatherPreference(Base):
    __tablename__ = 'weather_preferences'
    id = Column(Integer, primary_key=True)
    preferred_units = Column(String)
    precip_unit = Column(String)
    humid_unit = Column(String)
    feels_like_unit = Column(String)
    visibility_unit = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='weather_preferences')
    city_id = Column(Integer, ForeignKey('cities.id'))
    city = relationship('City', back_populates='weather_preferences')

engine = create_engine('sqlite:///db/weather_cli.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
