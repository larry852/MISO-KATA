class Kata:
    def numberElements(string):
        if string:
            if "," in string:
                return 2
            else:
                return 1
        return 0
