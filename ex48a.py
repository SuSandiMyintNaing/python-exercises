def convert(s):
        try:
            return int(s)
        except ValueError:
            return None
