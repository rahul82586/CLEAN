[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryDeal](../IMTHistoryDeal.md) / IMTHistoryDeal Assign

[Previous](IMTHistoryDeal-Release.md) | [Next](IMTHistoryDeal-Clear.md)

# IMTECNHistoryDeal::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTECNHistoryDeal::Assign(
       const IMTECNHistoryDeal*  deal  // source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryDeal.Assign(
       CIMTECNHistoryDeal        deal  // source object
       )

### Parameters

**deal**  
[in] Source object.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
