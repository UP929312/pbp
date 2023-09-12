# pylint: disable=missing-module-docstring, missing-function-docstring, line-too-long, too-few-public-methods, invalid-name, pointless-string-statement
import ast

from src.flake8_ast_error import PREFIX, Flake8ASTErrorInfo


class AnyOrAllWithCompNotAllowed:
    """
    # Bad
    any([x.id for x in my_list])
    all([x.id for x in my_list])

    # Good
    all(x.id for x in my_list)
    any(x.id for x in my_list)
    """

    msg = PREFIX + "15: Prefer simpler any or all statements: remove unnecessary comprehension"

    @classmethod
    def check(cls, node: ast.Call, errors: list[Flake8ASTErrorInfo]) -> None:
        if (
            isinstance(node.func, ast.Name)
            and node.func.id in {"all", "any"}
            and len(node.args) == 1
            and isinstance(node.args[0], ast.ListComp)  # fmt: skip
        ):
            errors.append(Flake8ASTErrorInfo(node.lineno, node.col_offset, cls.msg, type(cls)))


"""
Call(
    func=Name(id='any', ctx=Load()),
    args=[
        ListComp(
            elt=Name(id='x', ctx=Load()),
            generators=[
                comprehension(
                    target=Name(id='x', ctx=Store()),
                    iter=Call(
                    func=Name(id='range', ctx=Load()),
                    args=[
                        Constant(value=5)],
                    keywords=[]),
                    ifs=[],
                    is_async=0)])],
        keywords=[]))],
"""
