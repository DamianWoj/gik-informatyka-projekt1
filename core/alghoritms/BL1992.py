from core.alghoritms.converter import CoordinatesConverter
from core.model.ellipse import Ellipse


class BL1992CoordinatesConverter(CoordinatesConverter):

    def __init__(self, elips: Ellipse):
        super().__init__(elips)
        self.mode = "BL1992"

    def convert(self, args):
        if len(args) == 2:
            B, L = args
        else:
            raise ValueError("Wrong number of arguments")
        x_GK, y_GK = self._bl2xyGK(B, L)
        m_0 = 0.9993
        x1992 = m_0 * x_GK - 5_300_000
        y1992 = m_0 * y_GK + 500_000
        return x1992, y1992
