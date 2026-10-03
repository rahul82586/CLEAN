[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Summary Positions](../../Summary-Positions.md) / [IMTSummaryArray](../IMTSummaryArray.md) / Detach

[Previous](Delete.md) | [Next](Update.md)

# IMTSummaryArray::Detach

Detaches the summary position record object from the array.

C++
    
    
    IMTSummary*  IMTSummaryArray::Detach(
       const UINT  pos      // Position of the record
       )

.NET (Gateway/Manager API)
    
    
    CIMTSummary  CIMTSummaryArray.Detach(
       uint        pos      // Position of the record
       )

### Parameters

**pos**  
[in] The position of a record in an array, starting with 0.

### Return Value

Returns a pointer to the detached object of the [summary position record](../IMTSummary.md).

### Note

This method removes the pointer to the object at the given position of the array and returns it. The size of the array is decreased by one, and the deleted object is not freed.
