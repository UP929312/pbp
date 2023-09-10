import ast

from src.checks.flake_8_ast_error import PREFIX, Flake8ASTErrorInfo


class InheritsFromObjectNotAllowed:
    """
    # Bad
    class Foo(object):
        pass

    # Good
    class Foo:
        pass
    """

    msg = PREFIX + "10: Don't inherit from object, not required since Python 3.0"

    @classmethod
    def check(cls, node: ast.ClassDef, errors: list[Flake8ASTErrorInfo]) -> None:
        if any([base for base in node.bases if isinstance(base, ast.Name) and base.id == "object"]):
            errors.append(Flake8ASTErrorInfo(node.lineno, node.col_offset, cls.msg, type(cls)))
