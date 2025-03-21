import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.crudCateg import app

class CrudCategTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('app.crudCateg.bd.create_connection')
    def test_create_category_success(self, mock_create_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_create_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        response = self.app.post('/categories', json={
            'category_id': 1,
            'category_name': 'Test Category',
            'description': 'Test Description',
            'picture': None
        })

        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Category created successfully', response.data)

    @patch('app.crudCateg.bd.create_connection')
    def test_create_category_db_failure(self, mock_create_connection):
        mock_create_connection.return_value = None

        response = self.app.post('/categories', json={
            'category_id': 1,
            'category_name': 'Test Category',
            'description': 'Test Description',
            'picture': None
        })

        self.assertEqual(response.status_code, 500)
        self.assertIn(b'Failed to connect to the database', response.data)

    @patch('app.crudCateg.bd.create_connection')
    def test_read_category_success(self, mock_create_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_create_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = (1, 'Test Category', 'Test Description', None)

        response = self.app.get('/categories/1')

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Category', response.data)

    @patch('app.crudCateg.bd.create_connection')
    def test_read_category_not_found(self, mock_create_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_create_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = None

        response = self.app.get('/categories/1')

        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Category not found', response.data)

if __name__ == '__main__':
    unittest.main()