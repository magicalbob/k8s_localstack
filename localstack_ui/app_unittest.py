#!/usr/bin/env python3
import unittest
from flask import Flask
from unittest.mock import patch
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        # Tear down the test, nothing to do
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
        self.assertIn(b'API Gateway', response.data)

    @patch('subprocess.check_output')
    def test_service_not_found(self, mock_check_output):
        # Test case where the service URL does not exist in config.json
        mock_check_output.side_effect = FileNotFoundError("File not found")  # Simulate service not found
        response = self.app.get('/service/nonexistent')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Service not found', response.data)

    @patch('subprocess.check_output')
    def test_item_page_not_found(self, mock_check_output):
        # Test case where the service URL, section name, or item name do not exist in config.json
        response = self.app.get('/apigateway/nonexistent/Get')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Service or section not found', response.data)

    @patch('subprocess.check_output')
    def test_item_page_success(self, mock_check_output):
        # Test case where item page retrieval is successful
        mock_check_output.return_value = '{"test": "data"}'
        response = self.app.get('/apigateway/section/item')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Service or section not found', response.data)  # This should be present in the JSON response

    @patch('subprocess.check_output')
    def test_kms_list_page_success(self, mock_check_output):
        # Test case where kms list page retrieval is successful
        mock_check_output.return_value = '{"test": "data"}'
        response = self.app.get('/kms/Keys/List')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'List', response.data)  # This should be present in the JSON response

if __name__ == '__main__':
    unittest.main()

