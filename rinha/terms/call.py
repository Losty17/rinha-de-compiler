from uuid import uuid4
from ..nodes import Term
from ..term_executor import TermExecutor
from typing import List


class Call(Term):
    """Representa a declaração de uma variável"""

    callee: Term
    arguments: List[Term]


from ..rinha import Rinha


def exec(rinha: Rinha, term: Call, scope_name: str) -> None:
    callee = TermExecutor.exec(rinha, term["callee"])
    arguments = [TermExecutor.exec(rinha, argument) for argument in term["arguments"]]

    scope_name = scope_name if scope_name else f"scope_{uuid4().hex}"
    return TermExecutor.exec(rinha, callee, scope_name)(*arguments)