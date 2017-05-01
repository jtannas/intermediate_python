"""
22. Targeting Python 2+3

In a lot of cases you might want to develop programs which can be run
in both Python 2+ and 3+.

Just imagine that you have a very popular Python module which is used
by hundreds of people but not all of them have Python 2 or 3. In that
case you have two choices. The first one is to distribute 2 modules,
one for Python 2 and the other for Python 3. The other choice is to
modify your current code and make it compatible with both Python 2 and 3.

In this section I am going to highlight some of the tricks which you can
employ to make a script compatible with both of them.
"""

### FUTURE IMPORTS ############################################################
#: Future imports allow you to import features from future versions of python.
#: This is useful for creating a module in Python2 and then importing the
#: features you want from Python3.
from __future__ import with_statement
from __future__ import print_function

### MODULE RENAMING ###########################################################
#: Some modules have alternate versions between Python2 and Python3. To
#: deal with this, you can alias modules as you import them. By
#: aliasing each to the same name, your code can reference the same name.
try:
    import urllib.request as urllib_request  # for Python 3
except ImportError:
    import urllib2 as urllib_request  # for Python 2

### DEPRECATED BUILTINS #######################################################
#: There are 12 Python2 builtins that have been removed from Python 3.
#: To prevent their use in a Python 2 project (so that they won't
#: cause incompatibility), you can import a module that overrides them.
from future.builtins.disabled import *

### EXTERNAL BACKPORTS ########################################################
#: There are a few packages in the wild to provide certain Python 3
#: functionality in Python 2
#:      enum : pip install enum34
#:      singledispatch : pip install singledispatch
#:      pathlib : pip install pathlib