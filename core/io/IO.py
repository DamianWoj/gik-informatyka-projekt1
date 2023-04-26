import csv

from core.alghoritms.converter import CoordinatesConverter


class IO:

    def __init__(self, converter: CoordinatesConverter, file_name: str, delimiter: str = ";"):
        self.file_name = file_name
        self.converter = converter
        self.delimiter = delimiter
        self.system = None

    def read(self):
        out = {"headers": {"mode" : "", "system" : "", "args": ""}, "data": {}}
        with open(self.file_name, "r") as csv_file:
            data = csv.reader(csv_file, delimiter=self.delimiter)
            for row in enumerate(data):
                if row[0] == 0:
                    out["headers"]["mode"] = row[1][0]
                    out["headers"]["system"] = row[1][1]
                elif row[0] == 1:
                    out["headers"]["args"] = row[1]
                else:
                    out["data"][row[1][0]] = list(map(float, row[1][1:]))
        return out

    def write(self, out_file_name="./out.csv"):
        data = self.read()
        converted = []
        try:
            for i in data["data"]:
                labor = self.converter.convert(data["data"][i])
                converted.append([i, *labor])
        except ValueError as e:
            print(e)
            return

        with open(out_file_name, "w") as file:
            file.write(data["headers"]["mode"] + self.delimiter + data["headers"]["system"] + "\n")
            file.write(self.delimiter.join(data["headers"]["args"]) + "\n")
            for i in converted:
                file.write(self.delimiter.join(map(str, i)) + "\n")


if __name__ == "__main__":
    print("IO")
