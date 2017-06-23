import sys

# https://stackoverflow.com/questions/15014310/why-is-there-no-xrange-function-in-python3
# Fix compat
if sys.version_info >= (3, 0):
    def xrange(*args, **kwargs):
        return iter(range(*args, **kwargs))