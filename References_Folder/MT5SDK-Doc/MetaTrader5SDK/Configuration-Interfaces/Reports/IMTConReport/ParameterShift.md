[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Reports](../../Reports.md) / [IMTConReport](../IMTConReport.md) / ParameterShift

[Previous](ParameterClear.md) | [Next](ParameterTotal.md)

# IMTConReport::ParameterShift

Change the position of a report parameter in the list.

C++
    
    
    MTAPIRES  IMTConReport::ParameterShift(
       const UINT  pos,       // Position of the parameter
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConReport.ParameterShift(
       uint        pos,       // Position of the parameter
       int         shift      // Shift
       )

Python (Manager API)
    
    
    MTConReport.ParameterShift(
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
