"""
Provide implementation for abstract wallet.
"""
from abc import abstractmethod

import requests

from bridges_api.constants import (
    DEFAULT_HEADERS,
    WALLETS_BRIDGE_API_URL,
)

class AbstractWalletsBridgeNetwork:
    """
    Abstract wallet implementation.
    """

    @abstractmethod
    def wallet_name(self):
        """
        Wallet name to put it into URL.
        """
        return ETHEREUM_WALLET_URL_SLUG

    def get_balance(self, address):
        """
        Get wallet balance.
        """
        return requests.get(WALLETS_BRIDGE_API_URL + f'{self.wallet_name}/wallets/{address}/balance')

    def get_transaction_information(self, transaction_hash):
        """
        Get transaction information.
        """
        return requests.get(WALLETS_BRIDGE_API_URL + f'{self.wallet_name}/transactions/{transaction_hash}')

    def send_transaction(self, raw_transaction_hash):
        """
        Send transaction.

        Send signed raw transaction to the blockchain through bridge.
        """
        parameters = {
            'data': raw_transaction_hash,
        }

        return requests.post(
            WALLETS_BRIDGE_API_URL + f'{self.wallet_name}/wallets/transactions',
            json=parameters,
            headers=DEFAULT_HEADERS,
        )
