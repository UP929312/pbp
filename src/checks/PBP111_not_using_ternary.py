# pylint: disable=missing-module-docstring, missing-function-docstring, line-too-long, too-few-public-methods, invalid-name, pointless-string-statement
import ast

from src.flake8_ast_error import PREFIX, Flake8ASTErrorInfo, filter_by


class NotUsingTernaryNotAllowed:
    """
    # Bad
    if x == 1:
        a = "Value1"
    else:
        a = "Value2

    # Good
    a = "Value1" if x == 1 else "Value2"
    """

    msg = PREFIX + "11: Use a ternary here, instead of an if statement"

    @classmethod
    def check(cls, node: ast.If, errors: list[Flake8ASTErrorInfo]) -> None:
        if not (
            isinstance(node.test, ast.Compare)
            and isinstance(node.test.comparators[0], ast.Constant)  # Check if we're comparing
            and node.orelse is not None,  # Against a constant  # And we have an else
        ):
            return
        # =========================================================
        # Make sure we have an else
        variable_if = filter_by(node.body, ast.Assign)
        if not variable_if:
            return
        variable_else = filter_by(node.orelse, ast.Assign)
        if not variable_else:
            return
        # =========================================================
        # We now have 2 variables, one for the if, one for the else
        if not (isinstance(variable_if.targets[0], ast.Name) and isinstance(variable_else.targets[0], ast.Name)):
            return
        if variable_if.targets[0].id != variable_else.targets[0].id:
            return

        if (
            isinstance(variable_if.value, ast.Constant) and
            isinstance(variable_else.value, ast.Constant)  # fmt: skip
        ):
            errors.append(Flake8ASTErrorInfo(node.lineno, node.col_offset, cls.msg, type(cls)))


"""
If(
    test=Compare(
        left=Name(id='x', ctx=Load()),
        ops=[
            Is()],
        comparators=[
            Constant(value=None)]),
    body=[
        Assign(
            targets=[
                Name(id='a', ctx=Store())],
            value=Constant(value=True))],
    orelse=[
        Assign(
            targets=[
                Name(id='a', ctx=Store())],
            value=Constant(value=False))
"""
