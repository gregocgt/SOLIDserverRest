
# from .Exception import *

import sys

if sys.version_info[0] == 2:
    from SOLIDserverRest import *
    from mapper import *
    from Exception import *
else:
    from .mapper import *
    from .SOLIDserverRest import *
    from .Exception import *
