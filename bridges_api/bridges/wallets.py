"""
Provide implementation for bridge wallets.
"""
import requests

from bridges_api.abc.wallet import AbstractWalletsBridgeNetwork
from bridges_api.constants import (
    DEFAULT_HEADERS,
    ETHEREUM_WALLET_NAME,
    WALLETS_BRIDGE_API_URL,
)
from bridges_api.utils.requests import GetRequestParameters


class EthereumWallet(AbstractWalletsBridgeNetwork):
    """
    Ethereum wallet implementation.
    """

    def __init__(self):
        self.get_request_parameters = GetRequestParameters()

    @property
    def wallet_name(self):
        """
        Wallet name.
        """
        return ETHEREUM_WALLET_NAME

    def get_transactions_count(self, address):
        """
        Get count of transactions.
        """
        return requests.get(WALLETS_BRIDGE_API_URL + f'{self.wallet_name}/wallets/{address}/transactions/count').json()

    def get_gas_price(self):
        """
        Get gas price.
        """
        return requests.get(WALLETS_BRIDGE_API_URL + f'{self.wallet_name}/gas/price').json()

    def get_gas_estimate(self, address_from, address_to, data='0x'):
        """
        Get gas estimate.
        """
        parameters = {
            'from': address_from,
            'to': address_to,
            'data': data,
        }

        return requests.post(
            WALLETS_BRIDGE_API_URL + f'{self.wallet_name}/gas/estimate',
            json=parameters,
            headers=DEFAULT_HEADERS,
        ).json()

    def get_block_number(self):
        """
        Get last block number.
        """
        return requests.get(WALLETS_BRIDGE_API_URL + f'{self.wallet_name}/block-number').json()

    def get_smart_contracts_count(self, address, data):
        """
        Get count of smart-contracts.
        """
        parameters = {
            'to': address,
            'data': data,
        }

        return requests.post(
            WALLETS_BRIDGE_API_URL + f'{self.wallet_name}/smart-contracts',
            json=parameters,
            headers=DEFAULT_HEADERS,
        ).json()

    def get_receipt(self, transaction_hash):
        """
        Get receipt of transaction.
        """
        return requests.get(
            WALLETS_BRIDGE_API_URL + f'{self.wallet_name}/transactions/receipts/{transaction_hash}'
        ).json()


class ThirdPartyEthereumWallet(AbstractWalletsBridgeNetwork):
    """
    Third-party Ethereum wallet implementation.
    """

    @property
    def wallet_name(self):
        """
        Wallet name.
        """
        return ETHEREUM_WALLET_NAME

    def get_gas_price(self):
        """
        Get gas price.
        """
        return requests.get(WALLETS_BRIDGE_API_URL + f'third-party/{self.wallet_name}/gas-station/gas/price').json()


class WalletsThirdParty:
    """
    Proxy class for third-party services related to wallets.
    """

    @property
    def ethereum(self):
        """
        Third-party Ethereum wallet proxy property.
        """
        return ThirdPartyEthereumWallet()


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

    @property
    def third_party(self):
        """
        Third-party wallets proxy property.
        """
        return WalletsThirdParty()