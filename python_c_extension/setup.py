from setuptools import setup, Extension

module1 = Extension(
    'spam',
    sources=['spammodule.c']
)
setup(
    ext_modules=[module1]
)