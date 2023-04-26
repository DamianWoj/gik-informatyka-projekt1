import numpy as np

from core.alghoritms.converter import CoordinatesConverter
from core.model.ellipse import Ellipse


class BLH2XYZCoordinatesConverter(CoordinatesConverter):

    def __init__(self, elips: Ellipse):
        super().__init__(elips)
        self.mode = "BLH2XYZ"

    def convert(self, args):
        if len(args) == 3:
            B, L, H = args
        else:
            raise ValueError("Wrong number of arguments")
        N = self.a / (1 - self.e2 * (np.sin(B) ** 2)) ** 0.5
        X = (N + H) * np.cos(B) * np.cos(L)
        Y = (N + H) * np.cos(B) * np.sin(L)
        if H != 0:
            Z = (N * (1 - self.e2) + H) * np.sin(B)
            return X, Y, Z
        else:
            return X, Y
        pass
