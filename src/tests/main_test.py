import requests
import requests

condition = True
my_list = [1, 2, 3]
my_map = {1: 'a', 2: 'b'}# RangeLenNotAllowed

for i in range(len(my_list)):
    print(my_list[i])

for x in list:
    print(x)

# JsonLoadsNotAllowed

import json
response = requests.get("https://example.com")
data = json.loads(response.text)

response = requests.get("https://example.com").json()

# OpenNoWithNotAllowed

file = open("file.txt")
file.read()
file.close()

with open("file.txt") as file:
    data = file.read()

# RequestsJsonDumpsNotAllowed

import json
requests.post(data=json.dumps(data))

requests.post(json=data)

# AssignToListNotAllowed

x = list()

x = []

# CamelCaseFuncNotAllowed

def CamelCaseFunc():
    pass

def snake_case_func():
    pass

# DefaultMutableArgsNotAllowed

def foo(bar=[]):
    pass

def foo(bar=None):
    if bar is None:
        bar = []
    pass

# CompareTypesNotAllowed

if type(x) == int:
    pass
if type(x) is int:
    pass

if isinstance(x, int):
    pass

# ComparedToTrueNotAllowed

if x is True:
    pass

if x:
    pass

# InheritsFromObjectNotAllowed

class Foo(object):
    pass

class Foo:
    pass

# NotUsingTernaryNotAllowed

if x == 1:
    a = "Value1"
else:
    a = "Value2"

a = "Value1" if x == 1 else "Value2"

# UsingFilterNotAllowed

list(filter(lambda x: x > 5, range(10)))
list(map(lambda x: x**2, range(10)))

[x for x in range(10) if x > 5]
[x**2 for x in range(10)]

# ShadowBuiltinsNotAllowed

map = my_map
list = my_list

my_map = my_map
my_list = my_list

# NotPointlessTernaryNotAllowed

x = True if condition else False

x = bool(condition)

# AnyWithCompNotAllowed

any([x.id for x in my_list])
all([x.id for x in my_list])

all(x.id for x in my_list)
any(x.id for x in my_list)

# NonPascalCaseClassNotAllowed

class my_class:
    pass

class MyClass:
    pass

