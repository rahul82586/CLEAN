[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTConfirm](../Requests-IMTConfirm.md) / Requests Assign

[Previous](Requests-Release.md) | [Next](Requests-Clear.md)

# IMTConfirm::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConfirm::Assign(
       const IMTConfirm*  confirm      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConfirm.Assign(
       CIMTConfirm        confirm      // Source object
       )

### Parameters

**confirm**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
