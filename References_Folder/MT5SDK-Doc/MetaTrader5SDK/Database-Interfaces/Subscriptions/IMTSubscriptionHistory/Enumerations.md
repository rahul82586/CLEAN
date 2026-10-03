[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscriptionHistory](../IMTSubscriptionHistory.md) / Enumerations

[Previous](../IMTSubscriptionHistory.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTSubscriptionHistory](../IMTSubscriptionHistory.md) class contains the following enumerations:

  * [IMTSubscriptionHistory::EnAction (#enaction)](Enumerations.md#enaction)



<a id="enaction"></a>
## IMTSubscriptionHistory::EnAction (#enaction)

IMTSubscriptionHistory::EnAction provides a list of possible subscription actions.

ID | Value | Description  
ACTION_SUBSCRIBE | 0 | Subscribing.  
ACTION_RENEWAL | 1 | Subscription renewal.  
ACTION_SUSPEND | 2 | Subscription suspension.  
ACTION_CANCEL | 3 | Unsubscribing.  
ACTION_DELETED | 4 | Deleting a subscription.  
ACTION_FIRST |  | Enumeration beginning. Corresponds to ACTION_SUBSCRIBE.  
ACTION_LAST |  | End of enumeration. Corresponds to ACTION_DELETED.  
  
The enumeration is used in the [IMTSubscriptionHistory::Action](Action.md) method.
