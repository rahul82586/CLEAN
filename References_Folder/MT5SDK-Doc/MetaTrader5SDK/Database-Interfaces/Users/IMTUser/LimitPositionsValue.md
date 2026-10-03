[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / LimitPositionsValue

[Previous](LimitOrders.md) | [Next](APIDataSet.md)

# IMTUser::LimitPositionsValue

Get the maximum value of open positions allowed on the account.

C++
    
    
    UINT  IMTUser::LimitPositionsValue()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTUser.LimitPositionsValue()

### Return Value

The maximum value of positions in the deposit currency.

# IMTUser::LimitPositionsValue

Set the maximum value of open positions allowed on the account.

C++
    
    
    MTAPIRES  IMTUser::LimitPositionsValue(
       const double  limit    // Limit on positions
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUser.LimitPositionsValue(
       double        limit    // Limit on positions
       )

### Parameters

**limit**  
[in] The maximum value of positions in the deposit currency.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code has occurred.

### Note

The positions are evaluated as follows:
