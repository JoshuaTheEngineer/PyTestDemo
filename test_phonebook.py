import unittest

from phonebook import Phonebook


class PhoneBookTest(unittest.TestCase):

    def setUp(self) -> None:
        self.phonebook = Phonebook()

    def test_lookup_by_name(self):
        self.phonebook.add("Bob","1234")
        number = self.phonebook.lookup("Bob")
        self.assertEqual("1234", number)

    def test_missing_name(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

    @unittest.skip("WIP")
    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())