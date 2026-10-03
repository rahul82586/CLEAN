[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Subscriptions](../Subscriptions.md) / Subscribe

[Previous](Data-Structure.md) | [Next](Unsubscribe.md)

# Subscribe a user to a service

The request allows adding a user subscription.

## Rest API

Request Format
    
    
    GET /api/subscription/join?login=login&subscription=subscription
     
    POST /api/subscription/join?login=login&subscription=subscription

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
    GET /api/subscription/join?login=1077&subscription=132240225329952639
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
          "Action": "0",
          "Flags": "0",
          "Amount": "-3.50",
          "AmountDeal": "6745798"
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

  * login — the login of the user for whom the subscription is being added.
  * subscription — the identifier ([ID (#subscription)](../Configuration-Databases/Subscriptions/Data-Structure.md#subscription)) of the subscription configuration to be added.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * subscription — description of the created subscription. The complete list of passed parameters is available under the ["Data structure" (#subscription)](Data-Structure.md#subscription) section.
  * action — description of the action which was performed to create the subscription. The complete list of passed parameters is available under the ["Data structure" (#history)](Data-Structure.md#history) section.



## Note

  * During the request, it is checked whether adding a subscription is allowed in accordance with the [ControlMode (#subscription)](../Configuration-Databases/Subscriptions/Data-Structure.md#subscription) parameter. If necessary, the subscription cost is debited from the corresponding account. Thus, subscribing by this method is similar to how a trader subscribes.
  * To run the request, [the Manager account](../Text-Protocol-(Raw-API)/Authentication.md#client-start) must have permissions to edit subscriptions. Otherwise, error code [8](../../../Return-Codes/Common-errors.md) is returned.
  * When a subscription is added by this method, both handlers are called: [IMTSubscriptionSink::OnSubscriptionJoin](../../../Database-Interfaces/Subscriptions/IMTSubscriptionSink/OnSubscriptionJoin.md) and [IMTSubscriptionSink::OnSubscriptionAdd](../../../Database-Interfaces/Subscriptions/IMTSubscriptionSink/OnSubscriptionAdd.md).


