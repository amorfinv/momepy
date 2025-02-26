import momepy.datasets

from .coins import *
from .dimension import *
from .distribution import *
from .diversity import *
from .elements import *
from .graph import *
from .intensity import *
from .preprocessing import *
from .shape import *
from .utils import *
from .weights import *

__author__ = "Martin Fleischmann"
__author_email__ = "martin@martinfleischmann.net"

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions
