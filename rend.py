#!/usr/bin/env python3
import os, json
from HPLResult import HPLResult

HeaderLength = 1711 # characters

ResultEncodedTime = 0
ResultN = 1
ResultNB = 2
ResultP = 3
ResultQ = 4
ResultTime = 5
ResultGigaflops = 6

def getDataFilenames(directory):
    # get all output files in the given directory
    dataFilenames = []
    for _, __, filenames in os.walk(directory):
        for filename in filenames:
            if filename.split(".")[-1] != "out": # file extension is not .out
                continue
            dataFilenames.append(directory + filename)
    return dataFilenames

def rendData(filename):
    """
    Turns HPL data files into useable output.
    Note the name -- this is probably not the best way to do this.
    The best solution would probably involves regexes, which I don't know and
    probably can't learn in the short amount of time I've given myself.
    :return: A list of HPLResults containing data.
    """
    results = []
    with open(filename, 'r') as data:
        data.seek(0, 2) # seek to the end
        eof = data.tell() - 1 # get the eof location
        data.seek(HeaderLength, 0) # skip the header
        while data.tell() <= eof:
            line = data.readline()
            if not line.startswith("T/V"):
                continue # read until we hit a header
            data.readline() # skip a separator
            res = data.readline().split()
            start = " ".join(data.readline().split()[-5:]) # Start
            data.readline() # skip a separator
            end = " ".join(data.readline().split()[-5:]) # End
            results.append(HPLResult(
                res[ResultEncodedTime], int(res[ResultN]), int(res[ResultNB]), int(res[ResultP]),int(res[ResultQ]),
                float(res[ResultTime]), float(res[ResultGigaflops]), start, end
            ))
    return results

def rendAndOuputData(filename):
    """
    Rends the data and outputs it to a ".json" file
    (technically not json compliant due to containing multiple top-level objects)
    :return: A list of HPLResults containing data
    """
    outputFilename = filename.split(".")[0] + "_rended.json"
    rendedData = rendData(filename) # potential race condition wrt getDataFilenames
    with open(outputFilename, 'w') as out:
        out.write(json.dumps(rendedData.__dict__) + "\n")
    return rendedData
