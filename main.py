class Kata:
    def numberElements(string):
        if string:
            return len(string.split(",")[0])
        return 0
