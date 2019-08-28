import jwt

# go to  check https://jwt.io/
my_secret = "my secret text"
my_bad_secret = "not correct secret"
sample_payload = {"my_name":"Alex"} # in python json is a dictionary
encoded_jwt = jwt.encode(sample_payload, my_secret)
print(f"my encoded JWT is {encoded_jwt}")


#let's decode
try:
    # payload = jwt.decode(encoded_jwt, my_bad_secret)
    payload = jwt.decode(encoded_jwt, my_secret)
    print(payload)
except Exception as e: #any
    print(f"The problem with JWT token: {e}")
    