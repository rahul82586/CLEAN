[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Summary Positions](../../Summary-Positions.md) / [IMTSummaryArray](../IMTSummaryArray.md) / Shift

[Previous](UpdateCopy.md) | [Next](Total.md)

# IMTSummaryArray::Shift

Modifies the position of a summary position record in the array.

C++
    
    
    MTAPIRES  IMTSummaryArray::Shift(
       const UINT  pos,       // Position of the record
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSummaryArray.Shift(
       uint        pos,       // Position of the record
       int         shift      // Shift
       )

### Parameters

**pos**  
[in] The position of a record in an array, starting with 0.

**shift**  
[in] Record shift from its current position. A negative value means the shift to the beginning of an array, a positive value - to its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
