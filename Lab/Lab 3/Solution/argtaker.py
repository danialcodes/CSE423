import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--radius", "-r", help="Radius of the circle", type=int, default=200)
parser.add_argument("--centerX", "-cx", help="Center x of the circle", type=int, default=0)
parser.add_argument("--centerY", "-cy", help="Center y of the circle", type=int, default=0)
parser.add_argument("--innerCircle", "-ic", help="Center y of the circle", type=int, default=8)

args = parser.parse_args()