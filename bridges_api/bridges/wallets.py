"""
Provide implementation for bridge wallets.
"""
import requests

from bridges_api.abc.wallet import AbstractWalletsBridgeNetwork
from bridges_api.constants import (
    ETHEREUM_WALLET_NAME,
    WALLETS_BRIDGE_API_URL,
)


class EthereumWallet(AbstractWalletsBridgeNetwork):
    """
    Ethereum wallet implementation.
    """

    @property
    def wallet_name(self):
        return ETHEREUM_WALLET_NAME

    def get_transactions_count(self, address):
        """
        Get count of the transactions.
        """
        return requests.get(WALLETS_BRIDGE_API_URL + f'{self.wallet_name}/wallets/{address}/transactions/count')

    def get_gas_price(self):
        """
        Get gas price.
        """
        return requests.get(WALLETS_BRIDGE_API_URL + f'{self.wallet_name}/gas/price')

    def get_gas_estimate(self, address, data='0x'):
        """
        Get gas estimate.
        """
        return requests.get(WALLETS_BRIDGE_API_URL + f'{self.wallet_name}/gas/estimate' + '?' + f'address={address}&data={data}')

    def get_block_number(self):
        """
        Get last block number.
        """
        return requests.get(WALLETS_BRIDGE_API_URL + f'{self.wallet_name}/block-number')


class Wallets:
    """
    Proxy class for wallets.
    """

    @property
    def ethereum(self):
        """
        Ethereum wallet proxy property.
        """
        return EthereumWallet()
