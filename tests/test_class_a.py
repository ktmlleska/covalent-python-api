import unittest
import covalent_api
import mock
import os

SERVER_URL="https://api.covalenthq.com"


class TestClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.APIKEY = os.environ.get('COVALENT_API_KEY')
        if not cls.APIKEY:
            raise Exception("Need to set COVALENT_API_KEY in order to run tests.")
        cls.session = covalent_api.session.Session(server_url=SERVER_URL, api_key=cls.APIKEY)
        cls.cl_a = covalent_api.class_a.ClassA(cls.session)

    def test_get_transactions(self):
        ret = self.cl_a.get_transactions(chain_id="1", address="0x74c1e4b8cae59269ec1d85d3d4f324396048f4ac")
        print(ret)
        assert 'data' in ret

