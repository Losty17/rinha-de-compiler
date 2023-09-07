from .nodes import File, Term


class Rinha:
    def __init__(self, file: File) -> None:
        self.file: File = file
        self.members: dict[str, Term] = {}

    def execute(self) -> str:
        print(f'Executando {self.file["name"]}')

        from rinha.term_executor import TermExecutor

        TermExecutor.exec(self, self.file["expression"])

    def register_member(self, name: str, value: Term) -> None:
        self.members[name] = value
