
import os
import pandas as pd
from tabula import read_pdf
from utility import *

exclude = ["Hesap Özeti Dönemi :", "Toplam Dönem Alışveriş Tutarı :", "Toplam Dönem Nakit Çekim Tutarı :","ALIŞVERİŞ İŞLEMLERİ", "Kart Numarası", "İşlem Tarihi İşlemler"]

def yapiKrediExcluded(text):
    for e in exclude:
        if e in text:
            return True
    return False

def parse_YapiKredi(filename: str):
    data = read_pdf(filename, pages="all")
    data = data[0]
    data.to_csv("example.tsv", index=False, header=None, sep='\t')

    output = []
    for line in readTextFile("example.tsv"):
        if not yapiKrediExcluded(line):
            line = line.split("\t")
            desc = line[0]
            desc = desc[15:].strip()
            line.pop(0)
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

x = parse_YapiKredi("yapi-kredi.pdf")
for key,value in x:
    print(str(key).lstrip(),":",value)
    


