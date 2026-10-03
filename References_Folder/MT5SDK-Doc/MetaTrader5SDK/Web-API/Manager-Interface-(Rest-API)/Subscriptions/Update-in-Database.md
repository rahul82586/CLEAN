[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Subscriptions](../Subscriptions.md) / Update in Database

[Previous](Add-to-Database.md) | [Next](Delete-from-Database.md)

# Update a subscription in the server database

The request allows editing a user subscription directly in the server database.

## Rest API

Request Format
    
    
    POST /api/subscription/update
    [ Array of subscription descriptions in JSON format ]

Response Format
    
    
    {
      "retcode" : "0 Done",
     "answer" : [ response codes for each subscription ]
    }

Example
    
    
    //--- request to the server
    POST /api/subscription/update
    [
      {
        "Timestamp": "446824746",
        "Login": "1000",
        "Subscription": "330629627",
        "Status": "0",
        "Flags": "0",
        "TimeSubscribe": "1612778109",
        "TimeRenewal": "1612778109",
        "TimeExpire": "1615370109"
      },
      {
        "Timestamp": "446824746",
        "Login": "1000",
        "Subscription": "330629627",
        "Status": "0",
        "Flags": "0",
        "TimeSubscribe": "1612778109",
        "TimeRenewal": "1612778109",
        "TimeExpire": "1615370109"
      }
    ]
    //--- server response
    {
      "retcode": "0 Done",
      "answer": [
        0,
        17
      ]
    }

## Raw API

Request Format
    
    
    SUBSCRIPTION_UPDATE|\r\n
    Array of subscription descriptions in JSON format

Response Format
    
    
    SUBSCRIPTION_UPDATE|RETCODE=code description|\r\n
    Response codes for each subscription

## Request Parameters

The request has no parameters. The description of the subscriptions to be edited is passed in JSON format, as an additional body. The key field for finding an exiting record is ID.

All required fields of a subscription must be filled in, not only the ones that need to be changed. It is recommended that you first [receive](Get.md) a subscription from the server, change the required fields, and then send it back to the server.

The complete description of possible parameters is provided in the ["Data structure" (#subscription)](Data-Structure.md#subscription) section.

## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — array of response codes regarding the update of each subscription.



## Note

  * During the request, it is NOT checked whether editing a subscription is allowed in accordance with the [ControlMode (#subscription)](../Configuration-Databases/Subscriptions/Data-Structure.md#subscription) parameter. Changes take place directly in the database.
  * To run the request, [the Manager account](../Text-Protocol-(Raw-API)/Authentication.md#client-start) must have permissions to edit subscriptions. Otherwise, error code [8](../../../Return-Codes/Common-errors.md) is returned.


