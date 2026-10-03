[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeeder](../IMTConFeeder.md) / ParameterAdd

[Previous](TimeoutAttempts.md) | [Next](ParameterUpdate.md)

# IMTConFeeder::ParameterAdd

Add a parameter of a data feed.

C++
    
    
    MTAPIRES  IMTConFeeder::ParameterAdd(
       IMTConParam*  param      // An object of a data feed parameter
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFeeder.ParameterAdd(
       CIMTConParam  param      // An object of a data feed parameter
       )

Python (Manager API)
    
    
    MTConFeeder.ParameterAdd(
       param         # An object of a data feed parameter
       )

### Parameters

**param**  
[in] An object of a data feed parameter.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
