class Utils(object):
    """
    Utils class with static functions.
    """

    @staticmethod
    def parse_float(value):
        try:
            return float(value)
        except:
            return 0.0

    @staticmethod
    def parse_int(value):
        try:
            return int(value)
        except:
            return 0
