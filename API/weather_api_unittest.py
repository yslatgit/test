#coding:utf-8
import unittest
import requests

class WwetherTest(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://www.weather.com.cn/data/sk/101110101.html"

    def test_pass(self):
        r =requests.get(self.base_url)
        print(eval(r.json()["weatherinfo"]["city"]))
        self.assertEqual(r.json()["weatherinfo"]["city"],u"西安")

if __name__ == '__main__':
    unittest.main()