# from web3 import Web3

# w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/2885280182ee49d2a21e7ce953b542a4'))
# account = w3.eth.account.create()
# privateKey = account.privateKey.hex()
# address = account.address

# print(f'Your rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr adress: {address}\nYour keyL {privateKey}')


from web3 import Web3

# Connect to Ganache
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

# Create a new Ethereum account
account = w3.eth.account.create()

# Extract the address and private key
privateKey = account.privateKey.hex()
address = account.address

# Print the generated address and private key
print(f'Your address: {address}\nYour private key: {privateKey}')
