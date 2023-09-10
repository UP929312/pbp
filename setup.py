from setuptools import setup, find_packages

setup(
    install_requires=["flake8 > 3.0.0"],
    name="flake8_pgp",
    license="MIT",
    version="1.1.2",
    description="flake8 plugin which checks for various bad python practises",
    # author="Ben Skerritt",
    # author_email="ben.skerrit@vodafone.com",
    url="https://github.com/UP929312/pbp",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Framework :: Flake8",
    ],
    entry_points={
        'flake8.extension': [
            'PBP1 = src.flake8_pbp:ProduceBetterPythonPlugin',
        ],
    },
)