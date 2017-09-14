# This is written for PYTHON 3
# Don't forget to install requests package

import requests
import json

def getAtm(lat,lng,rad,apiKey):
	url = 'http://api.reimaginebanking.com/atms?lat={}&lng={}&rad={}&key={}'.format(lat,lng,rad,apiKey)
	response = requests.get(url,headers={'content-type':'application/json'})
	if response.status_code == 200:
		print('atms retrieved')
	else:
		print(response.status_code)

	data = json.loads(response.content)
	dataLength = len(data['data'])
	if dataLength > 0:
		money = data['data'][0]['amount_left']	

	return money

customerId = '599dc3bca73e4942cdafdb22'
apiKey = '95c2b61f4082919257c091e7429b2047'

url = 'http://api.reimaginebanking.com/customers?key={}'.format(apiKey)
payload = {
  "first_name": "jane",
  "last_name": "doe",
  "address": {
    "street_number": "123",
    "street_name": "hollywood blvd",
    "city": "reston",
    "state": "VA",
    "zip": "20194"
  }
}
# Create new customer
response = requests.post( 
	url, 
	data=json.dumps(payload),
	headers={'content-type':'application/json'},
	)

if response.status_code == 201:
	print('new customer added')
mymoney = getAtm(38.9283,-77.1753,1,apiKey)
print(mymoney)

# create new savings account
url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customerId,apiKey)
payload = {
  "type": "Savings",
  "nickname": "test",
  "rewards": 10000,
  "balance": 10000,	
}
# Create a Savings Account
response = requests.post( 
	url, 
	data=json.dumps(payload),
	headers={'content-type':'application/json'},
	)

if response.status_code == 201:
	print('account created')

# Post account billing
account_id = '59b99366ceb8abe24251ba54'
url = 'http://api.reimaginebanking.com/accounts/{}/bills?key={}'.format(account_id,apiKey)
payload = {
  "status": "pending",
  "payee": "capitalone",
  "nickname": "c1",
  "payment_date": "2017-09-14",
  "recurring_date": 1,
  "payment_amount": 1209000	
}
# posts a bill
response = requests.post( 
	url, 
	data=json.dumps(payload),
	headers={'content-type':'application/json'},
	)

if response.status_code == 201:
	print('bill posted')

# get purchases of account
acct_purchases = '59b98b77ceb8abe24251ba4b'
url = 'http://api.reimaginebanking.com/accounts/{}/purchases?key={}'.format(acct_purchases,apiKey)
# checks purchases
response = requests.get( 
	url,
	headers={'content-type':'application/json'},
	)

if response.status_code == 200:
	print('purchase check successful')

#check atm 
getAtm(38.9283,-77.1753,1,apiKey)

#create deposit
url = 'http://api.reimaginebanking.com/accounts/{}/deposits?key={}'.format(account_id,apiKey)
payload = {
  "medium": "balance",
  "transaction_date": "2017-09-14",
  "amount": 0.01,
  "description": "string"
}
# posts a deposit
response = requests.post( 
	url, 
	data=json.dumps(payload),
	headers={'content-type':'application/json'},
	)

if response.status_code == 201:
	print('deposit posted')

#enterprise account check
url = 'http://api.reimaginebanking.com/enterprise/accounts/{}?key={}'.format(account_id,apiKey)

# checks account
response = requests.get( 
	url, 
	headers={'content-type':'application/json'}
	)

if response.status_code == 200:
	print('account checked in enterprise system')

#delete purchases
url = 'http://api.reimaginebanking.com/data?type=Purchases&key={}'.format(apiKey)

response = requests.delete( 
	url, 
	headers={'content-type':'application/json'}
	)

if response.status_code == 204:
	print('purchases deleted')


