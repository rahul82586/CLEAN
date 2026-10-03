[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / DependsID

[Previous](ParentID.md) | [Next](Name.md)

# IMTConSubscription::DependsID

Get the subscription which the current subscription depends on.

C++
    
    
    UINT64  IMTConSubscription::DependsID()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConSubscription.DependsID()

### Return Value

The identifier of the subscription ([IMTConSubscription::ID](ID.md)), 

### Note

This property sets if another product subscription is required in order to subscribe to the current product.

# IMTConSubscription::DependsID

Set the subscription which the current subscription depends on.

C++
    
    
    MTAPIRES  IMTConSubscription::DependsID(
       const UINT64  depends_id  // Subscription ID
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.DependsID(
       uint          depends_id  // Subscription ID
       )

### Parameters

**depends_id**  
[in] The identifier of the subscription (IMTConSubscription::ID) which the current subscription depends on.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This property sets if another product subscription is required in order to subscribe to the current product.
