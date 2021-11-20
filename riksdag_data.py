import xml.etree.ElementTree as ET
import os
import glob
import csv
import pandas as pd


#parses xml file, returns [(party, speech), (party, speech)...]
def parser(textfile):
    tree = ET.parse(textfile)

    root = tree.getroot()
    parti = root.findall("parti")
    anf = root.findall("anforandetext")
    datum = root.findall("dok_datum")

    listofwords = []
    listofparty = []
    listofdatum = []


    for x in anf:
        print(x)
        if x is not None:
            try:
                listofwords.append(x.text.replace("\n"," "))   
            except (TypeError, AttributeError):
                listofwords.append("No speech")

        for x in parti:
            try:
                listofparty.append(x.text)
            except (TypeError, AttributeError):
                listofparty.append("No party")

        for x in datum:
            listofdatum.append(x.text)

    party_and_speech = zip(listofparty, listofwords, listofdatum)

    

    return party_and_speech


#finds files in "data" ending with xml, returns dataframe
def findfile():
    xmlfinder = glob.glob("./data/*.xml")

    all_speeches = []

    for x in xmlfinder:
        with open(x) as f:
            f = parser(f)
            for item in f:
                #print(item)
                all_speeches.append(item)
    
    
    
    df = pd.DataFrame(all_speeches, columns = ["Party", "Speech", "Date"])
    
    
    return df
    return 0



df = findfile()
df.to_csv("speeches_as_csv.csv")


import torch

