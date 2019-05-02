# maps command line names to displayable names for the graph
NameToDisplayName = {
    "encodedTime": "Encoded time",
    "n": "Problem size",
    "nb": "Block size",
    "p": "Number of matrix rows",
    "q": "Number of matrix columns",
    "time": "Time to solve",
    "gflops": "GigaFLOPS"
}

class HPLResult:
    """
    Stores data about an HPL result from a run.
    """
    def __init__(self, encodedTime, n, nb, p, q, time, gflops, start, end):
        self.encodedTime = encodedTime
        self.n = n
        self.nb = nb
        self.p = p
        self.q = q
        self.time = time
        self.gflops = gflops
        self.startTime = start
        self.endTime = end

    def __str__(self):
        output = (
            "T/V                N    NB     P     Q               Time                 Gflops\n"
            "--------------------------------------------------------------------------------\n"
            "{}        {}   {}     {}     {}             {}             {}\n"
            "start time {}\n"
            "end time {}\n"
        ).format(self.encodedTime, self.n, self.nb, self.p, self.q, self.time, self.gflops, self.startTime, self.endTime)
        return output

    def __repr__(self):
        return "HPLResult({}, {}, {}, {}, {}, {}, {}, {})".format(
            self.encodedTime, self.n, self.nb, self.p, self.q, self.time, self.gflops, self.startTime, self.endTime
        )

    """
    The following getters are meant to be used for organizing HPLResults into bins.
    This is meant to provide a cleaner way to get attributes dynamically versus getattr(obj, "attribute")
    There are no corresponding setters - set the values directly instead if you must.
    """

    def getEncodedTime(self):
        return self.encodedTime

    def getN(self):
        return self.n

    def getNB(self): # rights
        return self.nb

    def getP(self):
        return self.p

    def getQ(self):
        return self.q

    def getTime(self):
        return self.time

    def getGflops(self):
        return self.gflops

    def getStartTime(self):
        return self.startTime

    def getEndTime(self):
        return self.endTime

# maps names of properties of HPLResult to getters for HPLResult.
NameToGetter = {
    "encodedtime": HPLResult.getEncodedTime,
    "n": HPLResult.getN,
    "nb": HPLResult.getNB,
    "p": HPLResult.getP,
    "q": HPLResult.getQ,
    "time": HPLResult.getTime,
    "gflops": HPLResult.getGflops
}
