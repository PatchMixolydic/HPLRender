#!/usr/bin/env python3
from collections import defaultdict
from HPLResult import HPLResult
import rend

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
