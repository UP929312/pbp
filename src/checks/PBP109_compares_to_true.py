# pylint: disable=missing-module-docstring, missing-function-docstring, line-too-long, too-few-public-methods, invalid-name, pointless-string-statement
import ast

from src.flake8_ast_error import PREFIX, Flake8ASTErrorInfo, IS


class ComparedToTrueNotAllowed:
    """
    # Bad
    if x is True:
        pass

    # Good
    if x:
        pass
    """

    msg = PREFIX + "09: Don't use x is True, use bool(x) or just x: instead"

    @classmethod
    def check(cls, node: ast.If, errors: list[Flake8ASTErrorInfo]) -> None:
        if (
            isinstance(node.test, ast.Compare) and
            isinstance(node.test.ops[0], IS) and
            isinstance(node.test.comparators[0], ast.Constant) and
            node.test.comparators[0].value is True  # fmt: skip
        ):
            errors.append(Flake8ASTErrorInfo(node.lineno, node.col_offset, cls.msg, type(cls)))
