"""
Provide implementation for bridges entrypoints.
"""
from bridges_api.bridges.wallets import Wallets


class Bridge:
    """
    Proxy class for bridges.
    """

    @property
    def wallets(self):
        """
        Wallets bridge proxy property.
        """
        return Wallets()


bridges = Bridge()
