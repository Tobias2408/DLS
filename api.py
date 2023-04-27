from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from crud import get_all_orders, create_orders, get_orders_info_by_id, update_orders_info, delete_orders_info
from database import get_db
from exceptions import OrdersInfoException
from schemas import Orders, CreateAndUpdateOrders, PaginatedOrdersInfo
import datetime
router = APIRouter()


# Example of Class based view
@cbv(router)
class Orderss:
    session: Session = Depends(get_db)

    # API to get the list of orders info
    @router.get("/orders")
    def list_orderss(self, limit: int = 10, offset: int = 0):
        orderss_list = get_all_orders(self.session, limit, offset)
        response = {"limit": limit, "offset": offset, "data": orderss_list}
        return response

    # API endpoint to add a orders info to the database
    @router.post("/orders")
    def add_orders(self, orders_info: CreateAndUpdateOrders):

        try:
            orders_info = create_orders(self.session, orders_info)
            return orders_info
        except OrdersInfoException as cie:
            raise HTTPException(**cie.__dict__)


# API endpoint to get info of a particular orders
@router.get("/orders/{orders_id}")
def get_orders_info(orders_id: int, session: Session = Depends(get_db)):

    try:
        orders_info = get_orders_info_by_id(session, orders_id)
        return orders_info
    except OrdersInfoException as cie:
        raise HTTPException(**cie.__dict__)


# API to update a existing orders info
@router.put("/orders/{orders_id}")
def update_orders(orders_id: int, new_info: CreateAndUpdateOrders, session: Session = Depends(get_db)):

    try:
        orders_info = update_orders_info(session, orders_id, new_info)
        print("22id: "+str(orders_info.OrderId) + "DateCreated: "  + str(orders_info.dateCreated))
        return orders_info
    except OrdersInfoException as cie:
        raise HTTPException(**cie.__dict__)


# API to delete a orders info from the data base
@router.delete("/orders/{orders_id}")
def delete_orders(orders_id: int, session: Session = Depends(get_db)):

    try:
        return delete_orders_info(session, orders_id)
    except OrdersInfoException as cie:
        raise HTTPException(**cie.__dict__)