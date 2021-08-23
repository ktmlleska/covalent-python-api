from covalent_api import constants

class Dex(object):

    @property
    def session(self):
        return self._session

    def __init__(self, session):
        self._session = session

    # https://api.covalenthq.com/v1/{chain_id}/xy=k/{dexname}/health/
    def health(self, chain_id,dexname):
        if chain_id not in list(constants.AVAILABLE_CHAIN_IDS.values()):
            raise Exception(
                "chain_id should be one of {}".format(
                    list(constants.AVAILABLE_CHAIN_IDS.values())
                )
            )
        if dexname not in list(constants.AVAILABLE_DEXES.values()):
            raise Exception(
                "dexname should be one of {}".format(
                    list(constants.AVAILABLE_DEXES.values())
                )
            )
        method_url = (
            '/v1/{chain_id}/xy=k/{dexname}/health/'.format(
                chain_id=chain_id,
                dexname=dexname
            )
        )
        decode = format == 'json'
        result = self.session.query(method_url, decode=decode)
        return result
    # https://api.covalenthq.com/v1/{chain_id}/xy=k/{dexname}/ecosystem/
    def ecosystem(self, chain_id,dexname):
        if chain_id not in list(constants.AVAILABLE_CHAIN_IDS.values()):
            raise Exception(
                "chain_id should be one of {}".format(
                    list(constants.AVAILABLE_CHAIN_IDS.values())
                )
            )
        if dexname not in list(constants.AVAILABLE_DEXES.values()):
            raise Exception(
                "dexname should be one of {}".format(
                    list(constants.AVAILABLE_DEXES.values())
                )
            )
        method_url = (
            '/v1/{chain_id}/xy=k/{dexname}/ecosystem/'.format(
                chain_id=chain_id,
                dexname=dexname
            )
        )
        decode = format == 'json'
        result = self.session.query(method_url, decode=decode)
        return result
    # https://api.covalenthq.com/v1/{chain_id}/xy=k/{dexname}/pools/
    def pools(self, chain_id,dexname):
        if chain_id not in list(constants.AVAILABLE_CHAIN_IDS.values()):
            raise Exception(
                "chain_id should be one of {}".format(
                    list(constants.AVAILABLE_CHAIN_IDS.values())
                )
            )
        if dexname not in list(constants.AVAILABLE_DEXES.values()):
            raise Exception(
                "dexname should be one of {}".format(
                    list(constants.AVAILABLE_DEXES.values())
                )
            )
        method_url = (
            '/v1/{chain_id}/xy=k/{dexname}/pools/'.format(
                chain_id=chain_id,
                dexname=dexname
            )
        )
        decode = format == 'json'
        result = self.session.query(method_url, decode=decode)
        return result
    # https://api.covalenthq.com/v1/{chain_id}/xy=k/{dexname}/pools/address/{address}/
    def poolDataByAddress(self, chain_id,dexname,address):
        if chain_id not in list(constants.AVAILABLE_CHAIN_IDS.values()):
            raise Exception(
                "chain_id should be one of {}".format(
                    list(constants.AVAILABLE_CHAIN_IDS.values())
                )
            )
        if dexname not in list(constants.AVAILABLE_DEXES.values()):
            raise Exception(
                "dexname should be one of {}".format(
                    list(constants.AVAILABLE_DEXES.values())
                )
            )
        method_url = (
            'v1/{chain_id}/xy=k/{dexname}/pools/address/{address}/'.format(
                chain_id=chain_id,
                dexname=dexname,
                address=address
            )
        )
        decode = format == 'json'
        result = self.session.query(method_url, decode=decode)
        return result
    # https://api.covalenthq.com/v1/{chain_id}/xy=k/{dexname}/pools/address/{address}/transactions/
    def poolTransactionsByAddress(self, chain_id,dexname,address):
        if chain_id not in list(constants.AVAILABLE_CHAIN_IDS.values()):
            raise Exception(
                "chain_id should be one of {}".format(
                    list(constants.AVAILABLE_CHAIN_IDS.values())
                )
            )
        if dexname not in list(constants.AVAILABLE_DEXES.values()):
            raise Exception(
                "dexname should be one of {}".format(
                    list(constants.AVAILABLE_DEXES.values())
                )
            )
        method_url = (
            'v1/{chain_id}/xy=k/{dexname}/pools/address/{address}/transactions/'.format(
                chain_id=chain_id,
                dexname=dexname,
                address=address
            )
        )
        decode = format == 'json'
        result = self.session.query(method_url, decode=decode)
        return result
    # https://api.covalenthq.com/v1/{chain_id}/xy=k/{dexname}/tokens/
    def tokens(self, chain_id,dexname):
        if chain_id not in list(constants.AVAILABLE_CHAIN_IDS.values()):
            raise Exception(
                "chain_id should be one of {}".format(
                    list(constants.AVAILABLE_CHAIN_IDS.values())
                )
            )
        if dexname not in list(constants.AVAILABLE_DEXES.values()):
            raise Exception(
                "dexname should be one of {}".format(
                    list(constants.AVAILABLE_DEXES.values())
                )
            )
        method_url = (
            '/v1/{chain_id}/xy=k/{dexname}/tokens/'.format(
                chain_id=chain_id,
                dexname=dexname
            )
        )
        decode = format == 'json'
        result = self.session.query(method_url, decode=decode)
        return result
    # https://api.covalenthq.com/v1/{chain_id}/xy=k/{dexname}/tokens/address/{address}/
    def tokenDataByAddress(self, chain_id,dexname,address):
        if chain_id not in list(constants.AVAILABLE_CHAIN_IDS.values()):
            raise Exception(
                "chain_id should be one of {}".format(
                    list(constants.AVAILABLE_CHAIN_IDS.values())
                )
            )
        if dexname not in list(constants.AVAILABLE_DEXES.values()):
            raise Exception(
                "dexname should be one of {}".format(
                    list(constants.AVAILABLE_DEXES.values())
                )
            )
        method_url = (
            'v1/{chain_id}/xy=k/{dexname}/tokens/address/{address}/'.format(
                chain_id=chain_id,
                dexname=dexname,
                address=address
            )
        )
        decode = format == 'json'
        result = self.session.query(method_url, decode=decode)
        return result
    # https://api.covalenthq.com/v1/{chain_id}/xy=k/{dexname}/tokens/address/{address}/transactions/
    def tokenTransactionsByAddress(self, chain_id,dexname,address):
        if chain_id not in list(constants.AVAILABLE_CHAIN_IDS.values()):
            raise Exception(
                "chain_id should be one of {}".format(
                    list(constants.AVAILABLE_CHAIN_IDS.values())
                )
            )
        if dexname not in list(constants.AVAILABLE_DEXES.values()):
            raise Exception(
                "dexname should be one of {}".format(
                    list(constants.AVAILABLE_DEXES.values())
                )
            )
        method_url = (
            'v1/{chain_id}/xy=k/{dexname}/tokens/address/{address}/transactions/'.format(
                chain_id=chain_id,
                dexname=dexname,
                address=address
            )
        )
        decode = format == 'json'
        result = self.session.query(method_url, decode=decode)
        return result
    # https://api.covalenthq.com/v1/{chain_id}/xy=k/{dexname}/address/{address}/balances/
    def addressExchangesBalances(self, chain_id,dexname,address):
        if chain_id not in list(constants.AVAILABLE_CHAIN_IDS.values()):
            raise Exception(
                "chain_id should be one of {}".format(
                    list(constants.AVAILABLE_CHAIN_IDS.values())
                )
            )
        if dexname not in list(constants.AVAILABLE_DEXES.values()):
            raise Exception(
                "dexname should be one of {}".format(
                    list(constants.AVAILABLE_DEXES.values())
                )
            )
        method_url = (
            'v1/{chain_id}/xy=k/{dexname}/address/{address}/balances/'.format(
                chain_id=chain_id,
                dexname=dexname,
                address=address
            )
        )
        decode = format == 'json'
        result = self.session.query(method_url, decode=decode)
        return result
    # https://api.covalenthq.com/v1/{chain_id}/xy=k/{dexname}/address/{address}/transactions/
    def addressExchangesLiqudityTransactions(self, chain_id,dexname,address):
        if chain_id not in list(constants.AVAILABLE_CHAIN_IDS.values()):
            raise Exception(
                "chain_id should be one of {}".format(
                    list(constants.AVAILABLE_CHAIN_IDS.values())
                )
            )
        if dexname not in list(constants.AVAILABLE_DEXES.values()):
            raise Exception(
                "dexname should be one of {}".format(
                    list(constants.AVAILABLE_DEXES.values())
                )
            )
        method_url = (
            'v1/{chain_id}/xy=k/{dexname}/address/{address}/transactions/'.format(
                chain_id=chain_id,
                dexname=dexname,
                address=address
            )
        )
        decode = format == 'json'
        result = self.session.query(method_url, decode=decode)
        return result