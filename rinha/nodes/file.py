from typing import TypedDict
from .term import Term
from .location import Location

class File(TypedDict):
    name: str
    expression: Term
    location: Location