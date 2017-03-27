class GCD(object):

    def calculate(self, x, y):
        number_types = (int, float)

        if isinstance(x, number_types) and isinstance(y, number_types):
            pass
        else:
            raise ValueError
