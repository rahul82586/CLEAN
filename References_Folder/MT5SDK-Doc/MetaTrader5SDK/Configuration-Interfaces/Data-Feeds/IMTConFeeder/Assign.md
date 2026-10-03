[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeeder](../IMTConFeeder.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConFeeder::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConFeeder::Assign(
       const IMTConFeeder*  param      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFeeder.Assign(
       CIMTConFeeder        param      // Source object
       )

### Parameters

**param**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
