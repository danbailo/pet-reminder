import unittest

from models.reminder import Reminder
from utils import load_json


class TestCase(unittest.TestCase):

    def test_response(self):
        body = load_json('tests/fixtures/jsons/response.json')
        student = Reminder().get_student_response()
        for k in body.keys():
            self.assertIn(k, student.keys())


if __name__ == '__main__':
    unittest.main()
