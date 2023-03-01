"""ex_5_1.py"""
import sys
import argparse
try:
    from src.ex_5_0 import line_count
except ImportError:
    from ex_5_0 import line_count


def main(infile):
    """Call line_count with the infile argument."""
    line_count(infile)


if __name__ == "__main__" and sys.stdin.isatty():
    # Create your argument parser object here.
    # Collect the filename argument from the command line
    # pass this argument to the main function above
    # Tests will run your command using a system call.
    # To test your program with arguments, run it from the command line
    # (see README.md for more details)
    parser = argparse.ArgumentParser(description='This program prints the number of lines in infile.')
    parser.add_argument('infile', help='input file name',nargs='?')
    args = parser.parse_args()
    if args.infile:
        main(args.infile)
