[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Subscriptions](../Subscriptions.md) / Delete from History

[Previous](Update-in-History.md) | [Next](Get-from-History.md)

# Delete a subscription action from the server database

The request allows deleting a user subscription action directly from the server database.

## Rest API

Request Format
    
    
    GET /api/subscription/history/delete?id=identifier
     
    POST /api/subscription/history/delete?id=identifier

Response Format
    
    
    { "retcode" : "code description" }

Example
    
    
    //--- request to the server
    GET /api/subscription/history/delete?id=12345
    //--- server response
    {
      "retcode": "0 Done"
    }

## Raw API

Request Format
    
    
    SUBSCRIPTION_HISTORY_DELETE|ID=identifier|\r\n

Response Format
    
    
    SUBSCRIPTION_HISTORY_DELETE|RETCODE=code description|\r\n

## Request Parameters

  * id — identifier of a subscription action. The [ID (#history)](Data-Structure.md#history) value is used for the identifier.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.



## Note

To run the request, [the Manager account](../Text-Protocol-(Raw-API)/Authentication.md#client-start) must have permissions to edit subscriptions. Otherwise, error code [8](../../../Return-Codes/Common-errors.md) is returned.
