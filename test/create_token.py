import http.client, urllib, base64, uuid, json, requests

primary_key = '98bc5ef1ae864360b66024e1facadf51'

## Create reference_id

reference_id = str(uuid.uuid4())
print(reference_id)

## Create api user

headers = {
    # Request headers
    'X-Reference-Id': reference_id,
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': primary_key,
}
params = urllib.parse.urlencode({})
body = json.dumps({
  "providerCallbackHost": "http://127.0.0.1:4040" })
try:
    conn = http.client.HTTPSConnection('ericssonbasicapi2.azure-api.net')
    conn.request("POST", "/v1_0/apiuser?%s" % params, body, headers)
    response = conn.getresponse()
    print(response.status)
    print(response.reason)
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
api_user = reference_id


## Get user details

headers = {
    # Request headers
    'X-Reference-Id': reference_id,
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': primary_key
}
params = urllib.parse.urlencode({
})

body = json.dumps({
  "providerCallbackHost": "http://127.0.0.1:4040" })

# body = json.dumps(  
#     {
#         "amount": "string",
#         "currency": "string",
#         "externalId": "string",
#         "payer": {
#             "partyIdType": "MSISDN",
#             "partyId": "string"
#         },
#         "payerMessage": "string",
#         "payeeNote": "string"
#     }
# )

try:
    conn = http.client.HTTPSConnection('ericssonbasicapi2.azure-api.net')
    conn.request("POST", "/v1_0/apiuser/ed4fc92e-1b00-485a-b840-9fe55681d5d0?%s" % params, body, headers)
    response = conn.getresponse()
    print(response.status)
    print(response.reason)
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))


## Create api token

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': primary_key
}
params = urllib.parse.urlencode({
})
body = json.dumps({
  "providerCallbackHost": "http://127.0.0.1:4040" })
try:
    conn = http.client.HTTPSConnection('ericssonbasicapi2.azure-api.net')
    conn.request("POST", "/v1_0/apiuser/ed4fc92e-1b00-485a-b840-9fe55681d5d0/apikey?%s" % params, body, headers)
    response = conn.getresponse()
    print(response.status)
    print(response.reason)
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
api_key = json.loads(data.decode('utf8'))["apiKey"]





## Create jwt token

print(api_user)
print(api_key)

# params = urllib.parse.urlencode({
# })
# r = requests.post('https://ericssonbasicapi2.azure-api.net/collection/token/?%s' % params , auth=(api_user, api_key), headers = { 'Ocp-Apim-Subscription-Key' : primary_key } )
# print(r.content)


api_user_and_key  = api_user+':'+api_key
encoded = base64.b64encode(api_user_and_key.encode())
headers = {
    # Request headers
    'Authorization': 'Basic '+encoded.decode(),
    'Ocp-Apim-Subscription-Key': primary_key,
}
params = urllib.parse.urlencode({
})
body = json.dumps({
  "providerCallbackHost": "http://127.0.0.1:4040" })
try:
    conn = http.client.HTTPSConnection('ericssonbasicapi2.azure-api.net')
    conn.request("POST", "/collection/token/?%s" % params, "{body}", headers)
    response = conn.getresponse()
    print(response.status)
    print(response.reason)
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))