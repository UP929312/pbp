# pylint: disable=missing-module-docstring, missing-function-docstring, line-too-long, too-few-public-methods, invalid-name, pointless-string-statement
import ast
import builtins

from src.flake8_ast_error import PREFIX, Flake8ASTErrorInfo

key_words = [x for x in dir(builtins) if not x.startswith("_")]


class ShadowBuiltinsNotAllowed:
    """
    # Bad
    map = my_map_object
    list = my_list_object

    # Good
    my_map = my_map_object
    my_list = my_list_object
    """

    msg = PREFIX + "13: Don't override builtins, use a different name instead (used: `{}`))"

    @classmethod
    def check(cls, node: ast.Assign, errors: list[Flake8ASTErrorInfo]) -> None:
        if (
            node.targets and
            isinstance(node.targets[0], ast.Name) and
            node.targets[0].id in key_words  # fmt: skip
        ):
            name_used = node.targets[0].id
            errors.append(Flake8ASTErrorInfo(node.lineno, node.col_offset, cls.msg.format(name_used), type(cls)))


"""
Assign(
    targets=[
        Name(id='map', ctx=Store())],
    value=Constant(value='my_map_object'))],
"""
