"""
Provide implementation for bridges entrypoints.
"""
from essentia_bridges.bridges.wallets import Wallets
from essentia_bridges.constants import PUBLIC_ESSENTIA_WALLETS_BRIDGE_API_HOST


class EssentiaBridges:
    """
    Proxy class for bridges.
    """

    def __init__(self, host=PUBLIC_ESSENTIA_WALLETS_BRIDGE_API_HOST, port=None):

        if port is None:
            self.wallets_bridge_api_url = host + '/api/v1/'

        if port is not None:
            self.wallets_bridge_api_url = host + ':' + str(port) + '/api/v1/'

    @property
    def wallets(self):
        """
        Wallets bridge proxy property.
        """
        return Wallets(wallets_bridge_api_url=self.wallets_bridge_api_url)

essentia_bridges = EssentiaBridges()
