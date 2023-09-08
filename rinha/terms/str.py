from ..nodes import Term

class Str(Term):
    """ Representa uma string """

    value: str


from ..rinha import Rinha


def exec(rinha: Rinha, term: Str, scope_name: str) -> str:
    return term["value"]
