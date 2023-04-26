from core.alghoritms.BLH2XYZ import BLH2XYZCoordinatesConverter
from core.alghoritms.converter import CoordinatesConverter
from core.model.ellipse import Ellipse


class BL2000CoordinatesConverter(CoordinatesConverter):

    def __init__(self, elips: Ellipse):
        super().__init__(elips)
        self.blh2xyz = BLH2XYZCoordinatesConverter(elips)
        self.mode = "BL2000"

    def convert(self, args):
        if len(args) == 2:
            B, L = args
        else:
            raise ValueError("Wrong number of arguments")
        x_GK, y_GK = self._bl2xyGK(B, L)
        m_0 = 0.999923
        zone = round(L / 3)
        x2000 = m_0 * x_GK
        y2000 = zone * 1_000_000 + m_0 * y_GK + 500_000
        return x2000, y2000
