[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Subscriptions](../Subscriptions.md) / Unsubscribe

[Previous](Subscribe.md) | [Next](Add-to-Database.md)

# Unsubscribe a user from a service

The request allows canceling a user subscription.

## Rest API

Request Format
    
    
    GET /api/subscription/cancel?login=login&subscription=subscription
     
    POST /api/subscription/cancel?login=login&subscription=subscription

Response Format
    
    
    {
      "retcode" : "0 Done",
      "answer" : {
        "subscription" : { subscription description },
        "action" : { action description }
      }
    }

Example
    
    
    //--- request to the server
    GET /api/subscription/cancel?login=1077&subscription=132240225329952639
    //--- server response
    {
      "retcode": "0 Done",
      "answer": {
        "subscription": {
          "Id": "8",
          "Timestamp": "132576179398749593",
          "Login": "1077",
          "Subscription": "132240225329952639",
          "Status": "0",
          "Flags": "0",
          "TimeSubscribe": "1613147939",
          "TimeRenewal": "1613147939",
          "TimeExpire": "1615739939"
        },
        "action": {
          "Id": "13",
          "Timestamp": "132576179398799588",
          "Login": "1077",
          "Subscription": "132240225329952639",
          "Record": "8",
          "TimeCreated": "1613147939",
          "Action": "3",
          "Flags": "0",
          "Amount": "0",
          "AmountDeal": "0"
        }
      }
    }

## Raw API

Request Format
    
    
    SUBSCRIPTION_JOIN|LOGIN=login|SUBSCRIPTION=subscription|\r\n

Response Format
    
    
    SUBSCRIPTION_JOIN|RETCODE=code description|\r\n
    Description of the created subscription and action in JSON format

## Request Parameters

  * login — [the login of the user](../../../Database-Interfaces/Users/IMTUser/Login.md) for whom the subscription is canceled.
  * subscription — [ID of subscription configuration](../../../Configuration-Interfaces/Subscriptions/IMTConSubscription/ID.md) to be canceled.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * subscription — description of the canceled subscription. The complete list of passed parameters is available under the ["Data structure" (#subscription)](Data-Structure.md#subscription) section.
  * action — description of the action which was performed to cancel the subscription. The complete list of passed parameters is available under the ["Data structure" (#history)](Data-Structure.md#history) section.



## Note

  * During the request, it is checked if canceling a subscription is allowed in accordance with the [ControlMode (#subscription)](../Configuration-Databases/Subscriptions/Data-Structure.md#subscription) parameter.
  * To run the request, [the Manager account](../Text-Protocol-(Raw-API)/Authentication.md#client-start) must have permissions to edit subscriptions. Otherwise, error code [8](../../../Return-Codes/Common-errors.md) is returned.
  * When a subscription is canceled by this method, both handlers are called: [IMTSubscriptionSink::OnSubscriptionCancel](../../../Database-Interfaces/Subscriptions/IMTSubscriptionSink/OnSubscriptionCancel.md) and [IMTSubscriptionSink::OnSubscriptionDelete](../../../Database-Interfaces/Subscriptions/IMTSubscriptionSink/OnSubscriptionDelete.md).


