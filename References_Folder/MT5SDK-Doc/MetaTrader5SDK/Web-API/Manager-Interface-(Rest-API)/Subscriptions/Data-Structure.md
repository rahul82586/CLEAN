[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Subscriptions](../Subscriptions.md) / Data Structure

[Previous](../Subscriptions.md) | [Next](Subscribe.md)

<a id="data-structure"></a>
# Data Structure (#data-structure)

Subscription information is sent in JSON format in response to the following requests:

  * [/api/subscription/join](Subscribe.md)
  * [/api/subscription/cancel](Unsubscribe.md)
  * [/api/subscription/get](Get.md)
  * [/api/subscription/history/get](Get-from-History.md)



<a id="subscription"></a>
## Active subscription (#subscription)

Active subscription information includes the following parameters:

Parameter | Type | Description  
ID | Integer | Subscription ID  
Timestamp | Integer | Used by MetaTrader 5 servers for internal purposes. If the Timestamp of a record has changed, it means that the record has changed.  
Login | Integer | The login of the client to whom the subscription belongs.  
Subscription | Integer | Subscription configuration ID.  
Status | Integer | Subscription status. The status is passed by the [EnStatus (#enstatus)](../../../Database-Interfaces/Subscriptions/IMTSubscription/Enumerations.md#enstatus) enumeration.  
Flags | Integer | Additional subscription properties. Additional settings are passed by the [EnFlags (#enflags)](../../../Database-Interfaces/Subscriptions/IMTSubscription/Enumerations.md#enflags) enumeration.  
TimeSubscribe | Integer | Subscription start time in seconds since 01.01.1970.  
TimeRenewal | Integer | The last subscription renewal time in seconds since 01.01.1970.  
TimeExpire | Integer | Subscription expiration time in seconds since 01.01.1970.  
  
<a id="history"></a>
## Subscription action (history) (#history)

Information about an entry in the subscription history includes the following parameters:

Parameter | Type | Description  
ID | Integer | A unique identifier of a subscription action.  
Timestamp | Integer | Used by MetaTrader 5 servers for internal purposes. If the Timestamp of a record has changed, it means that the record has changed.  
Login | Integer | The login of the client to whom the subscription belongs.  
Subscription | Integer | Subscription configuration ID.  
Record | Integer | The identifier of the subscription with which the action is performed.  
Action | Integer | The type of performed subscription action. The type is passed by the [EnAction (#enaction)](../../../Database-Interfaces/Subscriptions/IMTSubscriptionHistory/Enumerations.md#enaction) enumeration.  
TimeCreated | Integer | Subscription action time in seconds since 01.01.1970.  
Amount | Float | The amount paid for the subscription.  
AmountDeal | Integer | The ticket of the deal by which the subscription payment was conducted.
