[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Subscriptions](../Subscriptions.md) / Get

[Previous](Delete-from-Database.md) | [Next](Check-Existence.md)

# Get user subscriptions

The request allows receiving a user's subscriptions.

## Rest API

Request Format
    
    
    GET /api/subscription/get?id=identifier
    GET /api/subscription/get?login=login
    GET /api/subscription/get?login=login&subscription=subscription
     
    POST /api/subscription/get?id=identifier
    POST /api/subscription/get?login=login
    POST /api/subscription/get?login=login&subscription=subscription

Response Format
    
    
    {
      "retcode" : "0 Done",
     "answer" : [ one or more subscription descriptions ]
    }

Example
    
    
    //--- request to the server
    GET /api/subscription/get?id=8
    //--- server response
    {
      "retcode": "0 Done",
      "answer": {
        "Id": "8",
        "Timestamp": "132576179398749593",
        "Login": "1077",
        "Subscription": "132240225329952639",
        "Status": "0",
        "Flags": "0",
        "TimeSubscribe": "1613147939",
        "TimeRenewal": "1613147939",
        "TimeExpire": "1615739939"
      }
    }

## Raw API

Request Format
    
    
    SUBSCRIPTION_GET|ID=identifier|\r\n
    SUBSCRIPTION_GET|LOGIN=login|\r\n
    SUBSCRIPTION_GET|LOGIN=login|SUBSCRIPTION=subscription|\r\n

Response Format
    
    
    SUBSCRIPTION_GET|RETCODE=code description|\r\n
    One or more subscription descriptions in JSON format

## Request Parameters

  * id — subscription identifier. The [ID (#subscription)](Data-Structure.md#subscription) value is used for the identifier.
  * login — the login of the user whose subscriptions you are requesting. All the user's subscriptions will be returned when requested by login.
  * subscription — the identifier of the subscription configuration ([ID (#subscription)](../Configuration-Databases/Subscriptions/Data-Structure.md#subscription)) to be received. This parameter can only be used in combination with 'login' parameter to get the user's subscription to a specific service.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.



## Note

To run the request, [the Manager account](../Text-Protocol-(Raw-API)/Authentication.md#client-start) must have permissions to view subscriptions. Otherwise, error code [8](../../../Return-Codes/Common-errors.md) is returned.
