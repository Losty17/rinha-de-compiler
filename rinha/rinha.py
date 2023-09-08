from .nodes import File, Term


class Rinha:
    def __init__(self, file: File) -> None:
        self.file: File = file
        self.__members: dict[str, Term] = {}

    def execute(self) -> str:
        from rinha.term_executor import TermExecutor

        TermExecutor.exec(self, self.file["expression"])

    def register_member(self, name: str, value: Term, *, scope_name: str = "") -> None:
        if scope_name:
            scope = self.__members.get(scope_name, {})
            scope[name] = value
            self.__members[scope_name] = scope
        else:
            self.__members[name] = value

    def register_members(self, scope_name: str, names: list[str], values: list[Term]) -> None:
        for name, value in zip(names, values):
            self.register_member(name["text"], value, scope_name=scope_name)

    def get_member(self, name: str) -> Term:
        return self.__members[name]
