import numpy as np

from core.alghoritms.converter import CoordinatesConverter
from core.model.ellipse import Ellipse


class XYZ2BLHCoordinatesConverter(CoordinatesConverter):

    def __init__(self, elips: Ellipse):
        super().__init__(elips)
        self.mode = "XYZ2BLH"

    def convert(self, args):
        if len(args) == 3:
            X, Y, Z = args
        else:
            raise ValueError("Wrong number of arguments")

        rp = (X ** 2 + Y ** 2) ** 0.5
        Bprev = np.arctan(Z / rp)
        while True:
            ck = self.e2 * np.sin(Bprev)
            deltak = self.a * self.e2 * ck / (1 - ck ** 2) ** 0.5
            Bknext = np.arctan((Z + deltak) / rp)

            if abs(Bknext - Bprev) > 0.0000000000001:
                Bprev = Bknext
            else:
                break

        L = np.arccos(X / rp)

        Rn = self.a / (1 - self.e2 * (np.sin(Bknext) ** 2)) ** 0.5
        dr = rp - Rn * np.sin(Bknext)

        # TODO H do poprawy
        dz = Z - Rn * np.cos(Bknext)  # tutaj niby "+ d" ale nie wiem co to jest d
        H = (dr ** 2 + dz ** 2) ** 0.5
        if dr < 0 or dz < 0:
            H *= -1
        return Bknext, L, H
