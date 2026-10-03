[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNFillingArray](../IMTFillingArray.md) / IMTFillingArray Delete

[Previous](IMTFillingArray-AddCopy.md) | [Next](IMTFillingArray-Detach.md)

# IMTECNFillingArray::Delete

Delete a filling order object by its position.

C++
    
    
    MTAPIRES  IMTECNFillingArray::Delete(
       const UINT  pos      // order position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNFillingArray.Delete(
       uint        pos      // order position
       )

### Parameters

**pos**  
[in] Order position in the array, starting with 0.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The deleted object will be automatically released by the [IMTECNFilling::Release](../IMTECNFilling/IMTFilling-Release.md) method call.
