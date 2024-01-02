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

    @patch('subprocess.check_output')
    def test_service_page(self, mock_check_output):
        mock_check_output.return_value = '{}'
        response = self.app.get('/service/test')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'AWS Service - Test', response.data)

    @patch('subprocess.check_output')
    def test_item_page(self, mock_check_output):
        mock_check_output.return_value = '{"test": "data"}'
        response = self.app.get('/test/test/item')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'{"test": "data"}', response.data)

    @patch('subprocess.check_output')
    def test_error_executing_aws_command(self, mock_check_output):
        mock_check_output.side_effect = subprocess.CalledProcessError(1, 'command')
        response = self.app.get('/test/test/item')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Error executing AWS command', response.data)

    @patch('subprocess.check_output')
    def test_error_decoding_json_data(self, mock_check_output):
        mock_check_output.return_value = 'invalid json'
        response = self.app.get('/test/test/item')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Error decoding JSON data', response.data)

if __name__ == '__main__':
    unittest.main()
