[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / TradeFlags

[Previous](MailMode.md) | [Next](TradeTransferMode.md)

# IMTConGroup::TradeFlags

Get trade options of a group.

C++
    
    
    UINT64  IMTConGroup::TradeFlags()  const

.NET (Gateway/Manager API)
    
    
    EnTradeFlags  CIMTConGroup.TradeFlags()

Python (Manager API)
    
    
    MTConGroup.TradeFlags

### Return Value

A value from the [IMTConGroup::EnTradeFlags (#entradeflags)](Enumerations.md#entradeflags) enumeration.

# IMTConGroup::TradeFlags

Get trade options of a group.

C++
    
    
    MTAPIRES  IMTConGroup::TradeFlags(
       const UINT64  flags      // Trade options
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.TradeFlags(
       EnTradeFlags  flags      // Trade options
       )

Python (Manager API)
    
    
    MTConGroup.TradeFlags

### Parameters

**flags**  
[in] The trading options of a group can be passed using theIMTConGroup::EnTradeFlagsenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
