from .var import Var
from ..nodes import Term
from ..term_executor import TermExecutor


class Print(Term):
    """Representa a declaração de uma variável"""

    value: Term


from ..rinha import Rinha


def exec(rinha: Rinha, term: Print, scope_name: str) -> None:
    result = TermExecutor.exec(rinha, term["value"])
    
    print(result)
