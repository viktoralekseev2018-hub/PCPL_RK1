from dataclasses import dataclass

@dataclass
class Operator:
    """Оператор; complexity — условная сложность в баллах.
    Language_id задаёт связь «один ко многим» с языком.
    """

    id: int
    name: str
    complexity: int
    language_id: int


@dataclass
class ProgrammingLanguage:
    """Язык программирования."""
    id: int
    name: str


@dataclass
class OperatorLanguage:
    """Связь оператора с языком для модели «многие ко многим»."""
    operator_id: int
    language_id: int
