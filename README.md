# polygonscan-python

<p align="center">
  <a href="https://github.com/tarsil/polygonscan-python" alt="build">
        <img src="https://github.com/tarsil/polygonscan-python/workflows/build/badge.svg" /></a>
</p>

<p align="center">
  <a href="https://badge.fury.io/py/polygonscan-python" alt="pypi">
        <img src="https://badge.fury.io/py/polygonscan-python.svg" /></a>
  
  <a href="" alt="license">
        <img src="https://img.shields.io/github/license/tarsil/polygonscan-python" /></a>
  
  <a href="https://www.python.org/downloads/release/python-385/" alt="python-version">
        <img src="https://img.shields.io/badge/python-3.8-blue.svg" /></a>
</p>

<p align="center">
  A complete Python API for <a href="https://polygonscan.com/">PolygonScan.com</a>
</p>

<p align="center">
  Powered by <a href="https://polygonscan.com/apis">PolygonScan.com APIs</a>
</p>

<p align="center">
  Available on <a href="https://pypi.org/project/polygonscan-python/">PyPI</a> 
</p>


<p align="center">
  <i>A fork of the <a href="https://github.com/pcko1/bscscan-python">bscscan-python</a> package.</i>
</p>

A minimal, yet complete, Python API for [polygonscan.com](https://polygonscan.com/).

This package was cloned from [bscscan-python](https://github.com/pcko1/bscscan-python) and
readapted to polygon network. A special thanks to the [creator](https://github.com/pcko1).
Without his hardwork this would be possible.

Available on [PyPI](https://pypi.org/project/polygonscan-python/). Powered by [polygonscan.com APIs](https://polygonscan.com/apis#misc).

___

## Endpoints

The following endpoints are provided:

<details><summary>Accounts <a href="https://polygonscan.com/apis#accounts">(source)</a></summary>
<p>

* `get_matic_balance`
* `get_matic_balance_multiple`
* `get_normal_txs_by_address`
* `get_normal_txs_by_address_paginated`
* `get_internal_txs_by_address`
* `get_internal_txs_by_address_paginated`
* `get_internal_txs_by_txhash`
* `get_internal_txs_by_block_range_paginated`
* `get_erc20_token_transfer_events_by_address`
* `get_erc20_token_transfer_events_by_contract_address_paginated`
* `get_erc20_token_transfer_events_by_address_and_contract_paginated`
* `get_erc721_token_transfer_events_by_address`
* `get_erc721_token_transfer_events_by_contract_address_paginated`
* `get_erc721_token_transfer_events_by_address_and_contract_paginated`
* `get_mined_blocks_by_address`
* `get_mined_blocks_by_address_paginated`

</details>

<details><summary>Contracts <a href="https://polygonscan.com/apis#contracts">(source)</a></summary>
<p>
  
* `get_contract_abi`
* `get_contract_source_code`

</details>

</details>

<details><summary>Transactions <a href="https://polygonscan.com/apis#transactions">(source)</a></summary>
<p>
  
* `get_contract_execution_status`
* `get_tx_receipt_status`

</details>

<details><summary>Blocks <a href="https://polygonscan.com/apis#blocks">(source)</a></summary>
<p>
  
* `get_block_reward_by_block_number`
* `get_est_block_countdown_time_by_block_number`
* `get_block_number_by_timestamp`

</details>

<details><summary>GETH/Parity Proxy <a href="https://polygonscan.com/apis#proxy">(source)</a></summary>
<p>

* `get_proxy_block_number`
* `get_proxy_block_by_number`
* `get_proxy_uncle_by_block_number_and_index`
* `get_proxy_block_transaction_count_by_number`
* `get_proxy_transaction_by_hash`
* `get_proxy_transaction_by_block_number_and_index`
* `get_proxy_transaction_count`
* `get_proxy_transaction_receipt`
* `get_proxy_call`
* `get_proxy_code_at`
* `get_proxy_storage_position_at`
* `get_proxy_gas_price`
* `get_proxy_est_gas`

</details>

<details><summary>Tokens <a href="https://polygonscan.com/apis#tokens">(source)</a></summary>
<p>
  
* `get_total_supply_by_contract_address`
* `get_acc_balance_by_token_and_contract_address`

</details>

<details><summary>Gas Tracker <a href="https://polygonscan.com/apis#gastracker">(source)</a></summary>
<p>
  
* `get_est_confirmation_time`
* `get_gas_oracle`

</details>

<details><summary>Stats <a href="https://polygonscan.com/apis#stats">(source)</a></summary>
<p>
  
* `get_total_matic_supply`
* `get_matic_last_price`

</details>

*If you think that a newly-added method is missing, kindly open an [issue](https://github.com/tarsil/polygonscan-python/issues) as a feature request and I will do my best to add it.*

## Installation

Before proceeding, you should register an account on [polygonscan.com](https://polygonscan.com/)
and [generate a personal API key](https://polygonscan.com/myapikey) to use.

If you wish to have access to the PRO endpoints, you should obtain elevated privileges via PolygonScans's
subscription service.

Install from source:

``` bash
pip install git+https://github.com/tarsil/polygonscan-python
```

Alternatively, install from [PyPI](https://pypi.org/project/polygonscan-python/):

```bash
pip install polygonscan-python
```

## Unit tests

In `bash`, test that everything looks OK on your end using your `YOUR_API_KEY` (without quotation marks)
before proceeding:

``` bash
bash run_tests.sh YOUR_API_KEY
````

This will regenerate the logs under `logs/` with the most recent results and the timestamp of the execution.

## Usage

In `python`, create a client with your personal [polygonscan.com](https://polygonscan.com/) API key:

``` python
from polygonscan import PolygonScan
matic = PolygonScan(YOUR_API_KEY) # key in quotation marks
```

Then you can call all available methods, e.g.:

``` python
matic.get_matic_balance(address="0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a")

> '40891631566070000000000'
```
You can also choose one of the other testnets:
``` python
matic = PolygonScan(YOUR_API_KEY, net="ropsten") # net name is case-insensitive, default is main
```

## Examples

Examples (arguments and results) for all methods may be found as JSON files
[here](https://github.com/tarsil/polygonscan-python/tree/master/logs).
For example, if you want to use the method `get_block_number_by_timestamp`,
you can find the supported arguments and the format of its output in its respective 
[JSON file](logs/standard/get_block_number_by_timestamp.json):

``` json
{
  "method": "get_block_number_by_timestamp",
  "module": "blocks",
  "kwargs": {
    "timestamp": "1578638524",
    "closest": "before"
  },
  "log_timestamp": "2020-10-28-12:34:44",
  "res": "9251482"
}
```

where `kwargs` refer to the required named arguments and `res` refers to the expected result if you were to run:

``` python
eth.get_block_number_by_timestamp(timestamp="1578638524", closest="before")

> '9251482'
```

**Disclaimer**: Those examples blindly use the arguments originally showcased
[here](https://api.polygonscan.com/apis) and the selected wallets/contracts
do not reflect any personal preference. You should refer to the same source for additional
information regarding specific argument values.

## Issues

For problems regarding installing or using the package please open an
[issue](https://github.com/tarsil/polygonscan-python/issues).
Kindly avoid disclosing potentially sensitive information such as your API keys or your wallet addresses.

Feel free to leave a :star: if you found this package useful.

___

 Powered by [polygonscan.com APIs](https://polygonscan.com/apis).
