import covalent_api as cov
from covalent_api.class_a import ClassA

import unittest
from unittest import mock



class TestPaginate(unittest.TestCase):
    def setUp(self):
        #sess = cov.Session(timeout=10, api_key_is_username=True)
        self.sess = mock.MagicMock()
        self.classa = ClassA(self.sess)

    def test_max_pages(self):
        address = 'dummy address'
        RSK_CHAIN_ID='30'
        self.sess.query.return_value = {'error': False, 'data': {'items': ['thing1', 'thing2']}}

        for result in self.classa.paginate(self.classa.get_transactions, chain_id=RSK_CHAIN_ID, address=address,
                        page_size=1, starting_page=1, max_pages=5):
            pass

        #this gets called max_pages number of times
        self.assertEqual(self.sess.query.call_count, 5)

    def test_no_more_results(self):
        address = 'dummy address'
        RSK_CHAIN_ID='30'
        self.sess.query.return_value = {'error': False, 'data': {'items': ['thing1', 'thing2']}}

        for result in self.classa.paginate(self.classa.get_transactions, chain_id=RSK_CHAIN_ID, address=address,
                        page_size=1, starting_page=1,
                        max_pages=100):
            self.sess.query.return_value = {'error': False, 'data': {'items': []}}

        #because no data came in, it only gets called 2 times instead of max_pages=100
        self.assertEqual(self.sess.query.call_count, 2)


if __name__ == '__main__':
    unittest.main()
