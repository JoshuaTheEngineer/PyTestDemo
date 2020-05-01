from unittest.mock import Mock
from chocolate_box import ChocolateBox, Chocolates

def test_chocolate_box_alarm_is_off_by_default():
    chocolate_box = ChocolateBox()
    assert not chocolate_box.is_alarm_on

class StubChocolates:
    def getTotal(self):
        return 13

def test_too_much_chocolate_activates_alarm():
    chocolatebox = ChocolateBox(chocolates=StubChocolates())
    chocolatebox.check()
    assert chocolatebox.is_alarm_on

# Unit Test Mock
def test_normal_chocolate_alarm_stays_off():
    stub_chocolates = Mock(Chocolates)
    stub_chocolates.getTotal.return_value = 12
    chocolate_box = ChocolateBox(stub_chocolates)
    chocolate_box.check()
    assert not chocolate_box.is_alarm_on