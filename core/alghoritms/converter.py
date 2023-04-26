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
