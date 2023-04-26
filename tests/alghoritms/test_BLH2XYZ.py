from unittest import TestCase

from core.alghoritms.BLH2XYZ import BLH2XYZCoordinatesConverter
from core.model.ellipse import Ellipse


class TestBLH2XYZCoordinatesConverter(TestCase):

    def test_convert(self):

        elipsoid = Ellipse()
        elipsoid.set_system("GRS80")
        converter = BLH2XYZCoordinatesConverter(elipsoid)

        X_expected = 3860189.975998430
        Y_expected = 1404994.249881152
        Z_expected = 4862865.642048912

        X, Y, Z = converter.convert([0.872664626 ,  0.3490658504, 100])

        print(X, Y, Z)
        print(X_expected, Y_expected, Z_expected)

        self.assertAlmostEqual(X_expected, X, places=5)
        self.assertAlmostEqual(Y_expected, Y, places=5)
        self.assertAlmostEqual(Z_expected, Z, places=5)
