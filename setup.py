from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as readme_file:
    readme = readme_file.read()

name = "gtimeit"

version = "0.0.5"

description = "Timer, benchmark and ressource usage tracker. A tool for python functions. Time and compare your functions inside or outside a program."

long_description = """
# gtimeit
Timer, benchmark and ressource usage tracker.
A tool for python functions. Time and compare your functions inside or outside a program.

## Benchmark

Allows to run multiple python functions a certain amount of times and to compare there respective execution times.
Similar to [timeit](https://docs.python.org/2/library/timeit.html) Display curves of all the execution times.
Prototype : benchmarking for complexity tests up to one variable parameter. The variable take all the values of a given range and the benchmarck keeps track of the executions times.

## Tracker
Allow to keep track of the execution time of some functions in a program. Useful to know which part of your program take the more time to execute.

Read the README at https://github.com/Chthi/gtimeit for more information.
"""


requirements = ["numpy>=1.18.2", "matplotlib>=3.2.1"]
extras_requirements = []


setup(
    name=name,
    version=version,
    author="Thibault Charmet",
    author_email="",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Chthi/gtimeit",
    project_urls={},
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    py_modules=[],
    entry_points={
        # "console_scripts": [
            # package=module.file:function
            # "gtimeit=gtimeit.__main__:main",
        # ]
    },
    python_requires='>=3.6',
    install_requires=requirements,
    # extras_require=extras_requirements,
    include_package_data=True,
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Development Status :: 3 - Alpha",
    ],
    keywords='time benchmark track plot compare',
)
