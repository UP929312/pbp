import ast

from src.flake_8_ast_error import PREFIX, Flake8ASTErrorInfo


class UsingFilterNotAllowed:
    """
    # Bad
    list(filter(lambda x: x > 5, range(10)))
    list(map(lambda x: x**2, range(10))

    # Good
    [x for x in range(10) if x > 5]
    [x**2 for x in range(10)]
    """

    msg = PREFIX + "12: Don't use list(filter()) or list(map()), use list comprehension instead"

    @classmethod
    def check(cls, node: ast.Call, errors: list[Flake8ASTErrorInfo]) -> None:
        if (
            isinstance(node.func, ast.Name)
            and node.func.id == "list"
            and isinstance(node.args[0], ast.Call)
            and isinstance(node.args[0].func, ast.Name)
            and node.args[0].func.id in ["filter", "map"]
        ):
            errors.append(Flake8ASTErrorInfo(node.lineno, node.col_offset, cls.msg, type(cls)))
