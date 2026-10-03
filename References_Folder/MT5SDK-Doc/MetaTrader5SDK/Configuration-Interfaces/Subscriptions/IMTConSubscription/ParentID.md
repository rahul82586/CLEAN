[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / ParentID

[Previous](ID.md) | [Next](DependsID.md)

# IMTConSubscription::ParentID

Get the ID of the subdirectory in which the configuration is located.

C++
    
    
    UINT64  IMTConSubscription::ParentID()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConSubscription.ParentID()

### Return Value

The unique identifier for the directory.

### Note

For convenience, subscriptions can be grouped by directories. The [IMTConSubscription](../IMTConSubscription.md) configuration object can be either a description of the subscription or a description of a subdirectory of subscriptions. This can be determined by the [IMTConSubscription::TYPE_FOLDER (#entype)](Enumerations.md#entype) property.
