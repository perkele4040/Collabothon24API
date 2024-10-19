import json
from getTokenSbx import getTokenSbxClientCredentials
from ClientCredentials import ClientCredentials
from callAPISbx import callApiSbx

"""
Run this file to execute a set of exemplary Sandbox API requests, preceded with a token request.
The following Client Credentials are not active and need to be replaced.
Client Credentials can be obtained by:
- Registering on developer.commerzbank.com.
- Creating a Sandbox project including all required APIs.
- Generating a set of Client Credentials in the last section of API project overview.

Popular error codes and reasons:
400 - a required header/parameter is missing.
401 - access token has run out or Client Credentials are invalid.
403 - the requested API first needs to be added to the API project.
404 - a non-existing endpoint was called or requested object was not found.
"""

cc = ClientCredentials("53234da7-8504-42a7-8272-81e6293e31ba", "9daad530-94d2-4046-b55b-37f39da1ee29")

token = getTokenSbxClientCredentials(cc)
print(token + "\n")

#**************ACCOUNTS FOREIGN UNITS*******************

basepath = "/accounts-api/21/v1"

#GET /info
callApiSbx(basepath, "/info", token)

#GET /accounts/accountID
response = callApiSbx(basepath, "/accounts", token, query="130471100000EUR")


#**************CORPORATE PAYMENTS*******************

basepath = "/corporate-payments-api/1/v1/bulk-payments"

#GET /heartbeat
callApiSbx(basepath, "/heartbeat", token)

#GET /messages
callApiSbx(basepath, "/messages", token)


#**************CUSTOMERS*******************

basepath = "/customers-api/v2"

#GET /heartbeat
callApiSbx(basepath, "/healthcheck", token)

#GET /messages
callApiSbx(basepath, "/customers", token)
