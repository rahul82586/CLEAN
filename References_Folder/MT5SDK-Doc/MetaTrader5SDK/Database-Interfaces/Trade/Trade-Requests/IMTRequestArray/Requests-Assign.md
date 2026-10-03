[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequestArray](../Requests-IMTRequestArray.md) / Requests Assign

[Previous](Requests-Release.md) | [Next](Requests-Clear.md)

# IMTRequestArray::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTRequestArray::Assign(
       const IMTRequestArray*  array      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequestArray.Assign(
       CIMTRequestArray        array      // Source object
       )

### Parameters

**array**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
