[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / MarginCall

[Previous](MarginSOMode.md) | [Next](MarginStopOut.md)

# IMTConGroup::MarginCall

Get the Margin Call level.

C++
    
    
    double  IMTConGroup::MarginCall()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConGroup.MarginCall()

Python (Manager API)
    
    
    MTConGroup.MarginCall()

### Return Value

The level of Margin Call.

### Note

The units of the level are set using the [IMTConGroup::MarginSOMode](MarginSOMode.md) method.

# IMTConGroup::MarginCall

Set the Margin Call level.

C++
    
    
    MTAPIRES  IMTConGroup::MarginCall(
       const double  level      // The level of Margin Call
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.MarginCall(
       double        level      // The level of Margin Call
       )

Python (Manager API)
    
    
    MTConGroup.MarginCall()

### Parameters

**level**  
[in] The level of Margin Call.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The units of the level are set using the [IMTConGroup::MarginSOMode](MarginSOMode.md) method.
