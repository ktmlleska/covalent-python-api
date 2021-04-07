# :coding: utf-8
# :copyright: Copyright (c) 2021 Lluis Casals Marsol
# Copyright 2021 Lluis Casals Marsol.
# All rights reserved.
# Please see the LICENSE file that should have been included as part of this
# package.


from covalent_api import constants
from covalent_api import url_utils


class Pricing(object):

    @property
    def base_url(self):
        return self._base_url

    @property
    def session(self):
        return self._session

    def __init__(self, session):
        self._base_url = "pricing/"
        self._session = session

    def prices_by_address(
            self, chain_id, quote_currency, contract_address, date_from=None,
            date_to=None, prices_at_asc=False, page_number=None, page_size=None,
            format="json"
    ):
        if chain_id not in constants.AVAILABLE_CHAIN_IDS:
            raise Exception(
                "chain_id should be one of {}".format(
                    list(constants.AVAILABLE_CHAIN_IDS.values)
                )
            )

        method_url = "historical_by_address"
        url_args = [method_url, chain_id, quote_currency, contract_address]

        url = url_utils.generate_url(self.base_url, url_args)
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

    def prices_by_addresses(
            self, chain_id, quote_currency, contract_address, date_from=None,
            date_to=None, prices_at_asc=False, page_number=None, page_size=None,
            format="json"
    ):
        if chain_id not in constants.AVAILABLE_CHAIN_IDS:
            raise Exception(
                "chain_id should be one of {}".format(
                    list(constants.AVAILABLE_CHAIN_IDS.values)
                )
            )

        method_url = "historical_by_address"
        url_args = [method_url, chain_id, quote_currency, contract_address]
        url = url_utils.generate_url(self.base_url, url_args)
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

    def prices_by_ticker(
            self, quote_currency, ticker_symbol, date_from=None, date_to=None,
            prices_at_asc=False, page_number=None, page_size=None, format="json"
    ):
        method_url = "historical"
        url_args = [method_url, quote_currency, ticker_symbol]
        url = url_utils.generate_url(self.base_url, url_args)
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

    def spot_prices(
            self, tickers=None, page_number=None, page_size=None, format="json"
    ):
        method_url = "tickers"
        url = url_utils.generate_url(self.base_url, [method_url])
        params = {
            'tickers': tickers,
            'page-number': page_number,
            'page-size': page_size,
            'format': format
        }
        decode = format == 'json'
        result = self.session.query(url, params, decode=decode)
        return result

    def price_volatility(
            self, tickers=None, page_number=None, page_size=None, format="json"
    ):
        method_url = "volatility"
        url = url_utils.generate_url(self.base_url, [method_url])
        params = {
            'tickers': tickers,
            'page-number': page_number,
            'page-size': page_size,
            'format': format
        }
        decode = format == 'json'
        result = self.session.query(url, params, decode=decode)
        return result