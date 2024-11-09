from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1.0",
    description="Math quiz game",
    author="Julia Jorkowitz",
    author_email="julia.jorkowitz@fau.de",
    url="https://github.com/juliajorkowitz/dsss_homework2.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[],  # List any dependencies your project needs, e.g., numpy
    entry_points={
        "console_scripts": [
            "math_quiz=math_quiz.math_quiz:math_quiz",  # Ensure this matches the function name in `math_quiz.py`
        ],
    },
)
