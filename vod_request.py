import json
import sys 
from urllib.request import urlopen
import urllib.parse
import os, ssl


# with open('./test_cashloan.json') as f:
#     data = json.loads(f.read())

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)): 
    ssl._create_default_https_context = ssl._create_unverified_context



# with open('./test ovd.json') as f:
#      data = json.loads(f.read())
url = 'url'
header = {'Api-Key' : 'secret'}

req = urllib.request.Request(url, headers = header)
with urllib.request.urlopen(req) as response:
    data = response.read()
    data =json.loads(decode('utf-8'))



credit_amount = int(input('Cash Loan amount = '))

tenor = int(input('Tenor = '))

apr = 1000
provider = ''

# for element in data:
# print(data, dir(data))
for el in data['products']:
    if el['isActive'] == True:  # szukam tylko elementów aktywnych
       #  print(el['isActive'])
        for val in el['interests']:
            if val['loanAmountMin'] <= credit_amount \
                    and credit_amount <= val['loanAmountMax'] \
                    and val['loanTenureMin'] <= tenor \
                    and tenor <= val['loanTenureMax'] \
                    and val['apr'] <= apr:

                apr = val['apr']
                provider = el['providerId']

if apr == 1000:
    print()
    print('Cannot find market offer for given parameters!')
    print()
else:
    print()
    print('Best market offer is from ', provider, ': APR =', apr, '%.')
    print()
    # print(el['interests'][0]['apr'])