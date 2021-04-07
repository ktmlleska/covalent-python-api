import os
import json
import logging
import requests


class Session(object):
    '''Attach session authentication information to requests.'''

    @property
    def server_url(self):
        '''Return server ulr used for session.'''
        return self._server_url

    @property
    def api_key(self):
        '''Return API key used for session.'''
        return self._api_key

    def __init__(self, server_url=None, api_key=None, timeout=60):
        '''Initialise with *api_key* and *api_user*.'''
        super(Session, self).__init__()
        self.logger = logging.getLogger(
            __name__ + '.' + self.__class__.__name__
        )

        if server_url is None:
            server_url = os.environ.get('COVALENT_SERVER')

        if not server_url:
            raise TypeError(
                'Required "server_url" not specified. Pass as argument or set '
                'in environment variable COVALENT_SERVER.'
            )

        self._server_url = server_url

        if api_key is None:
            api_key = os.environ.get('COVALENT_API_KEY')

        if not api_key:
            raise TypeError(
                'Required "api_key" not specified. Pass as argument or set in '
                'environment variable COVALENT_API_KEY.'
            )

        self._api_key = api_key

        self._request = requests.Session()
        self._request.auth = ('', self._api_key)

        self.request_timeout = timeout

    # def get(self, entity_type, entity_key):
    #     entity = self._get(entity_type, entity_key)
    #     return entity

    def decode(self, string):
        '''Return decoded JSON *string* as Python object.'''
        return json.loads(string)

    def encode(self, data):
        return json.dumps(
            data,
            sort_keys=True
        )

    def query(self, url, params=None, decode=True):#or change it direcly to get
        url = self._server_url + url
        print("url --> {}".format(url))
        #params = self.encode(params)

        response = self._request.get(
            url,
            params=params,
            timeout=self.request_timeout
        )

        result = response.text
        if decode:
            try:
                result = self.decode(result)
            except Exception as e:
                error_message = (
                    'Server reported error in unexpected format. '
                    'Raw error was: {0}. \n Exception: {1}'.format(response.text, e)
                )
                self.logger.exception(error_message)
                raise Exception(error_message)
        return result

    def get(self, entity, filter):
        entity = 'prices'
        filter = 'address'
        entity_map = {
            'prices':'pricing'
        }
        filter_map = {
            'address':'historical_by_adress',
            'addresses':'historical_by_adresses',
            'ticker':'historical',
            'prices':'tickers',
            'volatility':'volatility'
        }


