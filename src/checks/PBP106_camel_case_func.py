# pylint: disable=missing-module-docstring, missing-function-docstring, line-too-long, too-few-public-methods, invalid-name, pointless-string-statement
import ast
import re

from src.flake8_ast_error import PREFIX, Flake8ASTErrorInfo


class CamelCaseFuncNotAllowed:
    """
    # Bad
    def CamelCaseFunc():
        pass

    # Good
    def snake_case_func():
        pass
    """

    msg = PREFIX + "06: Function names should be in snake_case, not camelCase or PascalCase, (found: {}, should be: {})"

    @classmethod
    def check(cls, node: ast.For, errors: list[Flake8ASTErrorInfo]) -> None:
        if not node.name.islower():
            found = node.name
            expected = re.sub(r"(?<!^)(?=[A-Z])", "_", node.name).lower()
            errors.append(Flake8ASTErrorInfo(node.lineno, node.col_offset, cls.msg.format(found, expected), type(cls)))
