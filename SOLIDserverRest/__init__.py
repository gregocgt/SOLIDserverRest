# from .Exception import *

"""
init of the SOLIDserver module
"""

import sys

if sys.version_info[0] == 2:
    from SOLIDserverRest import *
    from mapper import *
    from Exception import *
else:
    from .mapper import *
    from .SOLIDserverRest import *
    from .Exception import *
