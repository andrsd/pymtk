import struct
import math
import sys


def loop(fld):
    """
    This starts the loop that will feed element sizes into GMSH using
    `ExternalProcess` field (see [1] for details)

    [1] https://gmsh.info/doc/texinfo/gmsh.html#index-ExternalProcess

    :param fld: Field that provides element size via call operator
    """

    while True:
        xyz = struct.unpack("ddd", sys.stdin.buffer.read(24))
        if math.isnan(xyz[0]):
            break
        if fld.dimension == 2:
            f = fld(xyz[0], xyz[1])
        elif fld.dimension == 3:
            f = fld(xyz[0], xyz[1], xyz[2])
        else:
            raise SystemError(f"Unsupported dimension {fld.dimension}")
        sys.stdout.buffer.write(struct.pack("d", f))
        sys.stdout.flush()
