class Kata:
    def numberElements(string):
        if string:
            return len(string.split(","))
        return 0

    def minElement(string):
        if string:
            return int(min(string.split(",")))

    def maxElement(string):
        return 0
