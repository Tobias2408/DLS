from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Enum, TIMESTAMP
from database import Base
import enum




class OrdersInfo(Base):
    __tablename__ = "orders"

    OrderId = Column(Integer, primary_key=True, index=True)
    dateCreated = Column(TIMESTAMP)
   