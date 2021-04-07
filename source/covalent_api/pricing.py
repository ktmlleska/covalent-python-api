import os
import json
import logging
import requests


class Pricing(object):

    # @property
    # def url(self):
    #     return self._url

    @property
    def base_url(self):
        return self._base_url

    @property
    def session(self):
        return self._session

    def __init__(self, session):
        self._base_url = "pricing/"
        self._session = session
        # self._url = "pricing/"

    def prices_by_ticker(
            self, quote_currency, ticker_symbol, date_from=None, date_to=None,
            prices_at_asc=False, page_number=None, page_size=None, format="json"
    ):
        # TODO: I should be using url join or path.join or something cooler
        prices_by_ticker_url = "historical/"
        url = self.base_url + prices_by_ticker_url + quote_currency+"/" + ticker_symbol+"/?"
        params = {
            'from': date_from,
            'to': date_to,
            'prices-at-asc': prices_at_asc,
            'page-number': page_number,
            'page-size': page_size,
            'format': format
        }
        decode = format == 'json'
        result = self.session.query(url, params, decode=decode)
        return result