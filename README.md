# essentia-bridges-api

The API wrapper written in Python allow you to speak with Bridges REST API in pythonic way.

[![Release](https://img.shields.io/github/release/essentiaone/essentia-bridges-api.svg)](https://github.com/essentiaone/essentia-bridges-api/releases)
![Python36](https://img.shields.io/badge/Python-3.6-brightgreen.svg)

## Installing

Install and update using `pip3`:

```
$ pip3 install essentia-bridges-api
```

## Usage

```python
>>> from bridges_api import bridges
>>> bridges.wallets.ethereum.get_balance(address='0xb563Dde324fa9842E74bbf98571e9De4FD5FE9bA').json()
{'result': {'balance': 0.07724806191011209}}
```
