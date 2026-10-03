[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Subscriptions](../Subscriptions.md) / Delete from Database

[Previous](Update-in-Database.md) | [Next](Get.md)

# Delete a subscription from the server database

The request allows deleting a user subscription directly from the server database.

## Rest API

Request Format
    
    
    GET /api/subscription/delete?id=identifier
     
    POST /api/subscription/delete?id=identifier

Response Format
    
    
    { "retcode" : "code description" }

Example
    
    
    //--- request to the server
    GET /api/subscription/delete?id=12345
    //--- server response
    {
      "retcode": "0 Done"
    }

## Raw API

Request Format
    
    
    SUBSCRIPTION_DELETE|ID=identifier|\r\n

Response Format
    
    
    SUBSCRIPTION_DELETE|RETCODE=code description|\r\n

## Request Parameters

  * id — subscription identifier. The [ID (#subscription)](Data-Structure.md#subscription) value is used for the identifier.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.



## Note

  * During the request, it is NOT checked whether deleting a subscription is allowed in accordance with the [ControlMode (#subscription)](../Configuration-Databases/Subscriptions/Data-Structure.md#subscription) parameter. Changes take place directly in the database.
  * To run the request, [the Manager account](../Text-Protocol-(Raw-API)/Authentication.md#client-start) must have permissions to edit subscriptions. Otherwise, error code [8](../../../Return-Codes/Common-errors.md) is returned.
  * When deleting a subscription by this method, the [IMTSubscriptionSink::OnSubscriptionDelete](../../../Database-Interfaces/Subscriptions/IMTSubscriptionSink/OnSubscriptionDelete.md) handler is called, while the [IMTSubscriptionSink::OnSubscriptionCancel](../../../Database-Interfaces/Subscriptions/IMTSubscriptionSink/OnSubscriptionCancel.md) handler is not called.


