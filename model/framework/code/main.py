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

start = time.time()
def my_model(smiles_list):
    return {smi:translate_forward(smi) for smi in smiles_list}

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
    writer.writerow(["smiles", "iupacs_names"]) # header
    for i, o in iupacs_names.items():
        writer.writerow([i, o])

print("Time taken for per prediction is {} sec\n".format((time.time() - start) / 100))