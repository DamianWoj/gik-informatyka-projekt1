from unittest import TestCase

from core.alghoritms.XYZ2NEU import XYZ2NEUCoordinatesConverter
from core.model.ellipse import Ellipse


class TestXYZ2NEUCoordinatesConverter(TestCase):
    def test_convert(self):

        elipsoid = Ellipse()
        elipsoid.set_system("GRS80")
        converter = XYZ2NEUCoordinatesConverter(elipsoid)

        N_expected = 268540.9270230197
        E_expected = -437151.6406011547
        U_expected = -695548.1389762581

        N, E, U = converter.convert([1000, 1000, 1000, 500000, 500000, 500000])

        print(N, E, U)
        print(N_expected, E_expected, U_expected)

        self.assertAlmostEqual(N_expected, N, places=5)
        self.assertAlmostEqual(E_expected, E, places=5)
        self.assertAlmostEqual(U_expected, U, places=5)
