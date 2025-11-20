from dataclasses import dataclass

from mercapi.models.base import ResponseModel


@dataclass
class PhotoUri(ResponseModel):
    uri: str


@dataclass
class Auction(ResponseModel):
    id_: str = None
    bid_deadline: str = None
    total_bid: str = None
    highest_bid: str = None


@dataclass
class Shop(ResponseModel):
    id_: str
    display_name: str = None
    thumbnail: str = None
