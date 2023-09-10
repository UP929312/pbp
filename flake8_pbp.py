from _ast import FunctionDef, IfExp
import ast
from typing import Any, Iterator
from flake_8_ast_error import Flake8ASTErrorInfo

# fmt: off
from checks import (
    RangeLenNotAllowed, JsonLoadsNotAllowed, OpenNoWithNotAllowed, RequestsJsonDumpsNotAllowed, AssignToListNotAllowed,  # For
    CamelCaseFuncNotAllowed, DefaultMutableArgsNotAllowed, UsingFilterNotAllowed,  AnyWithCompNotAllowed,  # Call
    CompareTypesNotAllowed,  # Compare
    ComparedToTrueNotAllowed, NotUsingTernaryNotAllowed,  # If
    InheritsFromObjectNotAllowed,  # ClassDef
    ShadowBuiltinsNotAllowed,  # Assign
    NotPointlessTernaryNotAllowed,  # IfExp
)
# fmt: on


class ProduceBetterPythonPlugin:
    name = "produce_better_python"
    version = "0.0.1"

    def __init__(self, tree: ast.AST) -> None:
        self._tree = tree

    def run(self) -> Iterator[Flake8ASTErrorInfo]:
        # print("Running plugin")
        visitor = Visitor()
        visitor.visit(self._tree)
        yield from visitor.errors


class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.errors: list[Flake8ASTErrorInfo] = []

    def visit_For(self, node: ast.For) -> None:
        RangeLenNotAllowed.check(node, self.errors)
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call) -> None:
        JsonLoadsNotAllowed.check(node, self.errors)
        OpenNoWithNotAllowed.check(node, self.errors)
        RequestsJsonDumpsNotAllowed.check(node, self.errors)
        AssignToListNotAllowed.check(node, self.errors)
        UsingFilterNotAllowed.check(node, self.errors)
        AnyWithCompNotAllowed.check(node, self.errors)
        self.generic_visit(node)

    def visit_FunctionDef(self, node: FunctionDef) -> Any:
        CamelCaseFuncNotAllowed.check(node, self.errors)
        DefaultMutableArgsNotAllowed.check(node, self.errors)
        self.generic_visit(node)

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        InheritsFromObjectNotAllowed.check(node, self.errors)
        self.generic_visit(node)

    def visit_Compare(self, node: ast.Compare) -> None:
        CompareTypesNotAllowed.check(node, self.errors)
        self.generic_visit(node)

    def visit_If(self, node: ast.If) -> None:
        ComparedToTrueNotAllowed.check(node, self.errors)
        NotUsingTernaryNotAllowed.check(node, self.errors)
        self.generic_visit(node)

    def visit_Assign(self, node: ast.Assign) -> None:
        ShadowBuiltinsNotAllowed.check(node, self.errors)
        self.generic_visit(node)

    def visit_IfExp(self, node: IfExp) -> None:
        NotPointlessTernaryNotAllowed.check(node, self.errors)
        self.generic_visit(node)
