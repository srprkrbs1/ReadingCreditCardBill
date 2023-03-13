import os
import pandas as pd
from tabula import read_pdf
import tabula
from utility import *

exclude = ["TARİHİ AÇIKLAMA", "BİR ÖNCEKİ HESAP ÖZETİ BAKİYENİZ", "ATMDEN ÖDEME", "KALAN DÖNEM:", "İADE"]


def isExcluded(text):
    for e in exclude:
        if e in text:
            return True
    return False


def parse_IsBankasi(filename: str):
    data = read_pdf(filename, pages="all")
    data = data[0]
    data.to_csv("example.tsv", index=False, header=None, sep='\t')

    output = []
    for line in readTextFile("example.tsv"):
        if not isExcluded(line):
            line = line.split("\t")
            desc = line[0]
            desc = desc[11:]
            line.pop(0)
            line = [l for l in line if len(l) > 0]
            line = line[0]
            line = float(line.replace(",", "."))
            if line > 0.0:
                output.append((desc, line))
    #: Delete the tsv file
    os.remove("example.tsv")
    #: Return
    return output


x = parse_IsBankasi("is-bankasi.pdf")
for key,value in x:
    print(str(key).lstrip(),":",value)