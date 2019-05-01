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
        self.start = start
        self.end = end

    def __str__(self):
        output = (
            "T/V                N    NB     P     Q               Time                 Gflops\n"
            "--------------------------------------------------------------------------------\n"
            "{}        {}   {}     {}     {}             {}             {}\n"
            "start time {}\n"
            "end time {}\n"
        ).format(self.encodedTime, self.n, self.nb, self.p, self.q, self.time, self.gflops, self.start, self.end)
        return output
