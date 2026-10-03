[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Subscriptions](../Subscriptions.md) / Add to Database

[Previous](Unsubscribe.md) | [Next](Update-in-Database.md)

# Add a subscription to the server database

The request allows adding a user subscription directly to the server database.

## Rest API

Request Format
    
    
    POST /api/subscription/add
    [ Array of subscription descriptions in JSON format ]

Response Format
    
    
    {
      "retcode" : "0 Done",
     "answer" : [ response codes for each subscription ]
    }

Example
    
    
    //--- request to the server
    POST /api/subscription/add
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
        "TimeExpire": "1615370109",
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
    
    
    SUBSCRIPTION_ADD|\r\n
    Array of subscription descriptions in JSON format

Response Format
    
    
    SUBSCRIPTION_ADD|RETCODE=code description|\r\n
    Response codes for each subscription

## Request Parameters

The request has no parameters. Descriptions of subscriptions is passed in JSON format, as an additional body. The complete description of the possible parameters is provided in the ["Data structure" (#subscription)](Data-Structure.md#subscription) section.

## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — array of response codes regarding the addition of each subscription.



## Note

  * During the request, it is NOT checked if adding a subscription is allowed in accordance with the [ControlMode (#subscription)](../Configuration-Databases/Subscriptions/Data-Structure.md#subscription) parameter. Changes take place directly in the database. Also, in this case, the subscription cost is not debited from the trader's account.
  * To run the request, [the Manager account](../Text-Protocol-(Raw-API)/Authentication.md#client-start) must have permissions to edit subscriptions. Otherwise, error code [8](../../../Return-Codes/Common-errors.md) is returned.
  * When adding a subscription by this method, the [IMTSubscriptionSink::OnSubscriptionAdd](../../../Database-Interfaces/Subscriptions/IMTSubscriptionSink/OnSubscriptionAdd.md) handler is called, while the [IMTSubscriptionSink::OnSubscriptionJoin](../../../Database-Interfaces/Subscriptions/IMTSubscriptionSink/OnSubscriptionJoin.md) handler is not called.


