from pydantic import BaseModel
import datetime
from typing import Optional, List



# TO support creation and update APIs
class CreateAndUpdateOrders(BaseModel):
    dateCreated = datetime.datetime
 



# TO support list and get APIs
class Orders(CreateAndUpdateOrders):
   #id: int

    class Config:
        orm_mode = True


# To support list cars API
class PaginatedOrdersInfo(BaseModel):
    limit: int
    offset: int
    data: List[Orders]