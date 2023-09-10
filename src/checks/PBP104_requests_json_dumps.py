import ast

from src.flake_8_ast_error import PREFIX, Flake8ASTErrorInfo


class RequestsJsonDumpsNotAllowed:
    """
    # Bad
    import json
    requests.post(data=json.dumps(data))

    # Good
    requests.post(json=data)
    """

    msg = PREFIX + "04: Don't use requests.post(data=json.dumps(data)), use requests.post(json=data) instead"

    @classmethod
    def check(cls, node: ast.Call, errors: list[Flake8ASTErrorInfo]) -> None:
        is_requests_call = (
            isinstance(node.func, ast.Attribute) and
            isinstance(node.func.value, ast.Name) and
            node.func.value.id == "requests"
        )
        if not is_requests_call:
            return
        # =================================================================================
        # From now on, we're only checking for requests.x() calls
        data = [x for x in node.keywords if x.arg == "data"]
        if not data:
            return
        data = data[0]

        if not (isinstance(data.value, ast.Call) and isinstance(data.value.func, ast.Attribute)):
            return
        # ================================================================================
        # From now on, we're only checking for data=<x> calls
        attribute = data.value.func
        if (
            isinstance(attribute.value, ast.Name) and
            attribute.value.id == "json" and
            attribute.attr == "dumps"
        ):
            errors.append(Flake8ASTErrorInfo(node.lineno, node.col_offset, cls.msg, type(cls)))


"""
Call(
    func=Attribute(
        value=Name(id='requests', ctx=Load()),
        attr='post',
        ctx=Load()),
    args=[
        Constant(value='<url>')],
    keywords=[
        keyword(
            arg='data',
            value=Call(
                func=Attribute(
                    value=Name(id='json', ctx=Load()),
                    attr='dumps',
                    ctx=Load()),
                args=[
                    Name(id='<data>', ctx=Load())],
                    keywords=[]))
    ])),
"""
