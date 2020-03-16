class Kata:
    def numberElements(string):
        if string:
            if "," in string:
                return len(string.split(","))
            return 1
        return 0

    def minElement(string):
        if string:
            if "," in string:
                return int(min(string.split(",")))
            return 0
        return None
