[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Subscriptions](../Subscriptions.md) / Get from History

[Previous](Delete-from-History.md) | [Next](../Common-Requests.md)

# Get a history of user's subscription actions

The request allows receiving a history of actions related to the user's subscriptions.

## Rest API

Request Format
    
    
    GET /api/subscription/history/get?from=date&to=date&login=login
    GET /api/subscription/history/get?id=identifier
     
    POST /api/subscription/history/get?from=date&to=date&login=login
    POST /api/subscription/history/get?id=identifier

Response Format
    
    
    {
      "retcode" : "0 Done",
     "answer" : [ one or more subscription descriptions ]
    }

Example
    
    
    //--- request to the server
    GET /api/subscription/history/get?id=2
    //--- server response
    {
      "retcode": "0 Done",
      "answer": {
        "Id": "2",
        "Timestamp": "841632718",
        "Login": "1000",
        "Subscription": "330629627",
        "Record": "2",
        "TimeCreated": "1613642109",
        "Action": "1",
        "Flags": "0",
        "Amount": "123123",
        "AmountDeal": "0"
      }
    }

## Raw API

Request Format
    
    
    SUBSCRIPTION_HISTORY_GET|FROM=date|TO=date|LOGIN=login|\r\n
    SUBSCRIPTION_HISTORY_GET|ID=identifier|\r\n

Response Format
    
    
    SUBSCRIPTION_HISTORY_GET|RETCODE=code description|\r\n
    One or more subscription descriptions in JSON format

## Request Parameters

  * id — identifier of a subscription action. The [ID (#history)](Data-Structure.md#history) value is used for the identifier.
  * login — the login of the user whose history of subscription actions you want to obtain.
  * from — the beginning of the history requesting period. The date is specified in seconds that have since 01.01.1970. The parameter is required when using the 'login' parameter.
  * to — the end of the history requesting period. The date is specified in seconds that have since 01.01.1970. The parameter is required when using the 'login' parameter.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.



## Note

To run the request, [the Manager account](../Text-Protocol-(Raw-API)/Authentication.md#client-start) must have permissions to view subscriptions. Otherwise, error code [8](../../../Return-Codes/Common-errors.md) is returned.
