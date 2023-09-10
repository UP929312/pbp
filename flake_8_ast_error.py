import ast
from typing import NamedTuple

PREFIX = "PBP1"

IS = type(ast.Is())
EQUAL = type(ast.Eq())
NOT_EQUAL = type(ast.NotEq())


def filter_by(node: ast.AST, cls: type) -> list[ast.AST]:
    options = [n for n in node if isinstance(n, cls)]
    if options:
        return options[0]
    return []


class Flake8ASTErrorInfo(NamedTuple):
    line_number: int
    offset: int
    message: str
    cls: type
