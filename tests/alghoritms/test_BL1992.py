from unittest import TestCase

from core.alghoritms.BL1992 import BL1992CoordinatesConverter
from core.model.ellipse import Ellipse


class TestCoordinatesConverter(TestCase):

    def test_convert_GRS80(self):

        elips = Ellipse()
        elips.set_GRS80()

        converter = BL1992CoordinatesConverter(elips)

        result = converter.convert([0.872664626, 0.3490658504])

        expected_x = 237447.41757088713
        expected_y = 571644.9347992322

        print(result)
        print(expected_x, expected_y)

        self.assertAlmostEqual(result[0], expected_x, places=2)
        self.assertAlmostEqual(result[1], expected_y, places=2)
