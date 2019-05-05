#!/usr/bin/env python3
import argparse
from matplotlib import pyplot as plt
import analyze, rend
import HPLResult

HPLOutputFile = "HPL.out"

if __name__ == "__main__":
    # Set up argument values
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--numCores", type = int, action = "append", help = "Number of cores in one trial. Repeat as many times as necessary for each trial. (required)", required = True)
    parser.add_argument("-t", "--title", help = "Title for this run")
    parser.add_argument("-l", "--loglog", action = "store_true", help = "Plot a log-log graph")
    parser.add_argument("inputTemplate", help = "The template to use for the directory name, with the number of cores replaced by '{}'.")
    args = parser.parse_args()

    functionThatYields = lambda n: (lambda x: n) # Create a function that yields a function that returns n.
    statFunc = HPLResult.NameToGetter.get("time")
    args.numCores.sort()

    # Process data
    binnedResults = {}
    for numCores in args.numCores:
        binnedResults.update(analyze.binResultsBy(rend.rendData(args.inputTemplate.format(numCores) + "/" + HPLOutputFile), functionThatYields(numCores)))
    minMaxAvg = analyze.minMaxAvgPerBin(binnedResults, statFunc)

    # Break averages into their own lists
    bins = list(minMaxAvg.keys())
    averages = [x[analyze.MMAAvg] for x in minMaxAvg.values()]
    # Get graph labels
    xLabel = "Number of Cores"
    yLabel = "Time to Solve"
    title = "{} vs. {}".format(yLabel, xLabel)
    if args.title:
        title += " ({})".format(args.title)

    # Plot results and display graph
    if args.loglog:
        plt.loglog(bins, averages, label = "Average")
    else:
        plt.plot(bins, averages, label = "Average")
    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.legend()
    plt.show()
