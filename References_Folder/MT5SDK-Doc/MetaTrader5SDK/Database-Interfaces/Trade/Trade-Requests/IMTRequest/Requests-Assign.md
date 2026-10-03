[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests Assign

[Previous](Requests-Release.md) | [Next](Requests-Clear.md)

# IMTRequest::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTRequest::Assign(
       const IMTRequest*  request      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.Assign(
       CIMTRequest        request      // Source object
       )

### Parameters

**request**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
