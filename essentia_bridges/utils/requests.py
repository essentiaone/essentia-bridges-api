"""
Provide implementation for requests utilities.
"""
from urllib.parse import urlencode


class GetRequestParameters:
    """
    Get request utilities implementation.
    """

    @staticmethod
    def create(parameters):
        """
        Create get request parameters from dictionaries.
        """
        return '?' + urlencode(list(parameters.items()))
