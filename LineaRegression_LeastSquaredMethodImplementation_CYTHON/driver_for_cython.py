import LeastSquaredMethodImplementation

LeastSquaredMethodImplementation.wrapper()

# PyCharm can see LeastSquaredMethodImplementation.pyx but still returns:
# module 'LeastSquaredMethodImplementation' has no attribute 'wrapper'
# solution:
# https://stackoverflow.com/questions/26417762/python-cython-trouble-importing-files-and-methods

# But Still no result


# Cython code was only addition but still curious why not working
# .pyx file still interpretes proper python instructions
# Will try to finish in the future