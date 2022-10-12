import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from schemas.order_items_schema import OrderItemsSchema

from schemas.product_schema import ProductSchema

class CartSchema(BaseModel):
    user_id: str
    order_items: List[OrderItemsSchema] = []
    total_price: float
    