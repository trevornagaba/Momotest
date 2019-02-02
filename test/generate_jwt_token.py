##
{"apiKey":"79c24602608a404b8c0810e06a761c57"}
{"apiUser":"6f1992b0-f2a4-4b78-b323-de60732fb369"}
##

import http.client, urllib, base64, json, uuid

api_key = "79c24602608a404b8c0810e06a761c57"
api_user = "6f1992b0-f2a4-4b78-b323-de60732fb369"
primary_key = '98bc5ef1ae864360b66024e1facadf51'
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
access_token = json.loads(data.decode())["access_token"]


# Request to pay


token = access_token
reference_id = str(uuid.uuid4())
headers = {
    # Request headers
    'Authorization': 'Bearer '+ token,
    # 'X-Callback-Url': "http://127.0.0.1:4040",
    'X-Reference-Id': reference_id,
    'X-Target-Environment': 'sandbox',
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': primary_key,
}
params = urllib.parse.urlencode({})
body = json.dumps({
  "amount": "5000",
  "currency": "EUR",
  "externalId": "12345",
  "payer": {
    "partyIdType": "MSISDN",
    "partyId": "0780123456"
  },
  "payerMessage": "test message",
  "payeeNote": "test note"
})
try:
    conn = http.client.HTTPSConnection('ericssonbasicapi2.azure-api.net')
    conn.request("POST", "/collection/v1_0/requesttopay?%s" % params, body, headers)
    response = conn.getresponse()
    print(response.status)
    print(response.reason)
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))