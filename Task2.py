import unittest

class Phonebook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        self.contacts[name] = number

    def get_contact(self, name):
        return self.contacts.get(name, None)

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]

class TestPhonebook(unittest.TestCase):
    def setUp(self):
        self.phonebook = Phonebook()
        self.phonebook.add_contact('John', '1234567890')

    def test_add_contact(self):
        self.phonebook.add_contact('Jane', '9876543210')
        self.assertEqual(self.phonebook.get_contact('Jane'), '9876543210')

    def test_get_contact(self):
        self.assertEqual(self.phonebook.get_contact('John'), '1234567890')
        self.assertIsNone(self.phonebook.get_contact('NonExistent'))

    def test_delete_contact(self):
        self.phonebook.delete_contact('John')
        self.assertIsNone(self.phonebook.get_contact('John'))

if __name__ == '__main__':
    unittest.main()
