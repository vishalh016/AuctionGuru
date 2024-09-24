# │   │   ├── models.py               # Database models (MongoDB schemas)

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List
from bson import ObjectId

class ItemModel(BaseModel):
    id: Optional[str] = Field(alias="_id")
    title: str
    description: str
    start_price: float
    current_price: float
    auction_end_time: datetime
    images: List[str]
    category: Optional[str]
    created_at: datetime = datetime.now()

class AuctionModel(BaseModel):
    id: Optional[str] = Field(alias="_id")
    item_id: str
    current_highest_bid: float
    highest_bidder_id: Optional[str]
    auction_start_time: datetime
    auction_end_time: datetime
    bids: List[dict] = []
    created_at: datetime = datetime.now()

class BidModel(BaseModel):
    user_id: str
    bid_amount: float
    bid_time: datetime = datetime.now()

