import ast

from src.flake_8_ast_error import PREFIX, Flake8ASTErrorInfo


class OpenNoWithNotAllowed:
    """
    # Bad
    file = open("file.txt")
    file.read()
    file.close()

    # Good
    with open("file.txt") as file:
        data = file.read()
    """

    msg = PREFIX + "03: Don't use data = open(), use a with statement instead"

    @classmethod
    def check(cls, node: ast.Call, errors: list[Flake8ASTErrorInfo]) -> None:
        if (
            isinstance(node.func, ast.Attribute)
            and isinstance(node.func.value, ast.Call)
            and isinstance(node.func.value.func, ast.Name)
            and node.func.value.func.id == "open"
        ):
            errors.append(Flake8ASTErrorInfo(node.lineno, node.col_offset, cls.msg, type(cls)))
