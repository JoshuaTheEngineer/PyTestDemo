import pytest


class Phonebook:

    def __init__(self) -> None:
        self.numbers = {}

    def add(self, name, number):
        self.numbers[name] = number

    def lookup(self, name):
        return self.numbers[name]

    def names(self):
        return set(self.numbers.keys())

@pytest.fixture
def phonebook():
    return Phonebook()

def test_phonebook_contains_all_names(phonebook):
    phonebook.add("Bob", "1234")
    assert "Bob" in phonebook.names()

def test_lookup_by_name(phonebook):
    phonebook.add("Bob","1234")
    number = phonebook.lookup("Bob")
    assert "1234" == number

def test_missing_name(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("missing")