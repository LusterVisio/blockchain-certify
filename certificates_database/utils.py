from web3 import Web3
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


# connect to an alchemy node
def sendTransaction(message):
    # alchemy_url = 'https://eth-mainnet.g.alchemy.com/v2/DJrvCiH29G7bI1MInozXNW7Wkolr3ARE'#os.environ["WEB3_ALCHEMY_PROJECT"]
    ganeche_url ="http://127.0.0.1:7545"
    w3 = Web3(Web3.HTTPProvider(ganeche_url))
    address = "0x91D7Ee01e8A4151C043CBBeFaF20820F42004970"
    privateKey = '0x92b95cd258021c3167ef65b0f6798b8f61b05810ff073fd37b78d2789a54cac4'
    nonce = w3.eth.getTransactionCount(address)
    gasPrice = w3.eth.gasPrice
    value = w3.toWei(0, "ether")
    signedTx = w3.eth.account.signTransaction(
        dict(
            nonce=nonce,
            gasPrice=gasPrice,
            gas=2000000,
            to="0x4B79Fe467Ef3CE2171068A9eF3c7b820AC5cACfa",
            value=value,
            data=message.encode("utf-8"),
        ),
        privateKey,
    )

    tx = w3.eth.sendRawTransaction(signedTx.rawTransaction)
    txId = w3.toHex(tx)
    return txId
   