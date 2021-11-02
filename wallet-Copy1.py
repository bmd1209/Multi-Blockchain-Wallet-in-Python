import subprocess 
import json
import os
from dotenv import load_dotenv
from constants import *
from bit import Key, PrivateKey, PrivateKeyTestnet
from bit.network import NetworkAPI
from bit import *
from web3 import Web3
from eth_account import Account


w3 = Web3(Web3.HTTPProvider("http://127.0.0.1.8545"))


load_dotenv


mnemonic = os.getenv('MNEMONIC', "win brave festival become force snack year around garbage rely void arch")
print(mnemonic)

def derive_wallets(mnemonic, coin, numderive):
 
    command = f'php derive -g --mnemonic="{mnemonic}" --coin="{coin}" --format=json' 
    
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
   
    keys = json.loads(output)
    return  keys




coins = {"eth", "btc-test", "btc"}
numderive = 3

keys = {}
for coin in coins:
    keys[coin]= derive_wallets(os.getenv('mnemonic'), coin, numderive=3)
    

eth_PrivateKey = keys["eth"][0]['privkey']
btc_PrivateKey = keys['btc-test'][0]['privkey']

print(json.dumps(eth_PrivateKey, indent=2, sort_keys=True))
print(json.dumps(btc_PrivateKey, indent=2, sort_keys=True))
print(json.dumps(keys, indent=2, sort_keys=True))


def priv_key_to_account(coin, priv_key):

    if coin == ETH:
        return Account.privateKeyToAccount(priv_key)
    if coin == BTCTEST:
        return PrivateKeyTestnet(priv_key)
    
eth_acc = priv_key_to_account(ETH,eth_PrivateKey)
btc_acc = priv_key_to_account(BTCTEST,btc_PrivateKey)

def create_trx(coin, account, recipient, amount):
    global trx_data
    if coin ==ETH:
        gasEstimate = w3.eth.estimateGas(
            {"from": account.address, "to": recipient, "value": amount}
        )
        trx_data = {
            "to": recipient,
            "from": account.address,
            "value": amount,
            "gasPrice": w3.eth.gasPrice,
            "gas": gasEstimate,
            "nonce": w3.eth.getTransactionCount(account.address)
        }
        return trx_data

    if coin == BTCTEST:
        return PrivateKeyTestnet.prepare_transaction(account.address, [(recipient, amount, BTC)]) 
    
def send_trx(coin, account, recipient, amount):
    
    if coin == "eth": 
        trx_eth = create_trx(coin,account, recipient, amount)
        sign = account.signTransaction(trx_eth)
        result = w3.eth.sendRawTransaction(sign.rawTransaction)
        print(result.hex())
        return result.hex()
    else:
        trx_btctest= create_trx(coin,account,recipient,amount)
        sign_trx_btctest = account.sign_transaction(trx_btctest)
        from bit.network import NetworkAPI
        NetworkAPI.broadcast_tx_testnet(sign_trx_btctest)       
        return sign_trx_btctest