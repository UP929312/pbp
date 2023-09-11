# pylint: disable=missing-module-docstring, missing-function-docstring, line-too-long, too-few-public-methods, invalid-name, pointless-string-statement
import ast

from src.flake8_ast_error import PREFIX, Flake8ASTErrorInfo


class JsonLoadsNotAllowed:
    """
    # Bad
    import json
    response = requests.get("https://example.com")
    data = json.loads(response.text)

    # Good
    response = requests.get("https://example.com").json()
    """

    msg = PREFIX + "02: Don't use json.loads(response.text), use response.json() instead"

    @classmethod
    def check(cls, node: ast.Call, errors: list[Flake8ASTErrorInfo]) -> None:
        # pylint: disable=too-many-boolean-expressions
        if (
            isinstance(node.func, ast.Attribute)
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == "json"
            and node.func.attr == "loads"
            and isinstance(node.args[0], ast.Attribute)
            and node.args[0].attr == "text"
        ):
            errors.append(Flake8ASTErrorInfo(node.lineno, node.col_offset, cls.msg, type(cls)))
