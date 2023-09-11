# pylint: disable=missing-module-docstring, missing-function-docstring, line-too-long, too-few-public-methods, invalid-name, pointless-string-statement
import ast

from src.flake8_ast_error import PREFIX, Flake8ASTErrorInfo


class AssignToListNotAllowed:
    """
    # Bad
    x = list()

    # Good
    x = []
    """

    msg = PREFIX + "05: Don't use x = list(), use x = [] instead"

    @classmethod
    def check(cls, node: ast.If, errors: list[Flake8ASTErrorInfo]) -> None:
        if (
            isinstance(node.func, ast.Name) and
            node.func.id == "list" and
            not node.args and
            not node.keywords  # fmt: skip
        ):
            errors.append(Flake8ASTErrorInfo(node.lineno, node.col_offset, cls.msg, type(cls)))
