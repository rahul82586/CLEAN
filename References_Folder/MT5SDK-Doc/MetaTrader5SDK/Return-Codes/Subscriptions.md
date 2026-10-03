[🏠 Document Start](../README.md) / [Return Codes](README.md) / Subscriptions

[Previous](Messengers.md) | [Next](../Structures/README.md)

# Subscriptions

This group of codes is returned by the server when working with [subscription configurations](../Configuration-Interfaces/Subscriptions.md) and [databases](../Database-Interfaces/Subscriptions.md):

Constant | Value | Description  
MT_RET_SUBS_NOT_FOUND | 15000 | [Subscription](../Database-Interfaces/Subscriptions/IMTSubscription.md) not found.  
MT_RET_SUBS_NOT_FOUND_CFG | 15001 | [Subscription configuration](../Configuration-Interfaces/Subscriptions/IMTConSubscription.md) not found.  
MT_RET_SUBS_NOT_FOUND_USER | 15002 | User from subscription not found.  
MT_RET_SUBS_DISABLED | 15003 | Subscription disabled. The current status can be obtained via [IMTSubscription::Status](../Database-Interfaces/Subscriptions/IMTSubscription/Status.md).  
MT_RET_SUBS_PERMISSION_USER | 15004 | Subscription not allowed for the user.  
MT_RET_SUBS_PERMISSION_SUBSCRIBE | 15005 | Subscription not allowed. The availability of a subscription option is determined by the [IMTConSubscription::ControlMode](../Configuration-Interfaces/Subscriptions/IMTConSubscription/ControlMode.md) property.  
MT_RET_SUBS_PERMISSION_UNSUBSCRIBE | 15006 | Unsubscribing not allowed. The ability to unsubscribe is determined by the [IMTConSubscription::ControlMode](../Configuration-Interfaces/Subscriptions/IMTConSubscription/ControlMode.md) property.  
MT_RET_SUBS_REAL_ONLY | 15007 | Subscription only allowed for real accounts.
