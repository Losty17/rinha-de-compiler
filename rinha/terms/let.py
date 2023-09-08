from .var import Var
from ..nodes import Term
from ..term_executor import TermExecutor


class Let(Term):
    """Representa a declaração de uma variável"""

    name: Var
    value: Term
    next: Term


from ..rinha import Rinha


def exec(rinha: Rinha, term: Let, scope_name: str) -> None:
    rinha.register_member(term["name"]["text"], term["value"])

    if term["next"]:
        TermExecutor.exec(rinha, term["next"])
