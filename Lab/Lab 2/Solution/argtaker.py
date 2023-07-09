import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--stdId", "-id", help="Student Id to show", type=str)
args = parser.parse_args()