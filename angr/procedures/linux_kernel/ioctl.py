import errno
import angr
from ..posix.read import read
from ..posix.write import write
from ...sim_type import register_types, parse_types


class ioctl(angr.SimProcedure):
    def run(self, fd, request):
        return -errno.ENODEV
