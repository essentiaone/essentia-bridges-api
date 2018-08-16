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

#### Litecoin wallet

Get balance of the wallet — `bridges.wallets.litecoin.get_balance`

| Arguments | Type   | Required | Description                  |
| :--------:|:------:|:--------:|------------------------------|
| address   | String | Yes      | Address to get balance from. |

```python
>>> address = 'LTNJvXUJeRi41DJuEg5V3zWRhUisC3KUtF'
>>> bridges.wallets.litecoin.get_balance(address=address)
{
    "result": {
        "balance": 0.00099999
    }
}
```

Get information of the particular transaction of the wallet — `bridges.wallets.ethereum.get_transaction_information`

| Arguments        | Type   | Required | Description       |
| :---------------:|:------:|:--------:|-------------------|
| transaction_hash | String | Yes      | Transaction hash. |

```python
>>> transaction_hash = '5d61a2bd067081fe792e703baf28cbb8bbee137e043909d0fd5a7ccddff87ce4'
>>> bridges.wallets.litecoin.get_transaction_information(transaction_hash=transaction_hash)
{
    "blockhash": "730919fe24ee4a5daa27c0690ab1b197914b4f7e5a6c90b35ce74041a5930dbb",
    "blockheight": 1474586,
    "blocktime": 1534343622,
    "confirmations": 2,
    "fees": 0.01061571,
    "locktime": 0,
    "size": 226,
    "time": 1534343622,
    "txid": "5d61a2bd067081fe792e703baf28cbb8bbee137e043909d0fd5a7ccddff87ce4",
    "valueIn": 9.59987334,
    "valueOut": 9.58925763,
    "version": 1,
    "vin": [
        {
            "addr": "LTRJDsRDhxu1FD3qdNDr5oPK1qGHBuLTZW",
            "doubleSpentTxID": null,
            "n": 0,
            "scriptSig": {
                "asm": "3045022100a2c0147eeda8478a2468eb9f4ffa58418ad787da59c1c2bbdfb980a0b1fc3a1e02201c6b88424ccf589d2eeea94177744062a27541002bd4dfdbf891f948bcfd9ac5[ALL] 03ae0081f0b150b23c35ea80609064903db39c758cf504f4c7b6add6a64ca9836a",
                "hex": "483045022100a2c0147eeda8478a2468eb9f4ffa58418ad787da59c1c2bbdfb980a0b1fc3a1e02201c6b88424ccf589d2eeea94177744062a27541002bd4dfdbf891f948bcfd9ac5012103ae0081f0b150b23c35ea80609064903db39c758cf504f4c7b6add6a64ca9836a"
            },
            "sequence": 4294967295,
            "txid": "e1018d12bdceaf90b6bcc7091e1ed71fbf72839db4a9fb06987ce1877c94bf7d",
            "value": 9.59987334,
            "valueSat": 959987334,
            "vout": 0
        }
    ],
    "vout": [
        {
            "n": 0,
            "scriptPubKey": {
                "addresses": [
                    "Ld8PiAcP88mrCjzpbPwZwRxk8ae492J8x4"
                ],
                "asm": "OP_DUP OP_HASH160 c46502c5059c3971516a25195ae08e9128fe1dd8 OP_EQUALVERIFY OP_CHECKSIG",
                "hex": "76a914c46502c5059c3971516a25195ae08e9128fe1dd888ac",
                "type": "pubkeyhash"
            },
            "spentHeight": null,
            "spentIndex": null,
            "spentTxId": null,
            "value": "4.07153000"
        },
        {
            "n": 1,
            "scriptPubKey": {
                "addresses": [
                    "LSvLY6WcMPHvvLaW6A2n7BwA3zAkWrHWbJ"
                ],
                "asm": "OP_DUP OP_HASH160 546c1cbac0c236944ba46ff9827ddc1a748e76a8 OP_EQUALVERIFY OP_CHECKSIG",
                "hex": "76a914546c1cbac0c236944ba46ff9827ddc1a748e76a888ac",
                "type": "pubkeyhash"
            },
            "spentHeight": null,
            "spentIndex": null,
            "spentTxId": null,
            "value": "5.51772763"
        }
    ]
}
```
