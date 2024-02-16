"""
GMSH
"""

from ._loop import loop
from ._bkgnd_mesh_2d import (BackgroundMesh2D, TriMesh2D)
from ._bkgnd_mesh_3d import (BackgroundMesh3D)

__all__ = [
    "loop",
    # 2D
    "BackgroundMesh2D",
    "TriMesh2D",
    # 3D
    "BackgroundMesh3D"
]
