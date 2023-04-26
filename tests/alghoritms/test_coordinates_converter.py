from unittest import TestCase

from core.alghoritms.BLH2XYZ import BLH2XYZCoordinatesConverter
from core.model.ellipse import Ellipse


class TestCoordinatesConverter(TestCase):
    def test__bl2xy_gk(self):
        elipsoid = Ellipse()
        elipsoid.set_system("GRS80")
        converter = BLH2XYZCoordinatesConverter(elipsoid)

        xGk_expected = 5541326.346140075
        yGk_expected = 71695.12555877925

        xGk, yGk = converter._bl2xyGK(0.872664626, 0.3490658504)

        print(xGk, yGk)
        print(xGk_expected, yGk_expected)

        self.assertAlmostEqual(xGk, xGk_expected, 2)
        self.assertAlmostEqual(yGk, yGk_expected, 2)
