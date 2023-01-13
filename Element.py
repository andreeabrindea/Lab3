class Element:
    def __init__(self, Q, E, d, q0, F):
        self.Q = Q
        self.E = E
        self.d = d
        self.q0 = q0
        self.F = F

    def __str__(self):
        print("States:")
        print(*self.Q, sep=", ")
        print("Alphabet:")
        print(*self.E, sep=", ")
        print("Transitons:")
        for elem in self.d:
            if len(self.d[elem]) > 1:
                for third in self.d[elem]:
                    print(str(elem).replace("('", "").replace("')", "").replace("'",
                                                                                "") + "-> " + third)  # non-deterministic finite
            else:
                print(str(elem).replace("('", "").replace("')", "").replace("'",
                                                                            "") + "-> " + str(self.d[elem]).replace(
                    "['",
                    "").replace(
                    "']", ""))
        print("Initial state: ")
        print(*self.q0, sep=", ")
        print("Final state: ")
        print(*self.F, sep=", ")
        return ""