[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / MarginMode

[Previous](MarginFreeProfitMode.md) | [Next](MarginFlags.md)

# IMTConGroup::MarginMode

Gets the risk management mode applied for the group.

C++
    
    
    UINT  IMTConGroup::MarginMode()  const

.NET (Gateway/Manager API)
    
    
    EnMarginMode  CIMTConGroup.MarginMode()

Python (Manager API)
    
    
    MTConGroup.MarginMode

### Return Value

A value from [IMTConGroup::EnMarginMode (#enmarginmode)](Enumerations.md#enmarginmode).

# IMTConGroup::MarginMode

Sets the risk management mode applied for the group.

C++
    
    
    MTAPIRES  IMTConGroup::MarginMode(
       const UINT   mode        // Risk management model
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.MarginMode(
       EnMarginMode  mode        // Risk management model
       )

Python (Manager API)
    
    
    MTConGroup.MarginMode

### Parameters

**freemode**  
[in] TheIMTConGroup::EnMarginMode. enumeration is used to set the risk management model.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
