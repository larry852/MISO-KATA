class Kata:
    def numberElements(string):
        if string:
            if "," in string:
                return len(string.split(","))
            return 1
        return 0
