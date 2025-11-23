from setuptools import setup

# Available at setup time due to pyproject.toml
from pybind11.setup_helpers import Pybind11Extension, build_ext

ext_modules = [
    Pybind11Extension("concat_module",
        ["concat.cpp"],
        # Example: passing in the version to the compiled code
        define_macros = [('VERSION_INFO', '"1.0"')],
    ),
]

setup(
    name="concat_module",
    version="1.0",
    author="Me",
    author_email="me@example.com",
    description="A test project using pybind11",
    long_description="",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.6",
)
