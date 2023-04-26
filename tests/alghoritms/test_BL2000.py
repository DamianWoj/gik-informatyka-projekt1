from unittest import TestCase

from core.alghoritms.BL2000 import BL2000CoordinatesConverter
from core.model.ellipse import Ellipse


class TestBL2000CoordinatesConverter(TestCase):
    def test_convert(self):

        elips = Ellipse()
        elips.set_GRS80()

        converter = BL2000CoordinatesConverter(elips)

        result = converter.convert([0.872664626, 0.3490658504])

        expected_x = 5540899.6638844535
        expected_y = 571689.6008598545

        print(result)
        print(expected_x, expected_y)

        self.assertAlmostEqual(result[0], expected_x, places=2)
        self.assertAlmostEqual(result[1], expected_y, places=2)
