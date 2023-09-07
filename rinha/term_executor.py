from .rinha import Rinha
from .nodes import Term
from typing import Any, Callable
from importlib import import_module

class TermExecutor:
    @staticmethod
    def exec(rinha: Rinha, term: Term) -> None:
        name = term["kind"].lower()  # __exec_kind

        # Busca pelo módulo na pasta terms e executa a função chamada 'exec'
        # passando como argumentos a rinha e o termo
        try:
            module = import_module(f'.terms.{name}', package='rinha')
            func: Callable[[Rinha, Term]] = getattr(module, 'exec', TermExecutor.exec_error)
            func(rinha, term)        
        except ImportError:
            TermExecutor.exec_error(rinha, term)

    @staticmethod
    def exec_error(rinha: Rinha, term: Term) -> Any:
        from .errors import TermExecuteError

        raise TermExecuteError(
            f'Erro de sintaxe: {term["kind"].lower()} não é um termo válido.'
        )