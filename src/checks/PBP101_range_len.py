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
    """

    msg = PREFIX + "01: Don't use range(len(list)), use zip(list_a, list_b) instead, or for x in list"

    @classmethod
    def check(cls, node: ast.For, errors: list[Flake8ASTErrorInfo]) -> None:
        if (
            node.iter.func.id == "range" and
            node.iter.args[0].func.id == "len"  # fmt: skip
        ):
            errors.append(Flake8ASTErrorInfo(node.lineno, node.col_offset, cls.msg, type(cls)))
