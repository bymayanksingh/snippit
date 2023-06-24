import unittest
from app import app
from werkzeug.datastructures import FileStorage

class TestApp(unittest.TestCase):

    def setUp(self):
        app.testing == True
        self.client = app.test_client()

    def test_index_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<input type="submit" value="Upload"/>', response.data)

    def test_not_found_route(self):
        response = self.client.get('/non-existent-url')
        self.assertEqual(response.status_code, 404)
    
    def test_internal_server_error_route(self):
        response = self.client.get('/error-route')
        self.assertEqual(response.status_code, 500)

    def test_upload_file_route(self):
        data = {'file': (open('test_file.txt', 'rb'), 'test_file.txt')}
        response = self.client.post('/', data=data, content_type='multipart/form-data')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Summarize the following in bullet points:', response.data)

    def test_upload_invalid_file_format(self):
        file = FileStorage(
            stream=open('test_file_invalid.png', 'rb'),
            filename='test_file_invalid.png',
            content_type='image/jpeg'
        )
        response = self.client.post('/', data={'file': file}, content_type='multipart/form-data')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'<p>Invalid File Format, Please upload a text file</p>', response.data)

if __name__=="__main__":
    unittest.main()
