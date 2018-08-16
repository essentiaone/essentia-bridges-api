# essentia-bridges-api

The API wrapper written in Python allow you to speak with Bridges REST API in pythonic way.

[![Release](https://img.shields.io/github/release/essentiaone/essentia-bridges-api.svg)](https://github.com/essentiaone/essentia-bridges-api/releases)
![Python36](https://img.shields.io/badge/Python-3.6-brightgreen.svg)


  * [Getting started](#getting-started)
  * [API documentation](#api)
    * [Wallets](#wallets)
      * [Ethereum wallet](#ethereum-wallet)

## Getting started

Install and update using `pip3`:

```
$ pip3 install essentia-bridges-api
```

Simple usage of the library introduced below:

```python
>>> from bridges_api import bridges
>>> address = '0xb563Dde324fa9842E74bbf98571e9De4FD5FE9bA'
>>> bridges.wallets.ethereum.get_balance(address=address)
{
    "result": {
        "balance": 0.07724806191011209
    }
}
```

## API

### Wallets

#### Ethereum wallet

Get balance of the wallet — `bridges.wallets.ethereum.get_balance`

| Arguments | Type   | Required | Description                  |
| :--------:|:------:|:--------:|------------------------------|
| address   | String | Yes      | Address to get balance from. |

```python
>>> address = '0xb563Dde324fa9842E74bbf98571e9De4FD5FE9bA'
>>> bridges.wallets.ethereum.get_balance(address=address)
{
    "result": {
        "balance": 0.07724806191011209
    }
}
```

Get information of the particular transaction of the wallet — `bridges.wallets.ethereum.get_transaction_information`

| Arguments        | Type   | Required | Description       |
| :---------------:|:------:|:--------:|-------------------|
| transaction_hash | String | Yes      | Transaction hash. |

```python
>>> transaction_hash = '0x86e03096f808820404c62dea12c7c59cdc74fdbd9020b0d71c8aba39b4a143bb'
>>> bridges.wallets.ethereum.get_transaction_information(transaction_hash=transaction_hash)
{
    "result": {
        "blockHash": "0x91a823e7c029d78ea1d46fd8aad5e8b631683a11c2ee5582f0ea5c845fbf5e64",
        "blockNumber": "0x5c23e0",
        "from": "0xb563dde324fa9842e74bbf98571e9de4fd5fe9ba",
        "gas": "0x5208",
        "gasPrice": "0x28fa6ae00",
        "hash": "0x86e03096f808820404c62dea12c7c59cdc74fdbd9020b0d71c8aba39b4a143bb",
        "input": "0x",
        "nonce": "0x73",
        "r": "0xe25959a60754de7d5480ce6cdfaa4eba3512e17c88811ca73cbbbbb67343e63b",
        "s": "0x530f09c33dbd90ac12be34b3eaea394476a88cbde85f63942d466e583a99ad9",
        "to": "0x4aa548d7589f003486892777cbb0b70dff5d6949",
        "transactionIndex": "0x76",
        "v": "0x25",
        "value": "0xaa87bee538000"
    }
}
```

Send raw transaction hash to blockchain — `bridges.wallets.ethereum.send_transaction`

| Arguments            | Type   | Required | Description                                        |
| :-------------------:|:------:|:--------:|----------------------------------------------------|
| raw_transaction_hash | String | Yes      | Signed raw transaction hash to send to blockchain. |

```python
>>> raw_transaction_hash = '0xf86b7485028fa6ae00825208944aa548d7589f003486892777cbb..'
>>> bridges.wallets.ethereum.send_transaction(raw_transaction_hash=raw_transaction_hash)
{
    "result": "0x9d8c5483c25a26a69b6b3b831ce68a917d1dec22a56882c4ea84a0d5ff14785c"
}
```

Get transactions count of the wallet — `bridges.wallets.ethereum.get_transactions_count`

| Arguments | Type   | Required | Description                             |
| :--------:|:------:|:--------:|-----------------------------------------|
| address   | String | Yes      | Address to get transactions count from. |

```python
>>> address = '0xb563Dde324fa9842E74bbf98571e9De4FD5FE9bA'
>>> bridges.wallets.ethereum.get_transactions_count(address=address)
{
    "result": 117
}
```

Get gas price — `bridges.wallets.ethereum.get_gas_price`

```python
>>> bridges.wallets.ethereum.get_gas_price()
{
    "result": 100000000
}
```

Get gas limit estimate  — `bridges.wallets.ethereum.get_gas_estimate` 

| Arguments | Type   | Required | Description                                           |
| :--------:|:------:|:--------:|-------------------------------------------------------|
| address   | String | Yes      | Address to get estimate for.                          |
| data      | String | No       | Arbitrary message of transaction. By default is "0x". |

```python
>>> address = '0xb563Dde324fa9842E74bbf98571e9De4FD5FE9bA'
>>> bridges.wallets.ethereum.get_gas_estimate(address=address)
{
    "result": 21000
}
```

Get block number — `bridges.wallets.ethereum.get_block_number`

```python
>>> bridges.wallets.ethereum.get_block_number()
{
    "result": 6062378
}
```

Get smart-contracts count  — `bridges.wallets.ethereum.get_smart_contracts_count`

| Arguments | Type   | Required | Description                                           |
| :--------:|:------:|:--------:|-------------------------------------------------------|
| address   | String | Yes      | Address to get smart-contracts count from.            |
| data      | String | Yes      | Arbitrary message of transaction. By default is "0x". |

```python
>>> address = '0xb563Dde324fa9842E74bbf98571e9De4FD5FE9bA'
>>> bridges.wallets.ethereum.get_smart_contracts_count(address=address, data=data)
{
    "result": 2
}
```

Get receipt of transaction  — `bridges.wallets.ethereum.get_receipt`

| Arguments        | Type   | Required | Description       |
| :---------------:|:------:|:--------:|-------------------|
| transaction_hash | String | Yes      | Transaction hash. |

```python
>>> transaction_hash = '0x86e03096f808820404c62dea12c7c59cdc74fdbd9020b0d71c8aba39b4a143bb'
>>> bridges.wallets.ethereum.get_receipt(transaction_hash=transaction_hash)
{
    "result": {
        "blockHash": "0xac9bec5ba838618a8abd6152eeda25cb4d47511a038d7ba9e17dded924d725ce",
        "blockNumber": "0x5df6e2",
        "contractAddress": null,
        "cumulativeGasUsed": "0x4c2740",
        "from": "0xb563dde324fa9842e74bbf98571e9de4fd5fe9ba",
        "gasUsed": "0x5208",
        "logs": [],
        "logsBloom": "0x000000000000000000000000000000000000000000000000000000000000000000
        0000000000000000000000000000000000000000000000000000000000000000000000000000000000
        0000000000000000000000000000000000000000000000000000000000000000000000000000000000
        0000000000000000000000000000000000000000000000000000000000000000000000000000000000
        0000000000000000000000000000000000000000000000000000000000000000000000000000000000
        0000000000000000000000000000000000000000000000000000000000000000000000000000000000
        000000000000000000000000000000000000",
        "status": "0x1",
        "to": "0x4aa548d7589f003486892777cbb0b70dff5d6949",
        "transactionHash": "0x73d53064c302af6ea1038273183e8da70b87f35cdd70e133b3e96225d3834c1c",
        "transactionIndex": "0x83"
    }
}
```

Get gas speed — `bridges.wallets.ethereum.get_gas_speed`

```python
>>> bridges.wallets.ethereum.get_gas_speed()
{
    "result": 100000000
}
```