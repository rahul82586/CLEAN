[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeeder](../IMTConFeeder.md) / ParameterShift

[Previous](ParameterClear.md) | [Next](ParameterTotal.md)

# IMTConFeeder::ParameterShift

Change the position of the data feed parameter in the list.

C++
    
    
    MTAPIRES  IMTConFeeder::ParameterShift(
       const UINT  pos,       // Position of the parameter
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFeeder.ParameterShift(
       uint        pos,       // Position of the parameter
       int         shift      // Shift
       )

Python (Manager API)
    
    
    MTConFeeder.ParameterShift(
       pos,        # Position of the parameter
       shift       # Shift
       )

### Parameters

**pos**  
[in] Position of the parameter, starting with 0.

**shift**  
[in] Shift from its current position. A negative value means the shift to the top of the list, a positive value - to its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
