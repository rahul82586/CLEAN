[🏠 Document Start](../../README.md) / [Database Interfaces](../README.md) / [Subscriptions](../Subscriptions.md) / IMTSubscriptionHistory

[Previous](IMTSubscriptionArray/SearchRight.md) | [Next](IMTSubscriptionHistory/Enumerations.md)

# IMTSubscriptionHistory

This interface provides access to [parameters of actions with subscriptions (#history)](https://support.metaquotes.net/en/docs/mt5/platform/administration/subscriptions/subscriptions_control#history).

Method | Purpose  
---|---  
[Release](IMTSubscriptionHistory/Release.md) | Delete the current object.  
[Assign](IMTSubscriptionHistory/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTSubscriptionHistory/Clear.md) | Clear an object.  
[ID](IMTSubscriptionHistory/ID.md) | Get a unique identifier of a subscription action.  
[Login](IMTSubscriptionHistory/Login.md) | Get and set the login of the client to whom the subscription belongs.  
[Subscription](IMTSubscriptionHistory/Subscription.md) | Get and set the subscription configuration identifier.  
[Record](IMTSubscriptionHistory/Record.md) | Get and set the identifier of the subscription with which the action is performed.  
[Action](IMTSubscriptionHistory/Action.md) | Get and set the type of performed subscription action.  
[Time](IMTSubscriptionHistory/Time.md) | Get and set the subscription action time.  
[Amount](IMTSubscriptionHistory/Amount.md) | Get and set the subscription payment amount.  
[AmountDigits](IMTSubscriptionHistory/AmountDigits.md) | Get and set the number of decimal places in the subscription payment amount.  
[AmountDeal](IMTSubscriptionHistory/AmountDeal.md) | Get and set the ticket of the deal by which the subscription payment was conducted.  
  
The IMTSubscriptionHistory class contains the following enumerations:

Enumeration | Description  
---|---  
[EnAction (#enaction)](IMTSubscriptionHistory/Enumerations.md#enaction) | Possible actions with subscriptions.
