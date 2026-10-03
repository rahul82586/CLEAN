[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / LimitOrders

[Previous](Credit.md) | [Next](LimitPositionsValue.md)

# IMTUser::LimitOrders

Get the maximum number of active (placed) pending orders allowed on the account.

C++
    
    
    UINT  IMTUser::LimitOrders()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTUser.LimitOrders()

### Return Value

The maximum number of orders.

# IMTUser::LimitOrders

Set the maximum number of active (placed) pending orders allowed on the account.

C++
    
    
    MTAPIRES  IMTUser::LimitOrders(
       const UINT  limit      // Limit on orders
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUser.LimitOrders(
       ouint       limit      // Limit on orders
       )

### Parameters

**limit**  
[in] The maximum number of orders.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code has occurred.

### Note

Once the limit is reached, the client will no longer be able to place new pending orders If the value is not specified (0), a limit defined at the group level ([IMTConGroup::LimitOrders](../../../Configuration-Interfaces/Groups/IMTConGroup/LimitOrders.md)) will be used. If limits are set both at the account and at the group level, the stricter one of them will be applied.
