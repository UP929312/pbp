import requests

condition = True
my_list = [1, 2, 3]
my_map = {1: "a", 2: "b"}
my_sub_list = [4, 5, 6]

# ========== RangeLenNotAllowed

# Bad
for i in range(len(my_list)):
    print(my_list[i])

# Good
for x in list:
    print(x)
for _ in range(len(my_list)):
    ...

# ========== JsonLoadsNotAllowed

# Bad
import json
response = requests.get("https://example.com")
data = json.loads(response.text)

# Good
response = requests.get("https://example.com").json()

# ========== OpenNoWithNotAllowed

# Bad
file = open("file.txt")
file.read()
file.close()

# Good
with open("file.txt") as file:
    data = file.read()

# ========== RequestsJsonDumpsNotAllowed

# Bad
import json
requests.post(data=json.dumps(data))

# Good
requests.post(json=data)

# ========== AssignToListNotAllowed

# Bad
x = list()

# Good
x = []

# ========== CamelCaseFuncNotAllowed

# Bad
def CamelCaseFunc():
    pass

# Good
def snake_case_func():
    pass

# ========== DefaultMutableArgsNotAllowed

# Bad
def foo(bar=[]):
    pass

# Good
def foo(bar=None):
    if bar is None:
        bar = []
    pass

# ========== CompareTypesNotAllowed

# Bad
if type(x) == int:
    pass
if type(x) is int:
    pass

# Good
if isinstance(x, int):
    pass

# ========== ComparedToTrueNotAllowed

# Bad
if x is True:
    pass

# Good
if x:
    pass

# ========== InheritsFromObjectNotAllowed

# Bad
class Foo(object):
    pass

# Good
class Foo:
    pass

# ========== NotUsingTernaryNotAllowed

# Bad
if x == 1:
    a = "Value1"
else:
    a = "Value2"

# Good
a = "Value1" if x == 1 else "Value2"

# ========== UsingFilterOrMapNotAllowed

# Bad
list(filter(lambda x: x > 5, range(10)))
list(map(lambda x: x**2, range(10)))

# Good
[x for x in range(10) if x > 5]
[x**2 for x in range(10)]

# ========== ShadowBuiltinsNotAllowed

# Bad
map = ...
list = ...

# Good
my_map = ...
my_list = ...

# ========== NoPointlessTernaryNotAllowed

# Bad
x = True if condition else False

# Good
x = bool(condition)

# ========== AnyOrAllWithCompNotAllowed

# Bad
any([x.id for x in my_list])
all([x.id for x in my_list])

# Good
all(x.id for x in my_list)
any(x.id for x in my_list)

# ========== NonPascalCaseClassNotAllowed

# Bad
class my_class:
    pass

# Good
class MyClass:
    pass

# ========== NonUsingListCompNotAllowed

# Bad
my_list = []
for char in my_sub_list:
    my_list.append(char)

# Good
my_list = [x for x in my_sub_list]

