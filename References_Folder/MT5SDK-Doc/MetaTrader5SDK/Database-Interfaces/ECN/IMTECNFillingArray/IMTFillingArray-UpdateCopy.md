[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNFillingArray](../IMTFillingArray.md) / IMTFillingArray UpdateCopy

[Previous](IMTFillingArray-Update.md) | [Next](IMTFillingArray-Shift.md)

# IMTECNFillingArray::UpdateCopy

Change the filling order at the specified position of the array by copying the parameters of the passed order object.

C++
    
    
    MTAPIRES  IMTECNFillingArray::UpdateCopy(
       const UINT             pos,    // position
       const IMTECNFilling*   order   // order object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNFillingArray.UpdateCopy(
       uint                   pos,    // position
       CIMTECNFilling         order   // order object
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

Unlike the [IMTECNFillingArray::Update](IMTFillingArray-Update.md) method, calling this method sets no additional conditions for the order object control, but it is more resource-intensive since an additional object is created.
