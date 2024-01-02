#!/usr/bin/env python3
import unittest
import json
import subprocess
from flask import Flask
from unittest.mock import patch
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    @patch('subprocess.check_output')
    def test_landing_page(self, mock_check_output):
        mock_check_output.return_value = '{}'
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'AWS Services', response.data)

if __name__ == '__main__':
    unittest.main()
