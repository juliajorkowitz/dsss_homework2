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
)
