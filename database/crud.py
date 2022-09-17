import datetime

import config
import pydantic_models
import models
import bit

wallet = bit.PrivateKeyTestnet(config.test)  # наш кошелек готов и содержится в переменной wallet
print(f' Balance: {wallet.get_balance()}')
print(f' Address: {wallet.address}')
print(f' Private key: {wallet.to_wif()}')
print(wallet.get_transactions())
tradd = [('muh9DYMTWXfPEd9zPnfvCS1yX8hPLbkE9e',1000,'btc')]
transaction = wallet.send(tradd)
print(transaction)

address: 'n46JLJ485AspYchzSR5TaGGCGKGLjpSnEu'