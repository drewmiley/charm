class GCD(object):

    def calculate(self, x, y):
        number_types = (int, float)

        if isinstance(x, number_types) and isinstance(y, number_types):
            if x < 0 or y < 0:
                return None
            if x == 0 or y == 0:
                return 0
            return self._iterator(x, y)
        else:
            raise ValueError

    def _iterator(self, x, y):
        if y == 0:
            return x
        else:
            newX = y
            newY = x % y
            return self._iterator(newX, newY)