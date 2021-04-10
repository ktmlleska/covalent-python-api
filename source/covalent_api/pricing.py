# :coding: utf-8
# :copyright: Copyright (c) 2021 Lluis Casals Marsol
# Copyright 2021 Lluis Casals Marsol.
# All rights reserved.
# Please see the LICENSE file that should have been included as part of this
# package.


from covalent_api import constants


class Pricing(object):

    @property
    def session(self):
        return self._session

    def __init__(self, session):
        self._session = session

    def get_prices_by_address(
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

        method_url = '/v1/pricing/historical_by_address/{chain_id}/{quote_currency}/{contract_address}/'.format(chain_id=chain_id, quote_currency=quote_currency,contract_address=contract_address)
        params = {
            'from': date_from,
            'to': date_to,
            'prices-at-asc': prices_at_asc,
            'page-number': page_number,
            'page-size': page_size,
            'format': format
        }
        decode = format == 'json'
        result = self.session.query(method_url, params, decode=decode)
        return result

    def get_prices_by_addresses(
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

        method_url = '/v1/pricing/historical_by_addresses/{chain_id}/{quote_currency}/{contract_addresses}/'.format(chain_id=chain_id, quote_currency=quote_currency, contract_addresses=contract_addresses)
        params = {
            'from': date_from,
            'to': date_to,
            'prices-at-asc': prices_at_asc,
            'page-number': page_number,
            'page-size': page_size,
            'format': format
        }
        decode = format == 'json'
        result = self.session.query(method_url, params, decode=decode)
        return result

    def get_historical_prices_by_ticker_symbol(
            self, quote_currency, ticker_symbol, date_from=None, date_to=None,
            prices_at_asc=False, page_number=None, page_size=None, format="json"
    ):

        method_url = '/v1/pricing/historical/{quote_currency}/{ticker_symbol}/'.format(quote_currency=quote_currency, ticker_symbol=ticker_symbol)
        params = {
            'from': date_from,
            'to': date_to,
            'prices-at-asc': prices_at_asc,
            'page-number': page_number,
            'page-size': page_size,
            'format': format
        }
        decode = format == 'json'
        result = self.session.query(method_url, params, decode=decode)
        return result

    def get_spot_prices(
            self, tickers=None, page_number=None, page_size=None, format="json"
    ):
        method_url = '/v1/pricing/tickers/'
        params = {
            'tickers': tickers,
            'page-number': page_number,
            'page-size': page_size,
            'format': format
        }
        decode = format == 'json'
        result = self.session.query(method_url, params, decode=decode)
        return result

    def get_price_volatility(
            self, tickers=None, page_number=None, page_size=None, format="json"
    ):
        method_url = '/v1/pricing/volatility/'
        params = {
            'tickers': tickers,
            'page-number': page_number,
            'page-size': page_size,
            'format': format
        }
        decode = format == 'json'
        result = self.session.query(method_url, params, decode=decode)
        return result
