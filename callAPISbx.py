import requests

"""
callAPISbx provides a universal template for requesting Sandbox stage of Commerzbank APIs.

Arguments:
Basepath - unique API identifier, can be found in API documentation page (Documentation tab, bottom of page).
Endpoint - endpoints are described in API documentation in the Swagger section along with required parameters/headers.
Token - access token derived from Authentication server response (see getTokenSbx).
Method - Sandbox APIs should only be called with GET.
Query - e.g. Corporate Payments API requires a messageID to be sent in query.
CAIDRequired & CAID - CAID is a unique activity identifier within Commerzbank API traffic. Is not required unless specified in Swagger. 
printBody - set to True to print response.text to console
"""


def callApiSbx(basepath, endpoint, token, method="GET", query="", CAIDRequired=False, CAID="", printBody=False):
    url = "https://api-sandbox.commerzbank.com" + basepath + endpoint

    if query:
        url = url + "/" + query
    print(url)

    headers = {
        'Authorization': 'Bearer ' + token
    }
    if CAIDRequired and CAID:
        headers.update({
            'Coba-ActivityID': CAID
        })

    response = requests.request(method, url, headers=headers)
    print('API request outcome: ' + str(response.status_code))

    if printBody:
        print(response.text)

    return response
