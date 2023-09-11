# pylint: disable=missing-module-docstring, missing-function-docstring, line-too-long, too-few-public-methods, invalid-name, pointless-string-statement
import ast

from src.flake8_ast_error import PREFIX, Flake8ASTErrorInfo


class DefaultMutableArgsNotAllowed:
    """
    # Bad
    def foo(bar=[]):
        pass

    # Good
    def foo(bar=None):
        if bar is None:
            bar = []
        pass
    """

    msg = PREFIX + "07: Parameter defaults shouldn't be mutable, set to None instead and do if param is None: param = []"

    @classmethod
    def check(cls, node: ast.For, errors: list[Flake8ASTErrorInfo]) -> None:
        if [
            x for x in node.args.defaults
            if isinstance(x, ast.List) and
            x.elts == []  # fmt: skip
        ]:
            errors.append(Flake8ASTErrorInfo(node.lineno, node.col_offset, cls.msg, type(cls)))
