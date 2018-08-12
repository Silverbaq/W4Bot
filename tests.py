import unittest
import utils
import chatcontroller


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
        response = chatcontroller.chat_with_bot("this is a message")
        result = isinstance(response, str)

        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
