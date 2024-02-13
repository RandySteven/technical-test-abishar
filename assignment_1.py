import unittest
import requests

class MyTestCase(unittest.TestCase):
    url = 'https://reqres.in/'

    def test_get_user_by_id(self):
        endpoint = 'api/users/'
        url = self.url + endpoint + '2'
        res = requests.get(url)
        self.assertEqual(res.status_code, 200)

    def test_post_user(self):
        req = {'name': 'Randy Steven', 'job': 'SDET'}
        endpoint = 'api/users'
        url = self.url + endpoint
        res = requests.post(url, req)
        self.assertEqual(res.status_code, 201)


if __name__ == '__main__':
    unittest.main()
