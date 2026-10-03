[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeeder](../IMTConFeeder.md) / ParameterUpdate

[Previous](ParameterAdd.md) | [Next](ParameterDelete.md)

# IMTConFeeder::ParameterUpdate

Update a parameter of a data feed.

C++
    
    
    MTAPIRES  IMTConFeeder::ParameterUpdate(
       const UINT          pos,       // Position of the parameter
       const IMTConParam*  param      // An object of a data feed parameter
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFeeder.ParameterUpdate(
       uint                pos,       // Position of the parameter
       CIMTConParam        param      // An object of a data feed parameter
       )

Python (Manager API)
    
    
    MTConFeeder.ParameterUpdate(
       pos,                # Position of the parameter
       param               # An object of a data feed parameter
       )
    
    
    MTConFeeder.ParameterSet(
       param               # A list of objects of a data feed parameters
       )

### Parameters

**pos**  
[in] Position of the parameter, starting with 0.

**param**  
[in] An object of a data feed parameter.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
