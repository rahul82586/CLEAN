[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTDeal::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTDeal::Assign(
       const IMTDeal*  deal      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.Assign(
       CIMTDeal        deal      // Source object
       )

### Parameters

**deal**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
