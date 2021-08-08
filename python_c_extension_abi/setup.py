from setuptools import setup, Extension

module1 = Extension(
    'spam2',
    sources=['spammodule.c'],
    py_limited_api=True,
    define_macros=[('Py_LIMITED_API', 0x03060000)]
)
setup(
    ext_modules=[module1]
)
