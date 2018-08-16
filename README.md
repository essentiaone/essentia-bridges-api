# essentia-bridges-api

The API wrapper written in Python allow you to speak with Bridges REST API in pythonic way.

[![Release](https://img.shields.io/github/release/essentiaone/essentia-bridges-api.svg)](https://github.com/essentiaone/essentia-bridges-api/releases)
![Python36](https://img.shields.io/badge/Python-3.6-brightgreen.svg)


  * [Getting started](#getting-started)
  * [API documentation](#api)
    * [Wallets](#wallets)
      * [Bitcoin wallet](#bitcoin-wallet)
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

#### Bitcoin wallet

Get balance of the wallet — `bridges.wallets.bitcoin.get_balance`

| Arguments | Type   | Required | Description                  |
| :--------:|:------:|:--------:|------------------------------|
| address   | String | Yes      | Address to get balance from. |

```python
>>> address = '16DWEqF6pX314CjV5u2dmiMhcXtyY6z7od'
>>> bridges.wallets.bitcoin.get_balance(address=address)
{
    "result": {
        "balance": 0.0001487
    }
}
```

Get Unspent Transaction Outputs (UTXO) of the wallet — `bridges.wallets.bitcoin.get_utxo`

| Arguments | Type   | Required | Description               |
| :--------:|:------:|:--------:|---------------------------|
| address   | String | Yes      | Address to get UTXO from. |

```python
>>> address = '16DWEqF6pX314CjV5u2dmiMhcXtyY6z7od'
>>> bridges.wallets.bitcoin.get_utxo(address=address)
[
    {
        "address": "16DWEqF6pX314CjV5u2dmiMhcXtyY6z7od",
        "amount": 0.0001,
        "confirmations": 1069,
        "height": 535953,
        "satoshis": 10000,
        "scriptPubKey": "76a9143936070b1eded9950affc4444953c2bb1e5abce388ac",
        "txid": "114f959a873041e87095fc71472b42debdc6780d3ac33dea8e7d6830977643ce",
        "vout": 0
    },
    {
        "address": "16DWEqF6pX314CjV5u2dmiMhcXtyY6z7od",
        "amount": 4.87e-05,
        "confirmations": 1079,
        "height": 535943,
        "satoshis": 4870,
        "scriptPubKey": "76a9143936070b1eded9950affc4444953c2bb1e5abce388ac",
        "txid": "e5bd8354909df8fc31828ced8a9121f70afa7f507e330860a8d5d9f11bc47430",
        "vout": 1
    }
]
```

Send raw transaction hash to blockchain — `bridges.wallets.bitcoin.send_transaction`

| Arguments            | Type   | Required | Description                                        |
| :-------------------:|:------:|:--------:|----------------------------------------------------|
| raw_transaction_hash | String | Yes      | Signed raw transaction hash to send to blockchain. |

```python
>>> raw_transaction_hash = '0100000001c5d33f8bd2cf21b42fa1b1a2993a94cdd93abaa886fe1e265...'
>>> bridges.wallets.bitcoin.send_transaction(raw_transaction_hash=raw_transaction_hash)
{
    "txid": "fb20f41645dd057b365a67f4b1a0d900a26b6a93be5245e954b838aafa44ce9d"
}
```

Get transactions history of the wallet — `bridges.wallets.bitcoin.get_transactions_history`

| Arguments | Type   | Required | Description                               |
| :--------:|:------:|:--------:|-------------------------------------------|
| address   | String | Yes      | Address to get transactions history from. |

```python
>>> address = '16DWEqF6pX314CjV5u2dmiMhcXtyY6z7od'
>>> bridges.wallets.bitcoin.get_transactions_history(address=address)
{
    "from": 0,
    "items": [
        {
            "blockhash": "00000000000000000011d372aabbef58d8fa45f960c4dfdeada3615f6e689afa",
            "blockheight": 535953,
            "blocktime": 1533833303,
            "confirmations": 1069,
            "fees": 0.00029999,
            "locktime": 0,
            "size": 519,
            "time": 1533833303,
            "txid": "114f959a873041e87095fc71472b42debdc6780d3ac33dea8e7d6830977643ce",
            "valueIn": 0.00169,
            "valueOut": 0.00139001,
            "version": 1,
            "vin": [
                {
                    "addr": "1B5K2VtjsMyfiZ1JncgSznKGiKiZayYRPc",
                    "doubleSpentTxID": null,
                    "n": 0,
                    "scriptSig": {
                        "asm": "304402204e32cfb1db89f020a7adc155fbeba4f65c4af57ba8a11c70db0cb456a2f5
                        6770022045e34cd2f203bbd413c375572834fc60a5d1ab6023fc410a01c9526e1c235f74[ALL]
                        031abb8bbf4a0513d18be9830808647e985267e576b503456788c6d271adefebda",
                        "hex": "47304402204e32cfb1db89f020a7adc155fbeba4f65c4af57ba8a11c70db0cb456a2f
                        56770022045e34cd2f203bbd413c375572834fc60a5d1ab6023fc410a01c9526e1c235f740121
                        031abb8bbf4a0513d18be9830808647e985267e576b503456788c6d271adefebda"
                    },
                    "sequence": 4294967295,
                    "txid": "e5bd8354909df8fc31828ced8a9121f70afa7f507e330860a8d5d9f11bc47430",
                    "value": 0.0001,
                    "valueSat": 10000,
                    "vout": 0
                },
                {
                    "addr": "1B5K2VtjsMyfiZ1JncgSznKGiKiZayYRPc",
                    "doubleSpentTxID": null,
                    "n": 1,
                    "scriptSig": {
                        "asm": "304402201ecb1961fb8b7482540fc06eedacf6e4383a3efa7f171d997b722e452446
                        a3c40220504d8571cee62998937f60014ef7a125c1c3b3913984bab1c5fc694b4fc97023[ALL]
                        031abb8bbf4a0513d18be9830808647e985267e576b503456788c6d271adefebda",
                        "hex": "47304402201ecb1961fb8b7482540fc06eedacf6e4383a3efa7f171d997b722e45244
                        6a3c40220504d8571cee62998937f60014ef7a125c1c3b3913984bab1c5fc694b4fc970230121
                        031abb8bbf4a0513d18be9830808647e985267e576b503456788c6d271adefebda"
                    },
                    "sequence": 4294967295,
                    "txid": "2524bb0d9af29798b73ac2a0a92be80bc6e93aaffebfe070ea750a95b38093f2",
                    "value": 0.00149,
                    "valueSat": 149000,
                    "vout": 1
                },
                {
                    "addr": "1B5K2VtjsMyfiZ1JncgSznKGiKiZayYRPc",
                    "doubleSpentTxID": null,
                    "n": 2,
                    "scriptSig": {
                        "asm": "3044022040e766c0b2b9cab69f2aaa4c2c88d078489570cc8ade642f862ba79e7d05
                        c1d00220250b37e60345c109e5ded2191229c1726b53339fe2eaa4fa23f68fb4277ad34f[ALL]
                        031abb8bbf4a0513d18be9830808647e985267e576b503456788c6d271adefebda",
                        "hex": "473044022040e766c0b2b9cab69f2aaa4c2c88d078489570cc8ade642f862ba79e7d0
                        5c1d00220250b37e60345c109e5ded2191229c1726b53339fe2eaa4fa23f68fb4277ad34f0121
                        031abb8bbf4a0513d18be9830808647e985267e576b503456788c6d271adefebda"
                    },
                    "sequence": 4294967295,
                    "txid": "e2e6ff331a10ee80fd698e2d5aa3ef2c22999be5e13f93755b2c5aa0a7dcb200",
                    "value": 0.0001,
                    "valueSat": 10000,
                    "vout": 0
                }
            ],
            "vout": [
                {
                    "n": 0,
                    "scriptPubKey": {
                        "addresses": [
                            "16DWEqF6pX314CjV5u2dmiMhcXtyY6z7od"
                        ],
                        "asm": "OP_DUP OP_HASH160 3936070b1eded9950affc4444953c2bb1e5abce3 OP_EQUALVERIFY OP_CHECKSIG",
                        "hex": "76a9143936070b1eded9950affc4444953c2bb1e5abce388ac",
                        "type": "pubkeyhash"
                    },
                    "spentHeight": null,
                    "spentIndex": null,
                    "spentTxId": null,
                    "value": "0.00010000"
                },
                {
                    "n": 1,
                    "scriptPubKey": {
                        "addresses": [
                            "1B5K2VtjsMyfiZ1JncgSznKGiKiZayYRPc"
                        ],
                        "asm": "OP_DUP OP_HASH160 6e81f8092d4b5b5a20d7257d042b0b170b5056cc OP_EQUALVERIFY OP_CHECKSIG",
                        "hex": "76a9146e81f8092d4b5b5a20d7257d042b0b170b5056cc88ac",
                        "type": "pubkeyhash"
                    },
                    "spentHeight": 536575,
                    "spentIndex": 0,
                    "spentTxId": "fb91cec2bdfd2f390f171d649b04518480c7cdd0b6b7de9d4f8a615d7e7f0181",
                    "value": "0.00129001"
                }
            ]
        },
        ...
    ]
}
```

Get information of the particular transaction of the wallet — `bridges.wallets.bitcoin.get_transaction_information`

| Arguments        | Type   | Required | Description       |
| :---------------:|:------:|:--------:|-------------------|
| transaction_hash | String | Yes      | Transaction hash. |

```python
>>> transaction_hash = 'b7b707244f0b56a49ea9339b6a70c589f24bdacbb20d850f55e3bb855f386c87'
>>> bridges.wallets.bitcoin.get_transaction_information(transaction_hash=transaction_hash)
{
    "blockhash": "0000000000000000001a71f184d147b59a3ef170e094a9c2c435faffa6ce2262",
    "blockheight": 518607,
    "blocktime": 1523964387,
    "confirmations": 18417,
    "fees": 0.0005,
    "locktime": 0,
    "size": 225,
    "time": 1523964387,
    "txid": "b7b707244f0b56a49ea9339b6a70c589f24bdacbb20d850f55e3bb855f386c87",
    "valueIn": 0.00714,
    "valueOut": 0.00664,
    "version": 1,
    "vin": [
        {
            "addr": "1MoRmwmoA1cFSuePCGJV6UWLTmcxaBBKfW",
            "doubleSpentTxID": null,
            "n": 0,
            "scriptSig": {
                "asm": "3044022035500343804d3c08dbbe8a6168865c044a53da5ba06158e4a013b03481d6f
                f2502207a73e65e4c9f0402861b69f9387a64bebb2cf8c0ecb5038603588290f273289e[ALL]
                0388c1c8e2bd42c9e40888f2373d69b0627925da9da8246765857a8f1283d32ddd",
                "hex": "473044022035500343804d3c08dbbe8a6168865c044a53da5ba06158e4a013b03481d
                6ff2502207a73e65e4c9f0402861b69f9387a64bebb2cf8c0ecb5038603588290f273289e0121
                0388c1c8e2bd42c9e40888f2373d69b0627925da9da8246765857a8f1283d32ddd"
            },
            "sequence": 4294967295,
            "txid": "e54c10f1749ba2cc73e8f4cd07e64565846e3ebe90032e5bbd1870f1cfb3a8a8",
            "value": 0.00714,
            "valueSat": 714000,
            "vout": 1
        }
    ],
    "vout": [
        {
            "n": 0,
            "scriptPubKey": {
                "addresses": [
                    "1PGEjYqbk8CzmsFdRXQSwfAtZ7ieRWaAtA"
                ],
                "asm": "OP_DUP OP_HASH160 f434788d260a2d5665008e9912b76afa64d4c9cd OP_EQUALVERIFY OP_CHECKSIG",
                "hex": "76a914f434788d260a2d5665008e9912b76afa64d4c9cd88ac",
                "type": "pubkeyhash"
            },
            "spentHeight": null,
            "spentIndex": null,
            "spentTxId": null,
            "value": "0.00010000"
        },
        {
            "n": 1,
            "scriptPubKey": {
                "addresses": [
                    "1MoRmwmoA1cFSuePCGJV6UWLTmcxaBBKfW"
                ],
                "asm": "OP_DUP OP_HASH160 e42a54ba2042e889461c7966ac6ba13eeb144a3f OP_EQUALVERIFY OP_CHECKSIG",
                "hex": "76a914e42a54ba2042e889461c7966ac6ba13eeb144a3f88ac",
                "type": "pubkeyhash"
            },
            "spentHeight": 525948,
            "spentIndex": 1,
            "spentTxId": "f3bc1022a05b6687b55d92361457ae7ee2299238a09aa99572e615cf9682ed9c",
            "value": "0.00654000"
        }
    ]
}
```

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
