##
{"apiKey":"79c24602608a404b8c0810e06a761c57"}
{"apiUser":"6f1992b0-f2a4-4b78-b323-de60732fb369"}
##

import httplib, urllib, base64
api_user = "79c24602608a404b8c0810e06a761c57"
api_key = "6f1992b0-f2a4-4b78-b323-de60732fb369"
api_user_and_key  = api_user+':'+api_key
encoded = base64.b64encode(api_user_and_key)
headers = {
    # Request headers
    'Authorization': 'Basic '+encoded,
    'Ocp-Apim-Subscription-Key': '98bc5ef1ae864360b66024e1facadf51',
}
params = urllib.urlencode({
})
try:
    conn = httplib.HTTPSConnection('ericssonbasicapi2.azure-api.net')
    conn.request("POST", "/collection/token/?%s" % params, "{body}", headers)
    response = conn.getresponse()
    print(response.status)
    print(response.reason)
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))