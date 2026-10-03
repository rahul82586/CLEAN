[🏠 Document Start](../../README.md) / [Database Interfaces](../README.md) / [Subscriptions](../Subscriptions.md) / IMTSubscription

[Previous](../Subscriptions.md) | [Next](IMTSubscription/Enumerations.md)

# IMTSubscription

This interface provides access to a [trader's subscription parameters](https://support.metaquotes.net/en/docs/mt5/platform/administration/subscriptions/subscriptions_control).

Method | Purpose  
---|---  
[Release](IMTSubscription/Release.md) | Delete the current object.  
[Assign](IMTSubscription/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTSubscription/Clear.md) | Clear an object.  
[ID](IMTSubscription/ID.md) | Get a unique subscription identifier.  
[Login](IMTSubscription/Login.md) | Get and set the login of the client to whom the subscription belongs.  
[Subscription](IMTSubscription/Subscription.md) | Get and set the subscription configuration identifier.  
[Status](IMTSubscription/Status.md) | Get and set the subscription status.  
[Flags](IMTSubscription/Flags.md) | Get and set additional subscription properties.  
[TimeSubscribe](IMTSubscription/TimeSubscribe.md) | Get and set the subscription start time.  
[TimeRenewal](IMTSubscription/TimeRenewal.md) | Get and set the last subscription renewal time.  
[TimeExpire](IMTSubscription/TimeExpire.md) | Get and set the subscription expiration time.  
  
The IMTSubscription class contains the following enumerations:

Enumeration | Description  
---|---  
[EnStatus (#enstatus)](IMTSubscription/Enumerations.md#enstatus) | Possible subscription statuses.  
[EnFlags (#enflags)](IMTSubscription/Enumerations.md#enflags) | Flags for additional subscription properties.
