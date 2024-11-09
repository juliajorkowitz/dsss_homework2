from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "math_quiz=math_quiz.math_quiz:main",  # `main` should be the entry function in `math_quiz.py`
        ],
    },
)
