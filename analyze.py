#!/usr/bin/env python3
import argparse, pprint, statistics
from collections import defaultdict
import rend
import HPLResult

# For minMaxAvgPerBin
MMAMin = 0
MMAMax = 1
MMAAvg = 2

def binResultsBy(results, binningFunction):
    """
    Place results into bins depending on a binning function.
    :param results: A list of results to bin.
    :param binningFunction: The function to use to sort results into bins. You can use the getters in HPLResult for this.
    For example, to bin functions by NB, one should use HPLResult.getNB for the binningFunction.
    :return: A dictionary containing a list of results mapped to key values by the result of the binning function.
    """
    binnedResults = defaultdict(list) # if an invalid key is accessed, it defaults to being an empty list
    for result in results:
        binnedResults[binningFunction(result)].append(result) # using dict.get() here breaks the defaultdict behaviour
    return dict(binnedResults) # cast to dict - we don't need the default entry functionality anymore

def minMaxAvgPerBin(binnedResults, statFunction):
    """
    For each bin in the binned results, find the minimum, maximum, and average of the value of the results determined
    by statFunction. The constants MMAMin, MMAMax, and MMAAvg are meant for accessing the results tuple data.
    :param binnedResults: The binned HPLResults.
    :param statFunction: A function that will return a value given an HPLResult. This will most likely be a getter from
    HPLResult.
    :return: A dictionary containing a tuple with the min, max, and average value of the bin as given by statFunction.
    """
    results = {}
    for key, contents in binnedResults.items(): # Loop over all of the bins.
        contents = list(map(statFunction, contents)) # Process their contents with statFunction.
        results[key] = (min(contents), max(contents), statistics.mean(contents)) # Minimum, maximum, average
    return results

def getBestBin(binnedResults, statFunction, lowerIsBetter):
    """
    Gets the best bin based on the average return value of statFunction for the items in that bin.
    :param binnedResults: The binned HPLResults.
    :param statFunction: A function that will return a value based on an HPLResult. See also minMaxAvgPerBin.
    :param lowerIsBetter: Is a lower score preferable?
    :return: The key value for the best bin on average for the given statFunction.
    """
    minMaxAvg = minMaxAvgPerBin(binnedResults, statFunction)
    bins = list(minMaxAvg.keys())
    # Sort the bins based on their average values, where the 0th element is the best.
    bins.sort(key = lambda x: minMaxAvg.get(x)[MMAAvg], reverse = not lowerIsBetter)
    return bins[0] # return the 0th element, which is the best

if __name__ == "__main__":
    # Set up argument values
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help = "HPL output file to analyze")
    parser.add_argument("-b", "--bin", help = "The result property used for binning the output (required)", choices = HPLResult.NameToGetter.keys(), required = True)
    parser.add_argument("-s", "--statistic", help = "The result property used for finding the best bin on average (required)", choices = HPLResult.NameToGetter.keys(), required = True)
    parser.add_argument("-o", "--output", help = "Where to output the results, defaults to stdout")
    parser.add_argument("-v", "--verbose", action = "store_true", help = "When used, outputs the results sorted into bins")
    parser.add_argument("-t", "--title", help = "Title for this run")
    args = parser.parse_args()

    # Get some necessary data based off the arguments
    binFunc = HPLResult.NameToGetter.get(args.bin)
    statFunc = HPLResult.NameToGetter.get(args.statistic)
    binName = HPLResult.NameToDisplayName.get(args.bin)
    statName = HPLResult.NameToDisplayName.get(args.statistic)

    # Process data
    binnedResults = binResultsBy(rend.rendData(args.input), binFunc)
    minMaxAvg = minMaxAvgPerBin(binnedResults, statFunc)
    bestBin = getBestBin(binnedResults, statFunc, statFunc == HPLResult.HPLResult.getTime)

    # Write output
    outFile = None
    if args.output: # We have an output file, write to it
        outFile = open(args.output, 'w')
        write = lambda x: outFile.write(str(x) + "\n")
    else: # No output file, write to stdout
        write = lambda x: print(x)

    if args.title:
        write("Results for {}".format(args.title))
    else:
        write("Results for {}".format(args.input))
    if args.verbose:
        write("Arguments to HPLResult are defined as follows:")
        write("Encoded time, N, NB, P, Q, Time, Gigaflops, Start time, End time")
    write("")

    write("Results are binned by {}".format(binName))
    write("")

    if args.verbose:
        write("Binned results")
        write(pprint.pformat(binnedResults))
        write("")

    write("Minimum, maximum, and average {} per bin".format(statName))
    write(pprint.pformat(minMaxAvg))
    write("")

    write("Best bin with respect to {}".format(statName))
    write(bestBin)

    # Clean up the output file if we opened it
    if outFile:
        outFile.close()
    del outFile
