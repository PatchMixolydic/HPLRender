# HPLRender

rend (v.) - (archaic) wrench something apart violently.

HPLRender tears apart HPL output files in an incredibly messy way to produce
usable results.
Also included are tools used for analysis of code.

## Usage

### analyze.py
analyze.py requires 2 arguments:
* --statistic PROPERTY, which sets the statistic that will be analyzed per bin
* an input file

...where PROPERTY is one of the following: encodedtime, n, nb, p, q, time, or
gflops.

There is a third, optional argument you will most likely want to set named --bin.
This argument is meant to describe how your results will be categorized. Like
--statistic, you should provide it with PROPERTY. However, if --bin is not
specified, it defaults to a null binning function which throws everything in
the same bin.

There are also three more optional arguments:
* --output FILE, which allows you to specify an output file (outputs to stdout
by default)
* --title TITLE, which allows you to set a custom title in the analysis results
* --verbose, which will add the binned results to the output

For instance, to analyze a run to see the time it took to solve each problem,
you would use `./analyze.py --statistic time --verbose --output timeTaken.txt HPL.out`.

### graph.py
graph.py requires 3 arguments:
* --bin PROPERTY, which describes how your results will be categorized (this is
your x-axis)
* --statistic PROPERTY, which sets the statistic that will be analyzed per bin
(this is your y-axis)
* an input file

...where PROPERTY is one of the following: encodedtime, n, nb, p, q, time, or
gflops. Unlike analyze.py, you cannot use the null binning function for --bin
here, because every point would get plotted at x = 0, which wouldn't make any
sense.

There's also the optional argument --title, which will add a run title in
parentheses after the regular graph title.

For instance, to visualize how many gigaFLOPS the system pulled per problem for
several block sizes, you would use `./graph.py --bin nb --statistic gflops HPL.out`. 
