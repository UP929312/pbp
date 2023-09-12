from src.checks import all_checks

final_string = "\n".join(
    [
        "import requests",
        "",
        "condition = True",
        "my_list = [1, 2, 3]",
        "my_map = {1: 'a', 2: 'b'}",
    ]
)

for check in all_checks:
    docs: str = check.__doc__.replace("\n    ", "\n")
    start, end = docs.split("# Good")
    good = end.strip("").strip("\n")
    bad = start.strip("").strip("\n").removeprefix("# Bad\n")

    final_string += f"# {check.__name__}\n\n{bad}\n\n{good}\n\n"

with open("src/tests/main_test.py", "w") as file:
    file.write("import requests\n"+final_string)

print(r"flake8 --ignore=R,E,W,F .\src\tests\main_test.py")