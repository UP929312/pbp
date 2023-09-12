# pylint: disable=missing-module-docstring, missing-function-docstring, line-too-long, too-few-public-methods, invalid-name, pointless-string-statement
import ast

from src.flake8_ast_error import PREFIX, Flake8ASTErrorInfo


class NonPascalCaseClassNotAllowed:
    """
    # Bad
    class my_class:
        pass

    # Good
    class MyClass:
        pass
    """

    msg = PREFIX + "16: Class names should be in PascalCase, (found: {}, should be: {})"

    def convert_to_pascal_case(name) -> str:
        return "".join(word.title() for word in name.split("_"))

    @classmethod
    def check(cls, node: ast.ClassDef, errors: list[Flake8ASTErrorInfo]) -> None:
        if node.name.islower() or "_" in node.name :
            found = node.name
            expected = cls.convert_to_pascal_case(node.name)
            msg = cls.msg.format(found, expected)
            errors.append(Flake8ASTErrorInfo(node.lineno, node.col_offset, msg, type(cls)))


"""
ClassDef(
    name='my_class',
    bases=[],
    keywords=[],
    body=[
    Pass()],
    decorator_list=[])],
"""