from uuid import uuid4
from ..nodes import Term
from ..term_executor import TermExecutor
from typing import List


class If(Term):
    """Representa uma condicional"""

    pass

from ..rinha import Rinha


def exec(rinha: Rinha, term: If, scope_name: str) -> None:
    pass