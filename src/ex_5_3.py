""" ex_5_3.py
This module contains an entry point that:

- creates a CLi that accepts an input file of data to be processed
- shifts and scales the data to a mean of 0 and a standard deviation 1
- writes the file to the output file argument
"""
import numpy as np
from argparse import ArgumentParser
import os
try:
    from src.util import get_repository_root
except ImportError:
    from util import get_repository_root

if __name__ == "__main__":
    # Create your argument parser object here.
    parser = ArgumentParser(description = "This program applies a standard scale transform to the data in infile and writes it to outfile")
    # Collect the filename arguments from the command line
    parser.add_argument("infile",help="Input file",nargs="?")
    parser.add_argument("outfile",help="Output file",nargs="?")
    args = parser.parse_args()
    # Rewrite your 5_3 logic here so that it utilizes the arguments passed from the command line.
    inputdata = np.loadtxt(args.infile)
    normalized = (inputdata - inputdata.mean(axis=0)) / inputdata.std(axis=0)
    processed = normalized
    root_dir = get_repository_root()
    os.makedirs(root_dir / "outputs", exist_ok=True)
    np.savetxt(args.outfile, processed, fmt='%.2e')
    
