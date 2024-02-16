from abc import ABC, abstractmethod
import matplotlib as mpl


class BackgroundMesh2D(ABC):
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

    @abstractmethod
    def value(self, x, y):
        """
        Evaluate the field defining the background mesh at spatial location
        (x, y)

        :param x: x-coordinate
        :param y: y-coordinate
        :return: Value of the field
        """
        pass

    def __call__(self, x, y):
        """
        Evaluate the field defining the background mesh at spatial location
        (x, y)

        :param x: x-coordinate
        :param y: y-coordinate
        :return: Value of the field
        """
        return self.value(x, y)


class TriMesh2D(BackgroundMesh2D):
    """
    This builds a triangular mesh and puts values in the mesh nodes. Then the
    values are linearly interpolated
    """

    def __init__(self, data):
        """
        Build a 2D spatial function interpolation (piecewise linear)

        :param data: (3, n) array. 0th index is x-coordinate, 1st index is
            y-coordinate, 2nd index is a function value
        """
        super().__init__()
        self.tri_obj = mpl.tri.Triangulation(data[0, :], data[1, :])
        self.ipol = mpl.tri.LinearTriInterpolator(self.tri_obj, data[2, :])

    def value(self, x, y):
        return self.ipol(x, y)
