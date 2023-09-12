from src.checks import all_checks

final_string = "\n".join(
    [
        "import requests",
        "",
        "condition = True",
        "my_list = [1, 2, 3]",
        "my_map = {1: 'a', 2: 'b'}",
        "",
        "",
    ]
)

for check in all_checks:
    docs: str = check.__doc__.replace("\n    ", "\n")
    final_string += f"#========== {check.__name__}\n{docs}\n"

with open("src/tests/main_test.py", "w") as file:
    file.write(final_string)

print(r"flake8 --ignore=R,E,W,F .\src\tests\main_test.py")