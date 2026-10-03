[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeederModule](../IMTConFeederModule.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConFeederModule::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConFeederModule::Assign(
       const IMTConFeederModule*  param      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFeederModule.Assign(
       CIMTConFeederModule        param      // Source object
       )

### Parameters

**param**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
