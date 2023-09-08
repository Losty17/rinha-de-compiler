from .rinha import Rinha
from .nodes import Term
from typing import Any, Callable
from importlib import import_module

class TermExecutor:
    @staticmethod
    def exec(rinha: Rinha, term: Term, scope_name: str = "") -> None:
        name = term["kind"].lower()  # __exec_kind

        # Busca pelo módulo na pasta terms e executa a função chamada 'exec'
        # passando como argumentos a rinha e o termo
        try:
            module = import_module(f'.terms.{name}', package='rinha')
            func: Callable[[Rinha, Term, str], None] = getattr(module, 'exec', TermExecutor.exec_error)
            return func(rinha, term, scope_name)        
        except ImportError:
            TermExecutor.exec_error(rinha, term, scope_name)

    @staticmethod
    def exec_error(rinha: Rinha, term: Term, scope_name: str) -> Any:
        from .errors import TermExecuteError

        raise TermExecuteError(
            f'Erro de sintaxe: {term["kind"].lower()} não é um termo válido.'
        )