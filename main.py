from statistics import mean


class Kata:
    def numberElements(string):
        if string:
            return len(string.split(","))
        return 0

    def minElement(string):
        if string:
            return int(min(string.split(",")))

    def maxElement(string):
        if string:
            return int(max(string.split(",")))

    def avgElements(string):
        if string:
            arreglo = [int(n) for n in string.split(",") if n]
            return mean(arreglo)
