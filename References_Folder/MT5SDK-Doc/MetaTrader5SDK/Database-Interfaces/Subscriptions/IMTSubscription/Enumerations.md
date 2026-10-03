[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscription](../IMTSubscription.md) / Enumerations

[Previous](../IMTSubscription.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTSubscription](../IMTSubscription.md) class contains the following enumerations:

  * [IMTSubscription::EnStatus (#enstatus)](Enumerations.md#enstatus)
  * [IMTSubscription::EnFlags (#enflags)](Enumerations.md#enflags)



<a id="enstatus"></a>
## IMTSubscription::EnStatus (#enstatus)

IMTSubscription::EnStatus provides a list of possible subscription states.

ID | Value | Description  
STATUS_ACTIVE | 0 | Active subscription.  
STATUS_SUSPENDED | 1 | Suspended subscription.  
STATUS_CANCELED | 2 | Canceled subscription.  
ORDER_STATE_FIRST |  | Enumeration beginning. Corresponds to STATUS_ACTIVE.  
ORDER_STATE_LAST |  | End of enumeration. Corresponds to STATUS_CANCELED.  
  
The enumeration is used in the [IMTSubscription::Status](Status.md) method.

<a id="enflags"></a>
## IMTSubscription::EnFlags (#enflags)

IMTSubscription::EnFlags provides a list of flags for additional subscription properties.

ID | Value | Description  
FLAG_NONE | 0x00 | No flags.  
FLAG_FREE_PERIOD | 0x01 | A free subscription period is currently active.  
FLAG_ALL |  | All flags are set.  
  
The enumeration is used in the [IMTSubscription::Flags](Flags.md) method.
