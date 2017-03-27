class GCD(object):

    def calculate(self, x, y):
        number_types = (int, float)

        if isinstance(x, number_types) and isinstance(y, number_types):
            if x < 0 or y < 0:
                return None
            return min(x, y)
        else:
            raise ValueError
