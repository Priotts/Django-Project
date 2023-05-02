from web3 import Web3
import json
import hashlib

def SendTransaction(message):
    #Get web3 instance with Infura
    w3 = Web3(Web3.HTTPProvider('')) #your infura url (goerli testnet)
    #Set the address and private key of the sender
    address = ''     #your address
    privateKey = ''  #your private Key
    #Get nonce and gas price
    nonce = w3.eth.get_transaction_count(address)
    gasPrice = w3.eth.gasPrice 
    #Convert value to wei
    value = w3.toWei(0, 'ether')
    #Sign transaction
    signedTx = w3.eth.account.sign_transaction(dict(
        nonce = nonce,
        gasPrice = gasPrice,
        gas = 100000,
        to = '0x0000000000000000000000000000000000000000',
        value = value,
        data = message.encode('utf-8')
    ), privateKey)
    #Send transaction
    tx= w3.eth.send_raw_transaction(signedTx.rawTransaction)
    txId = w3.toHex(tx)
    return txId