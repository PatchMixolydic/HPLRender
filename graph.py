#!/usr/bin/env python3
import argparse
from matplotlib import pyplot as plt
import analyze, rend
import HPLResult

if __name__ == "__main__":
    # Set up argument values
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help = "HPL output file to analyze")
    parser.add_argument("-b", "--bin", help = "The result property used for binning the output (required)", choices = HPLResult.GetterCommandLineNames, required = True)
    parser.add_argument("-s", "--statistic", help = "The result property used for finding the best bin on average (required)", choices = HPLResult.GetterCommandLineNames, required = True)
    parser.add_argument("-v", "--verbose", action = "store_true", help = "When used, outputs the results sorted into bins")
    parser.add_argument("-t", "--title", help = "Title for this run")
    args = parser.parse_args()
    binFunc = HPLResult.NameToGetter.get(args.bin)
    statFunc = HPLResult.NameToGetter.get(args.statistic)

    # Process data
    binnedResults = analyze.binResultsBy(rend.rendData(args.input), binFunc)
    minMaxAvg = analyze.minMaxAvgPerBin(binnedResults, statFunc)

    # Break minimums, averages, and maximums into their own lists
    bins = list(minMaxAvg.keys())
    mins = [x[analyze.MMAMin] for x in minMaxAvg.values()]
    maxxes = [x[analyze.MMAMax] for x in minMaxAvg.values()]
    averages = [x[analyze.MMAAvg] for x in minMaxAvg.values()]

    # Get graph labels
    xLabel = HPLResult.NameToDisplayName.get(args.bin)
    yLabel = HPLResult.NameToDisplayName.get(args.statistic)
    title = "{} vs. {}".format(yLabel, xLabel)
    if args.title:
        title += " ({})".format(args.title)

    # Plot results and display graph
    plt.plot(bins, mins, label = "Minimum")
    plt.plot(bins, averages, label = "Average")
    plt.plot(bins, maxxes, label = "Maximum")
    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.legend()
    plt.show()
