class Chocolates(object):

    def __init__(self):
        self.chocolates = {}

    def add(self, name, number):
        self.chocolates[name] = number

    def lookup(self,name):
        return self.chocolates[name]

    def getTotal(self):
        total = 0
        for name in self.chocolates.keys():
            total = total + self.chocolates[name]
        return total

class ChocolateBox:

    def __init__(self, chocolates=None):
        self._chocolatelimit = 12
        self._is_alarm_on = False
        self._chocolates = chocolates or Chocolates()

    def check(self):
        total = self._chocolates.getTotal()
        if total > self._chocolatelimit:
            self._is_alarm_on = True

    @property
    def is_alarm_on(self):
        return self._is_alarm_on