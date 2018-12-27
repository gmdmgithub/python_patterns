import json
from urllib.request import urlopen

with urlopen("https://free.currencyconverterapi.com/api/v6/currencies") as response:
    source = response.read()

print('SOURCE TYPE',type(source))
data = json.loads(source) # loads read to string - convert
print('DATA TYPE', type(data))
#print(json.dumps(data, indent=2)) # dump and dumps - outputs to string (JSON)


for item in data['results']:
    # print(item)
    name = data['results'][item]['currencyName']
    symbol = 'NOT EXISTS'
    if 'currencySymbol' in data['results'][item]:
        symbol = data['results'][item]['currencySymbol']
    id = data['results'][item]['id']
    print(name, symbol, id)


#### second - better with exhange historical data
print('\n#### exchangeratesapi ###')
# https://api.exchangeratesapi.io/2010-01-12
# https://api.exchangeratesapi.io/latest?base=USD

# similar to open (file)
#with open('exhange.json',encoding='utf-8') as response:
with urlopen("https://api.exchangeratesapi.io/latest") as response:
    source = response.read()

data = json.loads(source)  # loads from a string
print(json.dumps(data, indent=2))  # dump and dumps - outputs to string (JSON)

with open('exhange.json','w',encoding='utf-8') as f:
    f.write(json.dumps(data))

print('\n#### PRINTING exchangeratesapi ###')
print(data['base'], data['date'])
for item in data['rates']:
    print(item, data['rates'][item])

print('#### JSON ###')
print(dir(json))