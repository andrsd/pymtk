import matplotlib as mpl
import matplotlib.tri
import meshio


class BackgroundMesh2D:
    """
    Base class for defining a background mesh in 2D

    Users are supposed to inherit from this class and implement the `value`
    method
    """

    def __init__(self):
        pass

    @property
    def dimension(self):
        """
        Spatial dimension of the field

        :return: Spatial dimension of the field
        """
        return 2


class TriMesh2D(BackgroundMesh2D):
    """
    This builds a triangular mesh and puts values in the mesh nodes. Then the
    values are linearly interpolated
    """

    def __init__(self, data):
        """
        Build a 2D spatial function interpolation (piecewise linear)

        :param data: List of ([x, y], area) tuples, where `x` is an
            x-coordinate, `y` is a y-coordinate, and `area` is the desired size
            of an element
        """
        super().__init__()
        x = list(map(self.__get_x, data))
        y = list(map(self.__get_y, data))
        self.tri_obj = mpl.tri.Triangulation(x, y)

        area = list(map(self.__get_area, data))

        points = list(map(self.__get_point, data))
        cells = [
            ("triangle", self.tri_obj.triangles)
        ]
        self._mesh = meshio.Mesh(points, cells, point_data={"A": area})

    def __get_x(self, a):
        return self.__get_point(a)[0]

    def __get_y(self, a):
        return self.__get_point(a)[1]

    def __get_point(self, a):
        return a[0]

    def __get_area(self, a):
        return a[1]
