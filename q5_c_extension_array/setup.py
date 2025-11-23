from setuptools import setup, Extension

module = Extension('array_manager', sources=['array_manager.c'])

setup(
    name='array_manager',
    version='1.0',
    description='A C extension for array management',
    ext_modules=[module]
)
