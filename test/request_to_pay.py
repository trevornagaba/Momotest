########### Python 2.7 #############
import httplib, urllib, base64, uuid,json
token = ""
reference_id = str(uuid.uuid4())
headers = {
    # Request headersi
#    'Authorization': 'Bearer '+token,
    'X-Callback-Url': "http://127.0.0.1:4040",
    'X-Reference-Id': reference_id,
    'X-Target-Environment': 'sandbox',
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '98bc5ef1ae864360b66024e1facadf51',
}
params = urllib.urlencode({})
body = json.dumps({
  "amount": "5000",
  "currency": "UGX",
  "externalId": "12345",
  "payer": {
    "partyIdType": "MSISDN",
    "partyId": "0780123456"
  },
  "payerMessage": "test message",
  "payeeNote": "test note"
})
try:
    conn = httplib.HTTPSConnection('ericssonbasicapi2.azure-api.net')
    conn.request("POST", "/collection/v1_0/requesttopay?%s" % params, body, headers)
    response = conn.getresponse()
    print(response.status)
    print(response.reason)
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
####################################