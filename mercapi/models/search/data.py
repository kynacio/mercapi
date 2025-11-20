from dataclasses import dataclass

from mercapi.models.base import ResponseModel


@dataclass
class PhotoUri(ResponseModel):
    uri: str


@dataclass
class Auction(ResponseModel):
    id_: str
    bid_deadline: str
    total_bid: str
    highest_bid: str


@dataclass
class Shop(ResponseModel):
    id_: str
    display_name: str = None
    thumbnail: str = None
