[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryFillingArray](../IMTHistoryFillingArray.md) / IMTHistoryFillingArray UpdateCopy

[Previous](IMTHistoryFillingArray-Update.md) | [Next](IMTHistoryFillingArray-Shift.md)

# IMTECNHistoryFillingArray::UpdateCopy

Change a filling order at the specified position of an array by copying the parameters of a passed object of an order.

C++
    
    
    MTAPIRES  IMTECNHistoryFillingArray::UpdateCopy(
       const UINT                   pos,    // position
       const IMTECNHistoryFilling*  order   // order object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryFillingArray.UpdateCopy(
       uint                         pos,    // position
       CIMTECNHistoryFilling        order   // order object
       )

### Parameters

**pos**  
[in] Order position in the array, starting with 0.

**order**  
[in]Filling order object.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

This method copies the parameters of the order object into an object of an order at the specified position of an array.
