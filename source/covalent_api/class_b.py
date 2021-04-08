# :coding: utf-8
# :copyright: Copyright (c) 2021 Lluis Casals Marsol
# Copyright 2021 Lluis Casals Marsol.
# All rights reserved.
# Please see the LICENSE file that should have been included as part of this
# package.


from covalent_api import constants
from covalent_api import url_utils


class ClassB(object):

    @property
    def base_url(self):
        return self._base_url

    @property
    def session(self):
        return self._session

    def __init__(self, session):
        self._base_url = ''#"pricing/"
        self._session = session

    def get_sushiswap_address_exchange_liquidity_transactions(
            self, chain_id, address, swaps=False
    ):

        if chain_id not in list(constants.AVAILABLE_CHAIN_IDS.values()):
            raise Exception(
                "chain_id should be one of {}".format(
                    list(constants.AVAILABLE_CHAIN_IDS.values())
                )
            )

        method_url = '/v1/{chain_id}/address/{address}/stacks/sushiswap/acts/'.format(chain_id=chain_id,address=address)
        params = {
            'swaps': swaps
        }

        result = self.session.query(method_url, params, decode=False)
        return result


    def get_sushiswap_address_exchange_balances(self, chain_id, address):

        if chain_id not in list(constants.AVAILABLE_CHAIN_IDS.values()):
            raise Exception(
                "chain_id should be one of {}".format(
                    list(constants.AVAILABLE_CHAIN_IDS.values())
                )
            )

        method_url = '/v1/{chain_id}/address/{address}/stacks/sushiswap/balances/'.format(chain_id=chain_id,address=address)
        params = {
        }

        result = self.session.query(method_url, params, decode=False)
        return result

    def get_sushiswap_network_assets(self, chain_id):

        if chain_id not in list(constants.AVAILABLE_CHAIN_IDS.values()):
            raise Exception(
                "chain_id should be one of {}".format(
                    list(constants.AVAILABLE_CHAIN_IDS.values())
                )
            )

        method_url = '/v1/{chain_id}/networks/sushiswap/assets/'.format(chain_id=chain_id)
        params = {
        }

        result = self.session.query(method_url, params, decode=False)
        return result

    def get_aave_v2_address_balances(self, address):
        method_url = '/v1/1/address/{address}/stacks/aave_v2/balances/'.format(address=address)
        params = {
        }

        result = self.session.query(method_url, params, decode=False)
        return result

    def get_aave_address_balances(self, address):
        method_url = '/v1/1/address/{address}/stacks/aave/balances/'.format(address=address)
        params = {
        }

        result = self.session.query(method_url, params, decode=False)
        return result

    def get_balancer_exchange_address_balances(self, address):
        method_url = '/v1/1/address/{address}/stacks/balancer/balances/'.format(address=address)
        params = {
        }

        result = self.session.query(method_url, params, decode=False)
        return result

    def get_compound_address_activity(self, address):
        method_url = '/v1/1/address/{address}/stacks/compound/acts/'.format(address=address)
        params = {
        }

        result = self.session.query(method_url, params, decode=False)
        return result

    def get_compound_address_balances(self, address):
        method_url = '/v1/1/address/{address}/stacks/compound/balances/'.format(address=address)
        params = {
        }

        result = self.session.query(method_url, params, decode=False)
        return result

    def get_curve_address_balances(self, address):
        method_url = '/v1/1/address/{address}/stacks/curve/balances/'.format(address=address)
        params = {
        }

        result = self.session.query(method_url, params, decode=False)
        return result

    def get_farming_stats(self, address):
        method_url = '/v1/1/address/{address}/stacks/farming/positions/'.format(address=address)
        params = {
        }

        result = self.session.query(method_url, params, decode=False)
        return result

    def get_marker_address_balances_and_acts(self, address):
        method_url = '/v1/1/address/{address}/stacks/makerdao/'.format(address=address)
        params = {
        }

        result = self.session.query(method_url, params, decode=False)
        return result

    def get_uniswap_v1_address_exchange_balances(self, address):
        method_url = '/v1/1/address/{address}/stacks/uniswap_v1/balances/'.format(address=address)
        params = {
        }

        result = self.session.query(method_url, params, decode=False)
        return result

    def get_uniswap_v2_address_exchange_liquidity_transactions(self, address, swaps=False):
        method_url = '/v1/1/address/{address}/stacks/uniswap_v2/acts/'.format(address=address)
        params = {
            'swaps':swaps
        }

        result = self.session.query(method_url, params, decode=False)
        return result

    def get_uniswap_v2_address_exchange_balances(self, address):
        method_url = '/v1/1/address/{address}/stacks/uniswap_v2/balances/'.format(address=address)
        params = {
        }

        result = self.session.query(method_url, params, decode=False)
        return result

    def get_aave_v2_network_assets(self):
        method_url = '/v1/1/networks/aave_v2/assets/'
        params = {
        }

        result = self.session.query(method_url, params, decode=False)
        return result

    def get_aave_network_assets(self):
        method_url = '/v1/1/networks/aave/assets/'
        params = {
        }

        result = self.session.query(method_url, params, decode=False)
        return result

    def get_augur_market_affiliate_fee_divisors(self, page_number=None, page_size=None):
        method_url = '/v1/1/networks/augur/affiliate_fee/'
        params = {
            'page-number':page_number,
            'page-size':page_size
        }

        result = self.session.query(method_url, params, decode=False)
        return result

    def get_compound_network_assets(self):
        method_url = '/v1/1/networks/compound/assets/'
        params = {
        }

        result = self.session.query(method_url, params, decode=False)
        return result

    def get_uniswap_v2_network_assets(self, tickers=None, page_number=None, page_size=None):
        method_url = '/v1/1/networks/uniswap_v2/assets/'
        params = {
            'tickers': tickers,
            'page-number':page_number,
            'page-size':page_size
        }

        result = self.session.query(method_url, params, decode=False)
        return result