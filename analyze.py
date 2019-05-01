#!/usr/bin/env python3
import statistics
from collections import defaultdict
import rend
from HPLResult import HPLResult

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
