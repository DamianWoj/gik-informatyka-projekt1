
class Ellipse:

    def __init__(self):
        self.a = None
        self.e2 = None
        self.name = None


    def set_GRS80(self):
        self.a = 6_378_137
        self.e2 = 0.00669438002290
        self.name = "GRS80"

    def set_system(self, system_name):
        if system_name == "GRS80":
            self.set_GRS80()
        else:
            raise ValueError("Unknown system name")
