[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDealArray](../IMTDealArray.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTDealArray::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTDealArray::Assign(
       const IMTDealArray*  array      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDealArray.Assign(
       CIMTDealArray        array      // Source object
       )

### Parameters

**array**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
