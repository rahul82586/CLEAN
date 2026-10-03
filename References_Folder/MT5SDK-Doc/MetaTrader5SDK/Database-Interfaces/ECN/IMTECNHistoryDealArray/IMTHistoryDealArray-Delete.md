[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryDealArray](../IMTHistoryDealArray.md) / IMTHistoryDealArray Delete

[Previous](IMTHistoryDealArray-AddCopy.md) | [Next](IMTHistoryDealArray-Detach.md)

# IMTECNHistoryDealArray::Delete

Delete a deal object by its position.

C++
    
    
    MTAPIRES  IMTECNHistoryDealArray::Delete(
       const UINT  pos      // deal position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryDealArray.Delete(
       uint        pos      // deal position
       )

### Parameters

**pos**  
[in] Position of a deal in an array, starting with 0.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The deleted object will be automatically released by the [IMTECNHistoryDeal::Release](../IMTECNHistoryDeal/IMTHistoryDeal-Release.md) method call.
