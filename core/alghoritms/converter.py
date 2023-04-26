from abc import ABC, abstractmethod

from core.model.ellipse import Ellipse
import numpy as np


class CoordinatesConverter(ABC):

    def __init__(self, elips: Ellipse):
        self.a = elips.a
        self.e2 = elips.e2

    @abstractmethod
    def convert(self, *args):
        pass

    def _bl2xyGK(self, B, L):
        delta_l = L - 19 * np.pi / 180
        t = np.tan(B)
        n = self.e2 * np.cos(B) ** 2
        N = self.a / np.sqrt(1 - self.e2 * np.sin(B) ** 2)

        A0 = 1 - self.e2 / 4 - 3 * self.e2 ** 2 / 64 - 5 * self.e2 ** 3 / 256
        A2 = 3 / 8 * (self.e2 + self.e2 ** 2 / 4 + 15 * self.e2 ** 3 / 128)
        A4 = 15 / 256 * (self.e2 ** 2 + 3 * self.e2 ** 3 / 4)
        A6 = 35 * self.e2 ** 3 / 3072

        sigma = self.a * (A0 * B - A2 * np.sin(2 * B) + A4 * np.sin(4 * B) - A6 * np.sin(6 * B))

        x_GK = sigma + (delta_l ** 2 / 2) * N * np.sin(B) * np.cos(B) * \
               (1 + (delta_l ** 2 / 12) * np.cos(B) ** 2 * (5 - t ** 2 + 9 * n ** 2 + 4 * n ** 4)
                + (delta_l ** 4 / 360) * np.cos(B) ** 4 * (
                        61 - 58 * t ** 2 + t ** 4 + 270 * n ** 2 - 330 * n ** 2 * t ** 2))

        y_GK = delta_l * N * np.cos(B) * (1 + (delta_l ** 2 / 6) * np.cos(B) ** 2 * (1 - t ** 2 + n ** 2)
                                          + (delta_l ** 4 / 120) * np.cos(B) ** 4 *
                                          (5 - 18 * t ** 2 + t ** 4 + 14 * n ** 2 - 58 * n ** 2 * t ** 2))
        return x_GK, y_GK
