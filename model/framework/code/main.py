# imports
import os
import csv
import sys
from stout import translate_forward
import time

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

def my_model(smiles_list):
    for smi in smiles_list:
        print("smi")
        translate_forward(smi)
    return 

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader) # skip header
    smiles_list = [r[0] for r in reader]

# run model
iupacs_names = my_model(smiles_list)

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["iupacs_names"]) # header
    for o in iupacs_names:
        writer.writerow([o])