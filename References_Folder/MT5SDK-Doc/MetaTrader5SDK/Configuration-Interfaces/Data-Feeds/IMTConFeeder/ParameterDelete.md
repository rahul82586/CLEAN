[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeeder](../IMTConFeeder.md) / ParameterDelete

[Previous](ParameterUpdate.md) | [Next](ParameterClear.md)

# IMTConFeeder::ParameterDelete

Delete a parameter of a data feed by its index.

C++
    
    
    MTAPIRES  IMTConFeeder::ParameterDelete(
       const UINT  pos      // Position of the parameter
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFeeder.ParameterDelete(
       uint        pos      // Position of the parameter
       )

Python (Manager API)
    
    
    MTConFeeder.ParameterDelete(
       pos         # Position of the parameter
       )

### Parameters

**pos**  
[in] Position of the parameter, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) is returned.
