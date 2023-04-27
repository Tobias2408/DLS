# crud.py
from typing import List
from sqlalchemy.orm import Session
from exceptions import OrdersInfoInfoAlreadyExistError, OrdersInfoNotFoundError
from models import OrdersInfo
from schemas import CreateAndUpdateOrders
import datetime

# Function to get list of orders info
def get_all_orders(session: Session, limit: int, offset: int) -> List[OrdersInfo]:
    return session.query(OrdersInfo).offset(offset).limit(limit).all()


# Function to  get info of a particular orders
def get_orders_info_by_id(session: Session, _id: int) -> OrdersInfo:
    orders_info = session.query(OrdersInfo).get(_id)
    if orders_info is None:
        raise OrdersInfoNotFoundError

    print("id: "+str(orders_info.OrderId) + "DateCreated: "  + str(orders_info.dateCreated))
    
    return orders_info


# Function to add a new orders info to the database
def create_orders(session: Session, orders_info: CreateAndUpdateOrders) -> OrdersInfo:
    orders_details = session.query(OrdersInfo).filter().first()
    # rember to use this if you act have values
    #if orders_details is not None:
        #raise OrdersInfoInfoAlreadyExistError

    new_orders_info = OrdersInfo(**orders_info.dict())
    new_orders_info.dateCreated = datetime.datetime.now()
    session.add(new_orders_info)
    session.commit()
    session.refresh(new_orders_info)
    return new_orders_info


# Function to update details of the orders
def update_orders_info(session: Session, _id: int, info_update: CreateAndUpdateOrders) -> OrdersInfo:
    orders_info = get_orders_info_by_id(session, _id)

    if orders_info is None:
        raise OrdersInfoNotFoundError

    orders_info.dateCreated = datetime.datetime.now()
    print("23id: "+str(orders_info.OrderId) + "DateCreated: "  + str(orders_info.dateCreated))


    session.commit()
    session.refresh(orders_info)

    return orders_info


# Function to delete a orders info from the db
def delete_orders_info(session: Session, _id: int):
    orders_info = get_orders_info_by_id(session, _id)
    print("23id: "+str(orders_info.OrderId) + "DateCreated: "  + str(orders_info.dateCreated))

    if orders_info is None:
        raise OrdersInfoNotFoundError

    session.delete(orders_info)
    session.commit()

    return