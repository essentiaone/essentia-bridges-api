"""
Provide implementation of abstract wallet.
"""
from abc import abstractmethod

import requests

from essentia_bridges.constants import DEFAULT_HEADERS


class AbstractWalletsBridgeNetwork:
    """
    Abstract wallet implementation.
    """

    @abstractmethod
    def wallet_name(self):
        """
        Wallet name to put into URL.
        """
        return

    def get_balance(self, address):
        """
        Get wallet balance.
        """
        return requests.get(self.wallets_bridge_api_url + f'{self.wallet_name}/wallets/{address}/balance').json()

    def get_transaction_information(self, transaction_hash):
        """
        Get transaction information.
        """
        return requests.get(self.wallets_bridge_api_url + f'{self.wallet_name}/transactions/{transaction_hash}').json()

    def send_transaction(self, raw_transaction_hash):
        """
        Send transaction.

        Send signed raw transaction to the blockchain through the bridge.
        """
        parameters = {
            'data': raw_transaction_hash,
        }

        return requests.post(
            self.wallets_bridge_api_url + f'{self.wallet_name}/wallets/transactions',
            json=parameters,
            headers=DEFAULT_HEADERS,
        ).json()
