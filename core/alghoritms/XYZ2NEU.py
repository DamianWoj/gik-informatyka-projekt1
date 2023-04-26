import numpy as np

from core.alghoritms.XYZ2BLH import XYZ2BLHCoordinatesConverter
from core.alghoritms.converter import CoordinatesConverter
from core.model.ellipse import Ellipse


class XYZ2NEUCoordinatesConverter(CoordinatesConverter):

    def __init__(self, elips: Ellipse):
        super().__init__(elips)
        self.xyz2blh = XYZ2BLHCoordinatesConverter(elips)
        self.mode = "XYZ2NEU"

    def convert(self, args):
        if len(args) == 6:
            X, Y, Z, X0, Y0, Z0 = args
        else:
            raise ValueError("Wrong number of arguments")

        B, L, H = self.xyz2blh.convert([X0, Y0, Z0])
        R = np.array([[-np.sin(L), -np.sin(B) * np.cos(L), np.cos(B) * np.cos(L)],
                      [np.cos(L), -np.sin(B) * np.sin(L), np.cos(B) * np.sin(L)],
                      [0, np.cos(B), np.sin(B)]])
        XYZ0 = np.array([X - X0, Y - Y0, Z - Z0])
        XYZ = np.dot(R, XYZ0)
        return XYZ[0], XYZ[1], XYZ[2]
