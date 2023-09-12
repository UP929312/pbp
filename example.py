# Using loops
my_list = []
for char in "hello":
    my_list.append(char)

"""
Assign(
    targets=[
        Name(id='my_list', ctx=Store())],
    value=List(elts=[], ctx=Load())),
For(
    target=Name(id='char', ctx=Store()),
    iter=Constant(value='hello'),
    body=[
        Expr(
        value=Call(
            func=Attribute(
                value=Name(id='my_list', ctx=Load()),
                attr='append',
                ctx=Load()),
            args=[
                Name(id='char', ctx=Load())],
            keywords=[]))],
    orelse=[])],
"""