# pylint: disable=missing-module-docstring, missing-function-docstring, line-too-long, too-few-public-methods, invalid-name, pointless-string-statement
import ast

from src.flake8_ast_error import PREFIX, Flake8ASTErrorInfo


class NonUsingListCompNotAllowed:
    """
    # Bad
    my_list = []
    for char in my_sub_list:
        my_list.append(char)

    # Good
    my_list = [x for x in my_sub_list]
    """

    msg = PREFIX + "17: Use list comprehension where appropriate"

    @classmethod
    def check(cls, node: ast.Module, errors: list[Flake8ASTErrorInfo]) -> None:
        for i, statement in enumerate(node.body):
            if i == len(node.body) - 1:
                break
            next_statement = node.body[i + 1]
            if (
                # Check if they're assigning to a list
                isinstance(statement, ast.Assign)
                and isinstance(statement.value, ast.List)
                and statement.targets
                and isinstance(statement.targets[0], ast.Name)
                # =========================================================
                # Check if the next statement is a for loop
                and isinstance(next_statement, ast.For)
                and isinstance(next_statement.body[0], ast.Expr)
                and isinstance(next_statement.body[0].value, ast.Call)
                and isinstance(next_statement.body[0].value.func, ast.Attribute)
                and next_statement.body[0].value.func.attr == "append"
                and isinstance(next_statement.body[0].value.func.value, ast.Name)
                and next_statement.body[0].value.func.value.id == statement.targets[0].id
            ):
                errors.append(Flake8ASTErrorInfo(statement.lineno, statement.col_offset, cls.msg, type(cls)))


"""
Assign(
    targets=[
        Name(id='my_list', ctx=Store())],
    value=List(elts=[], ctx=Load())),
For(
    target=Name(id='char', ctx=Store()),
    iter=Constant(value='hello'),
    body=[
        Expr(
            value=Call(
                func=Attribute(
                    value=Name(id='my_list', ctx=Load()),
                    attr='append',
                    ctx=Load()),
                args=[
                    Name(id='char', ctx=Load())],
                keywords=[]))],
    orelse=[])],
"""
