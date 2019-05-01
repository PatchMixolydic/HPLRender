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
        ).format(self.encodedTime, self.n, self.nb, self.p, self.q, self.time, self.gflops, self.start, self.end)
        return output

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

    def getTime(self):
        return self.time

    def getGflops(self):
        return self.gflops

    def getStartTime(self):
        return self.startTime

    def getEndTime(self):
        return self.endTime
