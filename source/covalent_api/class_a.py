# :coding: utf-8
# :copyright: Copyright (c) 2021 Lluis Casals Marsol
# Copyright 2021 Lluis Casals Marsol.
# All rights reserved.
# Please see the LICENSE file that should have been included as part of this
# package.


from covalent_api import constants


class ClassA(object):

    @property
    def session(self):
        return self._session

    def __init__(self, session):
        self._session = session

    def get_token_balances_for_address(
            self, chain_id, address, nft=False, no_nft_fetch=False, format="json"
    ):
        '''
        Return a list of all ERC20 and NFT token balances along with their
        current spot prices.

        :param chain_id: Chain ID of the Blockchain being queried. Currently
        supports 1 for Ethereum Mainnet, 137 for Polygon/Matic Mainnet, 80001
        for Polygon/Matic Mumbai Testnet, 56 for Binance Smart Chain, 43114 for
        Avalanche C-Chain Mainnet, 43113 for Fuji C-Chain Testnet, and 250 for
        Fantom Opera Mainnet.
        :type chain_id: string
        :param address: Passing in an ENS resolves automatically.
        :type address: string
        :param nft: Set to true to return ERC721 and ERC1155 assets. Defaults to
        false.
        :type nft: boolean
        :param no_nft_fetch: Set to true to skip fetching NFT metadata, which
        can result in faster responses. Defaults to false and only applies when
        nft=true.
        :type no_nft_fetch: boolean
        :param format: If format=csv, return a flat CSV instead of JSON responses.
        :type format: string
        '''
        # TODO: on the api docs says the following for the address argument:
        #  Passing in an ENS resolves automatically. But I don't know what an
        #  ENS is.
        if chain_id not in list(constants.AVAILABLE_CHAIN_IDS.values()):
            raise Exception(
                "chain_id should be one of {}".format(
                    list(constants.AVAILABLE_CHAIN_IDS.values())
                )
            )

        method_url = '/v1/{chain_id}/address/{address}/balances_v2/'.format(chain_id=chain_id,address=address)
        params = {
            'nft': nft,
            'no-nft-fetch': no_nft_fetch,
            'format': format
        }
        decode = format == 'json'

        result = self.session.query(method_url, params, decode=decode)
        return result

    def get_historical_portfolio_value_over_time(
            self, chain_id, address, quote_currency=None, format="json"
    ):
        '''
        Given chain_id and wallet address, return wallet value for the last 30 days at 24 hour timestamps
        
        :param chain_id: Chain ID of the Blockchain being queried. Currently
        supports 1 for Ethereum Mainnet, 137 for Polygon/Matic Mainnet, 80001
        for Polygon/Matic Mumbai Testnet, 56 for Binance Smart Chain, 43114 for
        Avalanche C-Chain Mainnet, 43113 for Fuji C-Chain Testnet, and 250 for
        Fantom Opera Mainnet.
        :type chain_id: string
        :param address: Passing in an ENS resolves automatically.
        :type address: string
        :param quote_currency: The requested fiat currency.
        :type quote_currency: string
        :param format: If format=csv, return a flat CSV instead of JSON responses.
        :type format: string
        '''
        if chain_id not in list(constants.AVAILABLE_CHAIN_IDS.values()):
            raise Exception(
                "chain_id should be one of {}".format(
                    list(constants.AVAILABLE_CHAIN_IDS.values())
                )
            )

        method_url = '/v1/{chain_id}/address/{address}/portfolio_v2/'.format(chain_id=chain_id,address=address)
        params = {
            'quote-currency': quote_currency,
            'format': format
        }
        decode = format == 'json'

        result = self.session.query(method_url, params, decode=decode)
        return result

    def get_transactions(
            self, chain_id, address, block_signed_at_asc=None, no_logs=None,
            page_number=None, page_size=None, format="json"
    ):
        '''
        
        :param chain_id: Chain ID of the Blockchain being queried. Currently
        supports 1 for Ethereum Mainnet, 137 for Polygon/Matic Mainnet, 80001
        for Polygon/Matic Mumbai Testnet, 56 for Binance Smart Chain, 43114 for
        Avalanche C-Chain Mainnet, 43113 for Fuji C-Chain Testnet, and 250 for
        Fantom Opera Mainnet.
        :type chain_id: string 
        :param address: Passing in an ENS resolves automatically. 
        :type address: string 
        :param block_signed_at_asc: Sort the transactions in chronological
        ascending order. By default, it's set to false and returns transactions
        in chronological descending order.
        :type block_signed_at_asc: bool
        :param no_logs: Setting this to true will omit decoded event logs, 
        resulting in lighter and faster responses. By default it's set to false.
        :type no_logs: boolean
        :param page_number: The specific page to be returned.
        :type page_number: int32
        :param page_size: The number of results per page.
        :type page_size: int32
        :param format: If format=csv, return a flat CSV instead of JSON responses. 
        :type format: string 
         
         
        '''

        if chain_id not in list(constants.AVAILABLE_CHAIN_IDS.values()):
            raise Exception(
                "chain_id should be one of {}".format(
                    list(constants.AVAILABLE_CHAIN_IDS.values())
                )
            )

        method_url = '/v1/{chain_id}/address/{address}/transactions_v2/'.format(chain_id=chain_id,address=address)
        params = {
            'block-signed-at-asc': block_signed_at_asc,
            'no-logs': no_logs,
            'page-number': page_number,
            'page-size': page_size,
            'format': format
        }
        decode = format == 'json'

        result = self.session.query(method_url, params, decode=decode)
        return result

    def get_erc20_token_transfers(
            self, chain_id, address, contract_address=None,
            page_number=None, page_size=None, format="json"
    ):
        '''
        
        :param chain_id: Chain ID of the Blockchain being queried. Currently
        supports 1 for Ethereum Mainnet, 137 for Polygon/Matic Mainnet, 80001
        for Polygon/Matic Mumbai Testnet, 56 for Binance Smart Chain, 43114 for
        Avalanche C-Chain Mainnet, 43113 for Fuji C-Chain Testnet, and 250 for
        Fantom Opera Mainnet.
        :type chain_id: string 
        :param address: Passing in an ENS resolves automatically. 
        :type address: string 
        :param contract_address: 
        :type contract_address: 
        :param page_number: The specific page to be returned.
        :type page_number: int32
        :param page_size: The number of results per page.
        :type page_size: int32
        :param format: If format=csv, return a flat CSV instead of JSON responses. 
        :type format: string 
         
         
        '''

        if chain_id not in list(constants.AVAILABLE_CHAIN_IDS.values()):
            raise Exception(
                "chain_id should be one of {}".format(
                    list(constants.AVAILABLE_CHAIN_IDS.values())
                )
            )

        method_url = '/v1/{chain_id}/address/{address}/transfers_v2/'.format(chain_id=chain_id,address=address)
        params = {
            'contract-address': contract_address,
            'page-number': page_number,
            'page-size': page_size,
            'format': format
        }
        decode = format == 'json'

        result = self.session.query(method_url, params, decode=decode)
        return result

    def get_block(
            self, chain_id, block_height, format="json"
    ):
        '''
        
        :param chain_id: Chain ID of the Blockchain being queried. Currently
        supports 1 for Ethereum Mainnet, 137 for Polygon/Matic Mainnet, 80001
        for Polygon/Matic Mumbai Testnet, 56 for Binance Smart Chain, 43114 for
        Avalanche C-Chain Mainnet, 43113 for Fuji C-Chain Testnet, and 250 for
        Fantom Opera Mainnet.
        :type chain_id: string 
        :param block_height: 
        :type block_height: 
        :param format: If format=csv, return a flat CSV instead of JSON responses. 
        :type format: string 
         
         
        '''
        
        if chain_id not in list(constants.AVAILABLE_CHAIN_IDS.values()):
            raise Exception(
                "chain_id should be one of {}".format(
                    list(constants.AVAILABLE_CHAIN_IDS.values())
                )
            )

        method_url = '/v1/{chain_id}/block_v2/{block_height}/'.format(chain_id=chain_id, block_height=block_height)
        params = {
            'format': format
        }
        decode = format == 'json'

        result = self.session.query(method_url, params, decode=decode)
        return result

    def get_log_events_by_contract_address(
            self, chain_id, address, starting_block, ending_block,
            page_number=None, page_size=None, format="json"
    ):
        '''
        
        :param chain_id: Chain ID of the Blockchain being queried. Currently
        supports 1 for Ethereum Mainnet, 137 for Polygon/Matic Mainnet, 80001
        for Polygon/Matic Mumbai Testnet, 56 for Binance Smart Chain, 43114 for
        Avalanche C-Chain Mainnet, 43113 for Fuji C-Chain Testnet, and 250 for
        Fantom Opera Mainnet.
        :type chain_id: string 
        :param address: Passing in an ENS resolves automatically. 
        :type address: string 
        :param starting_block: 
        :type starting_block: 
        :param ending_block: 
        :type ending_block: 
        :param page_number: The specific page to be returned.
        :type page_number: int32
        :param page_size: The number of results per page.
        :type page_size: int32
        :param format: If format=csv, return a flat CSV instead of JSON responses. 
        :type format: string 
         
         
        '''

        if chain_id not in list(constants.AVAILABLE_CHAIN_IDS.values()):
            raise Exception(
                "chain_id should be one of {}".format(
                    list(constants.AVAILABLE_CHAIN_IDS.values())
                )
            )


        method_url = '/v1/{chain_id}/events/address/{address}/'.format(chain_id=chain_id, address=address)
        params = {
            'starting-block': starting_block,
            'ending-block': ending_block,
            'page-number': page_number,
            'page-size': page_size,
            'format': format
        }
        decode = format == 'json'

        result = self.session.query(method_url, params, decode=decode)
        return result

    def get_log_events_by_topic_hash(
            self, chain_id, topic, starting_block, ending_block, sender_address=None,
            page_number=None, page_size=None, format="json"
    ):
        '''
        
        :param chain_id: Chain ID of the Blockchain being queried. Currently
        supports 1 for Ethereum Mainnet, 137 for Polygon/Matic Mainnet, 80001
        for Polygon/Matic Mumbai Testnet, 56 for Binance Smart Chain, 43114 for
        Avalanche C-Chain Mainnet, 43113 for Fuji C-Chain Testnet, and 250 for
        Fantom Opera Mainnet.
        :type chain_id: string 
        :param topic: 
        :type topic: 
        :param starting_block: 
        :type starting_block: 
        :param ending_block: 
        :type ending_block: 
        :param sender_address: 
        :type sender_address: 
        :param page_number: The specific page to be returned.
        :type page_number: int32
        :param page_size: The number of results per page.
        :type page_size: int32
        :param format: If format=csv, return a flat CSV instead of JSON responses. 
        :type format: string 
         
         
        '''

        if chain_id not in list(constants.AVAILABLE_CHAIN_IDS.values()):
            raise Exception(
                "chain_id should be one of {}".format(
                    list(constants.AVAILABLE_CHAIN_IDS.values())
                )
            )

        method_url = '/v1/{chain_id}/events/topics/{topic}/'.format(chain_id=chain_id, topic=topic)
        params = {
            'sender-address': sender_address,
            'starting-block': starting_block,
            'ending-block': ending_block,
            'page-number': page_number,
            'page-size': page_size,
            'format': format
        }
        decode = format == 'json'

        result = self.session.query(method_url, params, decode=decode)
        return result

    def get_external_nft_metadata(
            self, chain_id, address, token_id, format="json"
    ):
        '''
        
        :param chain_id: Chain ID of the Blockchain being queried. Currently
        supports 1 for Ethereum Mainnet, 137 for Polygon/Matic Mainnet, 80001
        for Polygon/Matic Mumbai Testnet, 56 for Binance Smart Chain, 43114 for
        Avalanche C-Chain Mainnet, 43113 for Fuji C-Chain Testnet, and 250 for
        Fantom Opera Mainnet.
        :type chain_id: string 
        :param address: Passing in an ENS resolves automatically. 
        :type address: string 
        :param token_id: 
        :type token_id: 
        :param format: If format=csv, return a flat CSV instead of JSON responses. 
        :type format: string 
         
         
        '''

        if chain_id not in list(constants.AVAILABLE_CHAIN_IDS.values()):
            raise Exception(
                "chain_id should be one of {}".format(
                    list(constants.AVAILABLE_CHAIN_IDS.values())
                )
            )

        method_url = '/v1/{chain_id}/tokens/{address}/nft_metadata/{token_id}/'.format(chain_id=chain_id, address=address, token_id=token_id)
        params = {
            'format': format
        }
        decode = format == 'json'

        result = self.session.query(method_url, params, decode=decode)
        return result

    def get_nft_token_ids(
            self, chain_id, address, page_number=None, page_size=None,
            format="json"
    ):
        '''
        
        :param chain_id: Chain ID of the Blockchain being queried. Currently
        supports 1 for Ethereum Mainnet, 137 for Polygon/Matic Mainnet, 80001
        for Polygon/Matic Mumbai Testnet, 56 for Binance Smart Chain, 43114 for
        Avalanche C-Chain Mainnet, 43113 for Fuji C-Chain Testnet, and 250 for
        Fantom Opera Mainnet.
        :type chain_id: string 
        :param address: Passing in an ENS resolves automatically. 
        :type address: string 
        :param page_number: The specific page to be returned.
        :type page_number: int32
        :param page_size: The number of results per page.
        :type page_size: int32
        :param format: If format=csv, return a flat CSV instead of JSON responses. 
        :type format: string 
         
         
        '''

        if chain_id not in list(constants.AVAILABLE_CHAIN_IDS.values()):
            raise Exception(
                "chain_id should be one of {}".format(
                    list(constants.AVAILABLE_CHAIN_IDS.values())
                )
            )

        method_url = '/v1/{chain_id}/tokens/{address}/nft_token_ids/'.format(chain_id=chain_id, address=address)
        params = {
            'page-number': page_number,
            'page-size': page_size,
            'format': format
        }
        decode = format == 'json'

        result = self.session.query(method_url, params, decode=decode)
        return result

    def get_nft_transactions(
            self, chain_id, address, token_id, page_number=None, page_size=None,
            format="json"
    ):
        '''
        
        :param chain_id: Chain ID of the Blockchain being queried. Currently
        supports 1 for Ethereum Mainnet, 137 for Polygon/Matic Mainnet, 80001
        for Polygon/Matic Mumbai Testnet, 56 for Binance Smart Chain, 43114 for
        Avalanche C-Chain Mainnet, 43113 for Fuji C-Chain Testnet, and 250 for
        Fantom Opera Mainnet.
        :type chain_id: string 
        :param address: Passing in an ENS resolves automatically. 
        :type address: string 
        :param token_id: 
        :type token_id: 
        :param page_number: The specific page to be returned.
        :type page_number: int32
        :param page_size: The number of results per page.
        :type page_size: int32
        :param format: If format=csv, return a flat CSV instead of JSON responses. 
        :type format: string 
         
         
        '''

        if chain_id not in list(constants.AVAILABLE_CHAIN_IDS.values()):
            raise Exception(
                "chain_id should be one of {}".format(
                    list(constants.AVAILABLE_CHAIN_IDS.values())
                )
            )

        method_url = '/v1/{chain_id}/tokens/{address}/nft_transactions/{token_id}/'.format(chain_id=chain_id, address=address, token_id=token_id)
        params = {
            'page-number': page_number,
            'page-size': page_size,
            'format': format
        }
        decode = format == 'json'

        result = self.session.query(method_url, params, decode=decode)
        return result

    def get_changes_token_holders_between_two_block_heights(
            self, chain_id, address, starting_block, ending_block=None,
            page_number=None, page_size=None, format="json"
    ):
        '''
        
        :param chain_id: Chain ID of the Blockchain being queried. Currently
        supports 1 for Ethereum Mainnet, 137 for Polygon/Matic Mainnet, 80001
        for Polygon/Matic Mumbai Testnet, 56 for Binance Smart Chain, 43114 for
        Avalanche C-Chain Mainnet, 43113 for Fuji C-Chain Testnet, and 250 for
        Fantom Opera Mainnet.
        :type chain_id: string 
        :param address: Passing in an ENS resolves automatically. 
        :type address: string 
        :param starting_block: 
        :type starting_block: 
        :param ending_block: 
        :type ending_block: 
        :param page_number: The specific page to be returned.
        :type page_number: int32
        :param page_size: The number of results per page.
        :type page_size: int32
        :param format: If format=csv, return a flat CSV instead of JSON responses. 
        :type format: string 
         
         
        '''

        if chain_id not in list(constants.AVAILABLE_CHAIN_IDS.values()):
            raise Exception(
                "chain_id should be one of {}".format(
                    list(constants.AVAILABLE_CHAIN_IDS.values())
                )
            )

        method_url = '/v1/{chain_id}/tokens/{address}/token_holders_changes/'.format(chain_id=chain_id, address=address)
        params = {
            'starting_block': starting_block,
            'ending_block': ending_block,
            'page-number': page_number,
            'page-size': page_size,
            'format': format
        }
        decode = format == 'json'

        result = self.session.query(method_url, params, decode=decode)
        return result

    def get_token_holders_as_of_a_block_height(
            self, chain_id, address, block_height=None,
            page_number=None, page_size=None, format="json"
    ):
        '''
        
        :param chain_id: Chain ID of the Blockchain being queried. Currently
        supports 1 for Ethereum Mainnet, 137 for Polygon/Matic Mainnet, 80001
        for Polygon/Matic Mumbai Testnet, 56 for Binance Smart Chain, 43114 for
        Avalanche C-Chain Mainnet, 43113 for Fuji C-Chain Testnet, and 250 for
        Fantom Opera Mainnet.
        :type chain_id: string 
        :param address: Passing in an ENS resolves automatically. 
        :type address: string 
        :param block_height: 
        :type block_height: 
        :param page_number: The specific page to be returned.
        :type page_number: int32
        :param page_size: The number of results per page.
        :type page_size: int32
        :param format: If format=csv, return a flat CSV instead of JSON responses. 
        :type format: string 
         
         
        '''

        if chain_id not in list(constants.AVAILABLE_CHAIN_IDS.values()):
            raise Exception(
                "chain_id should be one of {}".format(
                    list(constants.AVAILABLE_CHAIN_IDS.values())
                )
            )

        method_url = '/v1/{chain_id}/tokens/{address}/token_holders/'.format(chain_id=chain_id, address=address)
        params = {
            'block-height': block_height,
            'page-number': page_number,
            'page-size': page_size,
            'format': format
        }
        decode = format == 'json'

        result = self.session.query(method_url, params, decode=decode)
        return result

    def get_all_contract_metadata(
            self, chain_id, id, page_number=None, page_size=None, format="json"
    ):
        '''
        
        :param chain_id: Chain ID of the Blockchain being queried. Currently
        supports 1 for Ethereum Mainnet, 137 for Polygon/Matic Mainnet, 80001
        for Polygon/Matic Mumbai Testnet, 56 for Binance Smart Chain, 43114 for
        Avalanche C-Chain Mainnet, 43113 for Fuji C-Chain Testnet, and 250 for
        Fantom Opera Mainnet.
        :type chain_id: string 
        :param id: 
        :type id: 
        :param page_number: The specific page to be returned.
        :type page_number: int32
        :param page_size: The number of results per page.
        :type page_size: int32
        :param format: If format=csv, return a flat CSV instead of JSON responses. 
        :type format: string 
         
         
        '''
        if chain_id not in list(constants.AVAILABLE_CHAIN_IDS_CONTRACT_METADATA.values()):
            raise Exception(
                "chain_id should be one of {}".format(
                    list(constants.AVAILABLE_CHAIN_IDS_CONTRACT_METADATA.values())
                )
            )
        if id != 'all':
            raise Exception(
                "Only all is supported right now"
            )

        method_url = '/v1/{chain_id}/tokens/tokenlists/{id}/'.format(chain_id=chain_id, id=id)
        params = {
            'page-number': page_number,
            'page-size': page_size,
            'format': format
        }
        decode = format == 'json'

        result = self.session.query(method_url, params, decode=decode)
        return result

    def get_a_transaction(
            self, chain_id, tx_hash, no_logs=None, page_number=None,
            page_size=None, format="json"
    ):
        '''
        
        :param chain_id: Chain ID of the Blockchain being queried. Currently
        supports 1 for Ethereum Mainnet, 137 for Polygon/Matic Mainnet, 80001
        for Polygon/Matic Mumbai Testnet, 56 for Binance Smart Chain, 43114 for
        Avalanche C-Chain Mainnet, 43113 for Fuji C-Chain Testnet, and 250 for
        Fantom Opera Mainnet.
        :type chain_id: string 
        :param tx_hash: 
        :type tx_hash: 
        :param no_logs: Setting this to true will omit decoded event logs, resulting in lighter and faster responses. By default it's set to false.
        :type no_logs: boolean
        :param page_number: The specific page to be returned.
        :type page_number: int32
        :param page_size: The number of results per page.
        :type page_size: int32
        :param format: If format=csv, return a flat CSV instead of JSON responses. 
        :type format: string 
         
         
        '''
        if chain_id not in list(constants.AVAILABLE_CHAIN_IDS.values()):
            raise Exception(
                "chain_id should be one of {}".format(
                    list(constants.AVAILABLE_CHAIN_IDS.values())
                )
            )

        method_url = '/v1/{chain_id}/transaction_v2/{tx_hash}/'.format(chain_id=chain_id, tx_hash=tx_hash)
        params = {
            'no-logs': no_logs,
            'page-number': page_number,
            'page-size': page_size,
            'format': format
        }
        decode = format == 'json'

        result = self.session.query(method_url, params, decode=decode)
        return result
