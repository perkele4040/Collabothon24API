import json
import requests

"""
getTokenSbx provides an example of retrieving an access token from Sandbox authentication server 
using the client_credentials grant type (OAuth 2).
Function returns the access token - first field of the response from authentication server. 

Arguments:
cc - object of class ClientCredentials holding a client_id and client_secret.
"""

def getTokenSbxClientCredentials(cc):
    url = "https://api-sandbox.commerzbank.com/auth/realms/sandbox/protocol/openid-connect/token"

    payload = ("grant_type=client_credentials&client_id=" + cc.getClientId() + "&client_secret=" + cc.getClientSecret())

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print('token request outcome: ' + str(response.status_code))

    token = json.loads(response.text)['access_token']
    return token
