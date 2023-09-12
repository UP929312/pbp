from setuptools import setup, find_packages

setup(
    install_requires=["flake8 > 3.0.0"],
    name="flake8_pbp",
    license="MIT",
    version="1.0.11",
    description="flake8 plugin which checks for various bad python practises",
    long_description="flake8 plugin which checks for various bad python practises",
    url="https://github.com/UP929312/pbp",
    packages=find_packages(),
    classifiers=[
        "Framework :: Flake8",
    ],
    entry_points={
        "flake8.extension": [
            "PBP1 = src.flake8_pbp:ProduceBetterPythonPlugin",
        ],
    },
)
