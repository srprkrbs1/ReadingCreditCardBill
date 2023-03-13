import os
import pandas as pd
from tabula import read_pdf
import tabula
from utility import *

exclude = ["bosluk", "bos", "MILES&SMILES PROGRAM ORTAKLARI DIŞI HARCAMALARINIZ", "GİYİM", "DİĞER"]


def garantiExcluded(text):
    for e in exclude:
        if e in text:
            return True
    return False


def parse_Garanti(filename: str):
    data = read_pdf(filename, pages="all")
    data = data[0]
    data.to_csv("example.tsv", index=False, header=None, sep='\t')

    output = []
    for line in readTextFile("example.tsv"):
        if not garantiExcluded(line):
            line = line.split("\t")
            desc = line[1]
            desc = desc[15:]
            line.pop(0)
            line.pop(0)
            line.pop(0)
            line.pop(0)
            line = [l for l in line if len(l) > 0]
            line = line[0]
            line = line.replace(".", "")
            line = float(line.replace(",", "."))
            if line > 0.0:
                output.append((desc, line))
    #: Delete the tsv file
    os.remove("example.tsv")
    #: Return
    return output


x = parse_Garanti("garanti.pdf")
for key,value in x:
    print(str(key).lstrip(),":",value)
    