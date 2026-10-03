[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryFillingArray](../IMTHistoryFillingArray.md) / IMTHistoryFillingArray Delete

[Previous](IMTHistoryFillingArray-AddCopy.md) | [Next](IMTHistoryFillingArray-Detach.md)

# IMTECNHistoryFillingArray::Delete

Delete a filling order object by its position.

C++
    
    
    MTAPIRES  IMTECNHistoryFillingArray::Delete(
       const UINT  pos      // order position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryFillingArray.Delete(
       uint        pos      // order position
       )

### Parameters

**pos**  
[in] Order position in the array, starting with 0.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The deleted object will be automatically released by the [IMTECNHistoryFilling::Release](../IMTHistoryFilling.md) method call.
