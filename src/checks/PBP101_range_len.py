# pylint: disable=missing-module-docstring, missing-function-docstring, line-too-long, too-few-public-methods, invalid-name, pointless-string-statement
import ast

from src.flake8_ast_error import PREFIX, Flake8ASTErrorInfo


class RangeLenNotAllowed:
    """
    # Bad
    for i in range(len(my_list)):
        print(my_list[i])

    # Good
    for x in list:
        print(x)
    for _ in range(len(my_list)):
        ...
    """

    msg = PREFIX + "01: Don't use range(len(list)), use zip(list_a, list_b) instead, or for x in list"

    @classmethod
    def check(cls, node: ast.For, errors: list[Flake8ASTErrorInfo]) -> None:
        if (
            isinstance(node.target, ast.Name) and
            node.target.id == "_"  # fmt: skip
        ):
            return
        # If they're using for _ in range(len(list)), we don't want to flag that, so we return early
        if (
            isinstance(node.iter, ast.Call) and 
            isinstance(node.iter.func, ast.Name) and
            node.iter.func.id == "range" and
            isinstance(node.iter.args[0], ast.Call) and
            isinstance(node.iter.args[0].func, ast.Name) and
            node.iter.args[0].func.id == "len"  # fmt: skip
        ):
            errors.append(Flake8ASTErrorInfo(node.lineno, node.col_offset, cls.msg, type(cls)))


"""
For(
    target=Name(id='i', ctx=Store()),
    iter=Call(
        func=Name(id='range', ctx=Load()),
        args=[
            Call(
                func=Name(id='len', ctx=Load()),
                args=[
                    Name(id='my_list', ctx=Load())],
                keywords=[])],
        keywords=[]),
    body=[
        Expr(
        value=Call(
            func=Name(id='print', ctx=Load()),
            args=[
                Subscript(
                    value=Name(id='my_list', ctx=Load()),
                    slice=Name(id='i', ctx=Load()),
                    ctx=Load()),
                Subscript(
                    value=Name(id='my_second_list', ctx=Load()),
                    slice=Name(id='i', ctx=Load()),
                    ctx=Load())],
            keywords=[]))],
    orelse=[])],
"""
