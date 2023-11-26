import unittest

from greeter import greet


class TestGreeter(unittest.TestCase):
    def test_greet(self):
        cases = [
            {"name": "zhews", "expected_output": "Hello zhews!"},
            {"name": "pygreeter", "expected_output": "Hello pygreeter!"},
            {"name": "", "expected_output": "Hello World!"},
            {"name": " ", "expected_output": "Hello World!"},
        ]
        for case in cases:
            with self.subTest(name=case.get("name")):
                input = case.get("name")
                expected_output = case.get("expected_output")
                output = greet(input)
                self.assertEqual(output, expected_output)
