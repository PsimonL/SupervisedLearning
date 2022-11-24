from setuptools import setup
from Cython.Build import cythonize

# https://www.youtube.com/watch?v=Ic1oE6SEOBs&t=149s
# https://cython.readthedocs.io/en/latest/src/tutorial/cython_tutorial.html

# Create code with .pyx

# In the terminal to compile c/c++ code into binary:
# python setup.py build_ext --inplace

# After code generations we dont need .pyx file, could be deleted

setup(
    ext_modules=cythonize("LeastSquaredMethodImplementation.pyx")
)
