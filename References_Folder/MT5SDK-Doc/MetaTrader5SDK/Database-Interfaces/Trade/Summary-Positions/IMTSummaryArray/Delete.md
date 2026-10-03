[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Summary Positions](../../Summary-Positions.md) / [IMTSummaryArray](../IMTSummaryArray.md) / Delete

[Previous](AddCopy.md) | [Next](Detach.md)

# IMTSummaryArray::Delete

Deletes the summary position record object from the array by its index.

C++
    
    
    MTAPIRES  IMTSummaryArray::Delete(
       const UINT  pos      // Position of the record
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSummaryArray.Delete(
       uint        pos      // Position of the record
       )

### Parameters

**pos**  
[in] Position of the record, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The object to delete will be automatically released by calling the [IMTSummary::Release](../IMTSummary/Release.md) method.
