# pylint: disable=missing-module-docstring, missing-function-docstring, line-too-long, too-few-public-methods, invalid-name, pointless-string-statement
import ast

from src.flake8_ast_error import PREFIX, Flake8ASTErrorInfo


class AnyWithCompNotAllowed:
    """
    # Bad
    any([x.id for x in bar])
    all([x.id for x in bar])

    # Good
    all(x.id for x in bar)
    any(x.id for x in bar)
    """

    msg = PREFIX + "15: Prefer-simple-any-all: remove unnecessary comprehension."

    @classmethod
    def check(cls, node: ast.Call, errors: list[Flake8ASTErrorInfo]) -> None:
        if not (
            isinstance(node.func, ast.Name) and
            node.func.id not in {"all", "any"}  # fmt: skip
        ):
            return
        if len(node.args) != 1:
            return
        if isinstance(node.args[0], ast.ListComp):
            errors.append(Flake8ASTErrorInfo(node.lineno, node.col_offset, cls.msg, type(cls)))
