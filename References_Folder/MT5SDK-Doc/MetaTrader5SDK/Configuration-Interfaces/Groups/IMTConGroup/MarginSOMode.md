[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / MarginSOMode

[Previous](MarginFreeMode.md) | [Next](MarginCall.md)

# IMTConGroup::MarginSOMode

Get the mode of checking the levels of Stop Out and Margin Call.

C++
    
    
    UINT  IMTConGroup::MarginSOMode()  const

.NET (Gateway/Manager API)
    
    
    EnStopOutMode  CIMTConGroup.MarginSOMode()

Python (Manager API)
    
    
    MTConGroup.MarginSOMode

### Return Value

A value of [IMTConGroup::EnStopOutMode (#enstopoutmode)](Enumerations.md#enstopoutmode).

# IMTConGroup::MarginSOMode

Setting the mode of checking the levels of Stop Out and Margin Call.

C++
    
    
    MTAPIRES  IMTConGroup::MarginSOMode(
       const UINT     level   // SO and MC checking mode
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.MarginSOMode(
       EnStopOutMode  level   // SO and MC checking mode
       )

Python (Manager API)
    
    
    MTConGroup.MarginSOMode

### Parameters

**level**  
[in] TheIMTConGroup::EnStopOutModeenumeration is used to pass the Stop Out and Margin call checking modes.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
