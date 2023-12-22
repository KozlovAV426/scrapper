from datetime import datetime

from sqlalchemy import Column, String, DateTime, Text, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Flight(Base):
    __tablename__ = 'flight'

    id = Column(Integer(), primary_key=True)
    departure_airport = Column(String(64), nullable=False)
    arrival_airport = Column(String(64), nullable=False)
    departure_time = Column(DateTime(), default=datetime.now)
    arrival_time = Column(DateTime(), default=datetime.now)
    price = Column(Integer(), nullable=False)
    flight_time = Column(Integer(), nullable=False)

# @dataclass
# class Flight:
#     departure_airport: str
#     arrival_airport: str
#     departure_time: int
#     arrival_time:
#     price: int
