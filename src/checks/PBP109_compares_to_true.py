import ast

from src.flake8_ast_error import PREFIX, Flake8ASTErrorInfo, IS


class ComparedToTrueNotAllowed:
    """
    # Bad
    if x is True:
        pass

    # Good
    if x:
        pass
    """

    msg = PREFIX + "09: Don't use x is True, use bool(x) or just x: instead"

    @classmethod
    def check(cls, node: ast.If, errors: list[Flake8ASTErrorInfo]) -> None:
        if (
            isinstance(node.test, ast.Compare) and
            isinstance(node.test.ops[0], IS) and
            node.test.comparators[0].value == True
        ):
            errors.append(Flake8ASTErrorInfo(node.lineno, node.col_offset, cls.msg, type(cls)))
