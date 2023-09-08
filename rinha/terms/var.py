from typing import Any
from ..nodes import Term

class Var(Term):
    """ Representa o nome (referência) de uma variável """
    text: str

from ..rinha import Rinha

def exec(rinha: Rinha, term: Var, scope_name: str) -> Any:
    return rinha.get_member(term["text"])