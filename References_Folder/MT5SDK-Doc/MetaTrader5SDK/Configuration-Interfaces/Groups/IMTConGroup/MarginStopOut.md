[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / MarginStopOut

[Previous](MarginCall.md) | [Next](MarginFreeProfitMode.md)

# IMTConGroup::MarginStopOut

Get the Stop Out level.

C++
    
    
    double  IMTConGroup::MarginStopOut()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConGroup.MarginStopOut()

Python (Manager API)
    
    
    MTConGroup.MarginStopOut

### Return Value

The level of Stop Out.

### Note

The units of the level are set using the [IMTConGroup::MarginSOMode](MarginSOMode.md) method.

# IMTConGroup::MarginStopOut

Set the Stop Out level.

C++
    
    
    MTAPIRES  IMTConGroup::MarginStopOut(
       const double  level      // The level of Stop Out
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.MarginStopOut(
       double        level      // The level of Stop Out
       )

Python (Manager API)
    
    
    MTConGroup.MarginStopOut

### Parameters

**level**  
[in] The level of Stop Out.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The units of the level are set using the [IMTConGroup::MarginSOMode](MarginSOMode.md) method.
