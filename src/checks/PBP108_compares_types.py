import ast

from src.checks.flake_8_ast_error import PREFIX, Flake8ASTErrorInfo


class CompareTypesNotAllowed:
    """
    # Bad
    if type(x) == int:
        pass
    if type(x) is int:
        pass

    # Good
    if isinstance(x, int):
        pass
    """

    msg = PREFIX + "08: Comparing types is not allowed, use isinstance() instead"

    @classmethod
    def check(cls, node: ast.Compare, errors: list[Flake8ASTErrorInfo]) -> None:
        left_is_type = (
            isinstance(node.left, ast.Call) and
            isinstance(node.left.func, ast.Name) and
            node.left.func.id == "type"
        )
        node.right = node.comparators[0]
        right_is_type = (
            isinstance(node.right, ast.Call) and
            isinstance(node.right.func, ast.Name) and
            node.right.func.id == "type"
        )
        # =========================================================
        if left_is_type or right_is_type:
            errors.append(Flake8ASTErrorInfo(node.lineno, node.col_offset, cls.msg, type(cls)))
