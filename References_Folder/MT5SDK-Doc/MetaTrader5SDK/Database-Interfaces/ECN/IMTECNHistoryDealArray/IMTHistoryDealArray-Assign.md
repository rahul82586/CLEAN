[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryDealArray](../IMTHistoryDealArray.md) / IMTHistoryDealArray Assign

[Previous](IMTHistoryDealArray-Release.md) | [Next](IMTHistoryDealArray-Clear.md)

# IMTECNHistoryDealArray

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTECNHistoryDealArray::Assign(
       const IMTECNHistoryDealArray*  array    // source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryDealArray.Assign(
       CIMTECNHistoryDealArray        array    // source object
       )

### Parameters

**array**  
[in] Source object.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
