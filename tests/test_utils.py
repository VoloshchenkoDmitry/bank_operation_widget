import json
import os
import tempfile
from unittest import TestCase

from src.utils import read_json_file


class TestUtils(TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_file = os.path.join(self.temp_dir.name, "test.json")

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_read_valid_json(self):
        data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
        with open(self.temp_file, "w") as f:
            json.dump(data, f)

        result = read_json_file(self.temp_file)
        self.assertEqual(result, data)

    def test_read_empty_file(self):
        open(self.temp_file, "w").close()

        result = read_json_file(self.temp_file)
        self.assertEqual(result, [])

    def test_read_invalid_json(self):
        with open(self.temp_file, "w") as f:
            f.write("invalid json")

        result = read_json_file(self.temp_file)
        self.assertEqual(result, [])

    def test_read_non_list_json(self):
        with open(self.temp_file, "w") as f:
            json.dump({"key": "value"}, f)

        result = read_json_file(self.temp_file)
        self.assertEqual(result, [])
