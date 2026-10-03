[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Assets](../../Assets.md) / [IMTExposureArray](../IMTExposureArray.md) / Shift

[Previous](UpdateCopy.md) | [Next](Total.md)

# IMTExposureArray::Shift

Changes the position of an asset record in the array.

C++
    
    
    MTAPIRES  IMTExposureArray::Shift(
       const UINT  pos,       // Position of the record
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCod  CIMTExposureArray.Shift(
       uint        pos,       // Position of the record
       int         shift      // Shift
       )

### Parameters

**pos**  
[in] The position of an asset record in an array, starting with 0.

**shift**  
[in] Record shift from its current position. A negative value means the shift to the beginning of an array, a positive value - to its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
