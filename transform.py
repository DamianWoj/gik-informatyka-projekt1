import argparse

from core.alghoritms.BL1992 import BL1992CoordinatesConverter
from core.alghoritms.BL2000 import BL2000CoordinatesConverter
from core.alghoritms.BLH2XYZ import BLH2XYZCoordinatesConverter
from core.alghoritms.XYZ2BLH import XYZ2BLHCoordinatesConverter
from core.alghoritms.XYZ2NEU import XYZ2NEUCoordinatesConverter
from core.io.IO import IO
from core.model.ellipse import Ellipse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--system", "-S", choices=["GRS80", "WGS84", "krasovsky"], type=str, required=True,
                        help="Set one of available systems (GRS90, WGS84, krasovsky)")
    parser.add_argument("--mode", "-M", choices=["BLH2XYZ", "XYZ2BLH", "BL1992", "BL2000", "XYZ2NEU"], type=str,
                        required=True,
                        help="Set mode (BLH2XYZ (B, L - required), XYZ2BLH (X, Y, Z - required), BL1992 (B, "
                             "L - required), BL2000 (B, L - required), XYZ2NEU (X, Y, Z - required)")

    parser.add_argument("-B", type=float, required=False, help="Set B")
    parser.add_argument("-L", type=float, required=False, help="Set L")
    parser.add_argument("-H", type=float, required=False, help="Set H")
    parser.add_argument("-X", type=float, required=False, help="Set X")
    parser.add_argument("-Y", type=float, required=False, help="Set Y")
    parser.add_argument("-Z", type=float, required=False, help="Set Z")
    parser.add_argument("-X0", type=float, required=False, help="Set X0")
    parser.add_argument("-Y0", type=float, required=False, help="Set Y0")
    parser.add_argument("-Z0", type=float, required=False, help="Set Z0")
    parser.add_argument("-inp", type=str, required=False, help="Set relative input file path")
    parser.add_argument("-out", type=str, default="./out.csv", required=False, help="Set relative output file path")
    parser.add_argument("--delimiter", "-d", type=str, default=";", required=False,
                        help="Set delimiter of CSV file (default: ';')")
    args = parser.parse_args()
    
    ellipse = Ellipse()
    ellipse.set_system(args.system)

    mode_init = {"BLH2XYZ": [BLH2XYZCoordinatesConverter(ellipse), [args.B, args.L, args.H]],
                 "XYZ2BLH": [XYZ2BLHCoordinatesConverter(ellipse), [args.X, args.Y, args.Z]],
                 "BL1992": [BL1992CoordinatesConverter(ellipse), [args.B, args.L]],
                 "BL2000": [BL2000CoordinatesConverter(ellipse), [args.B, args.L]],
                 "XYZ2NEU": [XYZ2NEUCoordinatesConverter(ellipse), [args.X, args.Y, args.Z, args.X0, args.Y0, args.Z0]]}
