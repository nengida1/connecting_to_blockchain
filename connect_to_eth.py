import json
from web3 import Web3
from web3.middleware import ExtraDataToPOAMiddleware
from web3.providers.rpc import HTTPProvider

# Codio credentials folder (your course expects this path)
CRED_DIR = "/home/codio/workspace/student_credentials"

'''
If you use one of the suggested infrastructure providers, the url will be of the form
now_url  = f"https://eth.nownodes.io/{now_token}"
alchemy_url = f"https://eth-mainnet.alchemyapi.io/v2/{alchemy_token}"
infura_url = f"https://mainnet.infura.io/v3/{infura_token}"
'''

def connect_to_eth():
    # You can keep this hardcoded, or read from a file if your course requires it.
    url = "https://mainnet.infura.io/v3/b993aa46b0e249ef9c8687fb3a7d09d7"
    w3 = Web3(HTTPProvider(url))
    assert w3.is_connected(), f"Failed to connect to provider at {url}"
    return w3


def connect_with_middleware(contract_json):
    with open(contract_json, "r") as f:
        d = json.load(f)
        d = d["bsc"]
        address = d["address"]
        abi = d["abi"]

    # TODO complete this method
    # The first section will be the same as "connect_to_eth()" but with a BNB url

    # 1. Connect to BNB
    bnb_url = "https://data-seed-prebsc-1-s1.binance.org:8545/"
    w3 = Web3(HTTPProvider(bnb_url))
    w3.middleware_onion.inject(ExtraDataToPOAMiddleware, layer=0)

    # 2. Load contract (already loaded above, so no need to reopen file)
    checksum_addr = Web3.to_checksum_address(address)
    contract = w3.eth.contract(address=checksum_addr, abi=abi)

    return w3, contract

if __name__ == "__main__":
    connect_to_eth()
