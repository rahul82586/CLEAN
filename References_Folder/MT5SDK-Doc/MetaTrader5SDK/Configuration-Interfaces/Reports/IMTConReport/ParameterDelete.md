[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Reports](../../Reports.md) / [IMTConReport](../IMTConReport.md) / ParameterDelete

[Previous](ParameterUpdate.md) | [Next](ParameterClear.md)

# IMTConReport::ParameterDelete

Delete a report parameter by the index.

C++
    
    
    MTAPIRES  IMTConReport::ParameterDelete(
       const UINT  pos      // Position of the parameter
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConReport.ParameterDelete(
       uint        pos      // Position of the parameter
       )

Python (Manager API)
    
    
    MTConReport.ParameterDelete(
       pos         # Position of the parameter
       )

### Parameters

**pos**  
[in] Position of the parameter, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) is returned.
