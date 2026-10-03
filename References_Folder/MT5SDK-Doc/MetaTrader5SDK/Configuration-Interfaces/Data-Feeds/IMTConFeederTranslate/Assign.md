[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeederTranslate](../IMTConFeederTranslate.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConFeederTranslate::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConFeederTranslate::Assign(
       const IMTConFeederTranslate*  param      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFeederTranslate.Assign(
       CIMTConFeederTranslate        param      // Source object
       )

### Parameters

**param**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
