from pandas import *
import funcs as f
from smiles_string_class import SmilesString


def main():
    data = read_csv("dataset.csv")
    smiles = data['smiles'].tolist()
    for i in smiles:
        smiles_object = SmilesString(i)
        print(i + ' '+ str(smiles_object.validate()))

main()