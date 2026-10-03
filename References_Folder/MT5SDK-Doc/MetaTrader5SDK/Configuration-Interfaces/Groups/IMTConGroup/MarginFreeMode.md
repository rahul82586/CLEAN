[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / MarginFreeMode

[Previous](TradeVirtualCredit.md) | [Next](MarginSOMode.md)

# IMTConGroup::MarginFreeMode

Gets the mode of including floating profit/loss into free margin calculation.

C++
    
    
    UINT  IMTConGroup::MarginFreeMode()  const

.NET (Gateway/Manager API)
    
    
    EnFreeMarginMode  CIMTConGroup.MarginFreeMode()

Python (Manager API)
    
    
    MTConGroup.MarginFreeMode

### Return Value

A value from [IMTConGroup::EnFreeMarginMode (#enfreemarginmode)](Enumerations.md#enfreemarginmode).

# IMTConGroup::MarginFreeMode

Sets the mode of including floating profit/loss into free margin calculation.

C++
    
    
    MTAPIRES  IMTConGroup::MarginFreeMode(
       const UINT      freemode   // Mode of including floating profit/loss
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.MarginFreeMode(
       EnFreeMarginMode freemode  // Mode of including floating profit/loss
       )

Python (Manager API)
    
    
    MTConGroup.MarginFreeMode

### Parameters

**freemode**  
[in] TheIMTConGroup::EnFreeMarginModeenumeration is used to set the mode of free margin use.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
