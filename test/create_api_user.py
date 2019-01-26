import uuid
reference_id = str(uuid.uuid4())
print(reference_id)

import httplib, urllib, base64, uuid,json
headers = {
    # Request headers
    'X-Reference-Id': reference_id,
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '98bc5ef1ae864360b66024e1facadf51',
}
params = urllib.urlencode({})
body = json.dumps({
  "providerCallbackHost": "http://127.0.0.1:4040" })
try:
    conn = httplib.HTTPSConnection('ericssonbasicapi2.azure-api.net')
    conn.request("POST", "/v1_0/apiuser?%s" % params, body, headers)
    response = conn.getresponse()
    print(response.status)
    print(response.reason)
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))