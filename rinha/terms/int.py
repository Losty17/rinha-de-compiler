from ..nodes import Term

class Int(Term):
    """ Representa um inteiro """

    value: int


from ..rinha import Rinha


def exec(rinha: Rinha, term: Int, scope_name: str) -> int:
    return term["value"]
