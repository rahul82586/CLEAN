[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / LimitPositions

[Previous](LimitSymbols.md) | [Next](CommissionAdd.md)

# IMTConGroup::LimitPositions

Get the maximum number of open positions that can be present simultaneously on a client account from this group.

C++
    
    
    UINT  IMTConGroup::LimitPositions()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConGroup.LimitPositions()

Python (Manager API)
    
    
    MTConGroup.LimitPositions

### Return Value

The maximum number of open positions that can be present simultaneously on a client account from this group. The 0 value means that the number of positions is unlimited.

### Note

The limitation operates differently depending on the position accounting type ([IMTConGroup::MarginMode](MarginMode.md)):

  * Netting — number of open positions is considered. When a limit is reached, the platform disables placing new orders whose execution may increase the number of open positions. In fact, the platform allows placing orders only for the symbols that already have open positions. The current pending orders are not considered since their execution may lead to changes in the current positions but it cannot increase their number.
  * Hedging — pending orders are considered together with open positions, since a pending order activation always leads to opening a new position. When a limit is reached, the platform disables placing both new market orders for opening positions and pending orders.



# IMTConGroup::LimitPositions

Set the maximum number of open positions that can be present simultaneously on a client account from this group.

C++
    
    
    MTAPIRES  IMTConGroup::LimitPositions(
       const UINT  limit      // Position limit
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.LimitPositions(
       uint        limit      // Position limit
       )

Python (Manager API)
    
    
    MTConGroup.LimitPositions

### Parameters

**limit**  
[in] The maximum number of open positions that can be present simultaneously on a client account from this group. The 0 value means that the number of positions is unlimited.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The limitation operates differently depending on the position accounting type ([IMTConGroup::MarginMode](MarginMode.md)):

  * Netting — number of open positions is considered. When a limit is reached, the platform disables placing new orders whose execution may increase the number of open positions. In fact, the platform allows placing orders only for the symbols that already have open positions. The current pending orders are not considered since their execution may lead to changes in the current positions but it cannot increase their number.
  * Hedging — pending orders are considered together with open positions, since a pending order activation always leads to opening a new position. When a limit is reached, the platform disables placing both new market orders for opening positions and pending orders.


