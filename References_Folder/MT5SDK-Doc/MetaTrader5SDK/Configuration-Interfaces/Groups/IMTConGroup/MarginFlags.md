[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / MarginFlags

[Previous](MarginMode.md) | [Next](MarginFloatingLeverage.md)

# IMTConGroup::MarginFlags

Gets margin calculation flags.

C++
    
    
    UINT64  IMTConGroup::MarginFlags()  const

.NET (Gateway/Manager API)
    
    
    MarginFlags  CIMTConGroup.MarginFlags()

Python (Manager API)
    
    
    MTConGroup.MarginFlags

### Return Value

A value from [IMTConGroup::MarginFlags (#enmarginflags)](Enumerations.md#enmarginflags).

# IMTConGroup::MarginFlags

Sets margin calculation flags.

C++
    
    
    MTAPIRES  IMTConGroup::MarginFlags(
       const UINT64  flags      // Margin calculation flags
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.MarginFlags(
       MarginFlags   flags      // Margin calculation flags
       )

Python (Manager API)
    
    
    MTConGroup.MarginFlags

### Parameters

**flags**  
[in] TheIMTConGroup::MarginFlagsenumeration is used to pass margin calculation flags.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
