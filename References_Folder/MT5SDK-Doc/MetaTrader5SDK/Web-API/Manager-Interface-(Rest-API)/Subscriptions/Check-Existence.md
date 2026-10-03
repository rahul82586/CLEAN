[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Subscriptions](../Subscriptions.md) / Check Existence

[Previous](Get.md) | [Next](Add-to-History.md)

# Checking if a user subscription exists

The request allows checking if the user has a subscription to the specified service.

## Rest API

Request Format
    
    
    GET /api/subscription/exist?login=login&subscription=subscription
     
    POST /api/subscription/exist?login=login&subscription=subscription

Response Format
    
    
    { "retcode" : "code description" }

Example
    
    
    //--- request to the server
    GET /api/subscription/exist?login=1001&subscription=132240225329952639
    //--- server response
    {
      "retcode": "13 Not found"
    }

## Raw API

Request Format
    
    
    SUBSCRIPTION_EXIST|LOGIN=login|SUBSCRIPTION=subscription|\r\n

Response Format
    
    
    SUBSCRIPTION_EXIST|RETCODE=code description|\r\n

## Request Parameters

  * logi — the login of the user whose subscriptions you want to check.
  * subscription — the identifier of the subscription configuration ([ID (#subscription)](../Configuration-Databases/Subscriptions/Data-Structure.md#subscription)) to be checked.



## Response Parameters

  * retcode — if the subscription exists, the command returns [response code](../../../Return-Codes/Successful-completion.md) 0\. If the subscription is not found, code [13](../../../Return-Codes/Common-errors.md) is returned.



## Note

To run the request, [the Manager account](../Text-Protocol-(Raw-API)/Authentication.md#client-start) must have permissions to view subscriptions. Otherwise, error code [8](../../../Return-Codes/Common-errors.md) is returned.
