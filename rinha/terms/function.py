from ..nodes import Term
from ..terms.var import Var
from ..term_executor import TermExecutor
from typing import List, Callable

class Function(Term):
    """Representa a declaração de uma função"""

    parameters: List[Var]
    value: Term

from ..rinha import Rinha


def exec(rinha: Rinha, term: Function, scope_name: str) -> Callable:
    def function(*args):
        rinha.register_members(scope_name, term["parameters"], args)
        return TermExecutor.exec(rinha, term["value"])

    return function
