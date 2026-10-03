[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryDealArray](../IMTHistoryDealArray.md) / IMTHistoryDealArray UpdateCopy

[Previous](IMTHistoryDealArray-Update.md) | [Next](IMTHistoryDealArray-Shift.md)

# IMTECNHistoryDealArray::UpdateCopy

Change a deal at the specified position of an array by copying the parameters of a passed deal object.

C++
    
    
    MTAPIRES  IMTECNHistoryDealArray::UpdateCopy(
       const UINT                    pos,    // position
       const IMTECNHistoryDeal*      deal    // deal object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryDealArray.UpdateCopy(
       uint                          pos,    // position
       CIMTECNHistoryDeal            deal    // deal object
       )

### Parameters

**pos**  
[in] Position of a deal in an array, starting with 0.

**deal**  
[in]Deal object.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

This method copies the parameters of the 'deal' object into a deal object at the specified position of an array.
