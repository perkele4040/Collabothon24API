from getTokenSbx import getTokenSbxClientCredentials
from ClientCredentials import ClientCredentials
from callAPISbx import callApiSbx

cc = ClientCredentials("53234da7-8504-42a7-8272-81e6293e31ba", "9daad530-94d2-4046-b55b-37f39da1ee29")

token = getTokenSbxClientCredentials(cc)
print(token + "\n")

#**************ACCOUNTS FOREIGN UNITS*******************

basepath = "/accounts-api/21/v1"

#GET /info
callApiSbx(basepath, "/info", token)

#GET /accounts/accountID
callApiSbx(basepath, "/accounts", token, query="130471100000EUR")


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