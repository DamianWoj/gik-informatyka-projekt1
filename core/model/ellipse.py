
class Ellipse:

    def __init__(self):
        self.a = None
        self.e2 = None
        self.name = None


    def set_GRS80(self):
        self.a = 6_378_137
        self.e2 = 0.00669438002290
        self.name = "GRS80"
            
    def set_WGS84(self):
        self.a = 6_378_137
        self.e2 = 1 / 298.257223563
        self.name = "WGS84"

    def set_Krasovsky(self):
        self.a = 6378245
        self.e2 = 1 / 298.3
        self.name = "Krasovsky"

    def set_system(self, system_name):
        if system_name == "GRS80":
            self.set_GRS80()
        elif system_name == "WGS84":
            self.set_WGS84()
        elif system_name == "krasovsky":
            self.set_Krasovsky()
        else:
            raise ValueError("Unknown system name")
