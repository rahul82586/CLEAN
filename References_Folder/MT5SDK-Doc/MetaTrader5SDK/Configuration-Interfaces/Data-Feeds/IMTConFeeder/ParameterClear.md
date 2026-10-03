[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeeder](../IMTConFeeder.md) / ParameterClear

[Previous](ParameterDelete.md) | [Next](ParameterShift.md)

# IMTConFeeder::ParameterClear

Clear the list of parameters of a data feed.

C++
    
    
    MTAPIRES  IMTConFeeder::ParameterClear()  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFeeder.ParameterClear()

Python (Manager API)
    
    
    MTConFeeder.ParameterClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method clears the entire list of parameters of a data feed.
