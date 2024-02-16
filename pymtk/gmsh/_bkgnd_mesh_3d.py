from abc import ABC, abstractmethod


class BackgroundMesh3D(ABC):
    """
    Base class for defining a background mesh in 3D

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
        return 3

    @abstractmethod
    def value(self, x, y, z):
        """
        Evaluate the field defining the background mesh at spatial location
        (x, y, z)

        :param x: x-coordinate
        :param y: y-coordinate
        :param z: z-coordinate
        :return: Value of the field
        """
        pass

    def __call__(self, x, y, z):
        """
        Evaluate the field defining the background mesh at spatial location
        (x, y, z)

        :param x: x-coordinate
        :param y: y-coordinate
        :param z: z-coordinate
        :return: The value of the field
        """
        return self.value(x, y, z)
