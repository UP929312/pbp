# pylint: disable=missing-module-docstring, missing-function-docstring, line-too-long, too-few-public-methods, invalid-name, pointless-string-statement
import ast

from src.flake8_ast_error import PREFIX, Flake8ASTErrorInfo


class NoPointlessTernaryNotAllowed:
    """
    # Bad
    x = True if condition else False

    # Good
    x = bool(condition)
    """

    msg = PREFIX + "14: Don't True if <condition> else False, just use bool(<condition>)"

    @classmethod
    def check(cls, node: ast.IfExp, errors: list[Flake8ASTErrorInfo]) -> None:
        if (
            isinstance(node.body, ast.NameConstant)
            and node.body.value in [True, False]
            and isinstance(node.orelse, ast.NameConstant)
            and node.orelse.value in [True, False]
        ):
            errors.append(Flake8ASTErrorInfo(node.lineno, node.col_offset, cls.msg, type(cls)))


"""
IfExp(
    test=Compare(
        left=Name(id='value', ctx=Load()),
        ops=[
            Eq()],
        comparators=[
            Constant(value=5)]),
    body=Constant(value=True),
    orelse=Constant(value=False)))],
"""
