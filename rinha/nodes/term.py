from typing import Literal, TypedDict
from .location import Location
from enum import Enum

class TermKind(Enum):
    Int = 0
    Str = 1
    Call = 2
    Binary = 3
    Function = 4
    Let = 5
    If = 6
    Print = 7
    First = 8
    Second = 9
    Bool = 10
    Tuple = 11
    Var = 12

class Term(TypedDict):
    kind: Literal['Int', 'Str', 'Call', 'Binary', 'Function', 'Let', 'If', 'Print', 'First', 'Second', 'Bool', 'Tuple', 'Var']
    location: Location