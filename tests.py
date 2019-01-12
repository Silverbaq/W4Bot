import unittest
import utils
#import chatcontroller

from events.event_model import Person, Event
from events.event_db_controller import EventDBController


class TestUtils(unittest.TestCase):

    def test_encodeb64(self):
        expected = 'dGhpcyBpcyBhIHRlc3Q='
        data = 'this is a test'
        res = utils.encode_base64(data)

        self.assertEqual(expected, res)

    def test_decode64(self):
        data = 'dGhpcyBpcyBhIHRlc3Q='
        expected = 'this is a test'
        res = utils.decode_base64(data)

        self.assertEqual(expected, res)



class TestChatBot(unittest.TestCase):

    def test_something(self):
        #response = chatcontroller.chat_with_bot("this is a message")
        #result = isinstance(response, str)

        #self.assertTrue(result)
        ''


class TestEventController(unittest.TestCase):

    def test_read_sheet(self):
        controller = EventDBController()
        sheet_data = controller.read_sheet()

        result = isinstance(sheet_data, str)

        self.assertTrue(result)


class TestEventDBController(unittest.TestCase):

    def test_create_and_find_person(self):
        controller = EventDBController()

        name = "Silverbaq"

        controller.add_person(name)

        person = controller.find_person(name)

        result = isinstance(person, Person)

        self.assertTrue(result)



if __name__ == '__main__':
    unittest.main()
