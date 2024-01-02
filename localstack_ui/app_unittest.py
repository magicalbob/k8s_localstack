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
        # tear down the test, nothing to do
        pass

    @patch('subprocess.check_output')
    def test_landing_page(self, mock_check_output):
        mock_check_output.return_value = '{}'
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'AWS Services', response.data)

    @patch('subprocess.check_output')
    def test_service_exists(self, mock_check_output):
        # Test case where the service URL exists in config.json
        mock_check_output.return_value = '{"test": "data"}'
        response = self.app.get('/service/apigateway')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'API Gateway', response.data)  # Update the expected content

    @patch('subprocess.check_output')
    def test_service_not_found(self, mock_check_output):
        # Test case where the service URL does not exist in config.json
        response = self.app.get('/service/nonexistent')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Service not found', response.data)

    @patch('subprocess.check_output')
    def test_item_page_not_found(self, mock_check_output):
        # Test case where the service URL, section name, or item name do not exist in config.json
        response = self.app.get('/apigateway/nonexistent/Get')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Service or section not found', response.data)


if __name__ == '__main__':
    unittest.main()
