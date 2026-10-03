[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Summary Positions](../../Summary-Positions.md) / [IMTSummaryArray](../IMTSummaryArray.md) / Next

[Previous](Total.md) | [Next](Sort.md)

# IMTSummaryArray::Next

Gets the summary position record object by its index.

C++
    
    
    IMTSummary*  IMTSummaryArray::Next(
       const UINT  index      // Position of the record
       )  const

.NET (Gateway/Manager API)
    
    
    CIMTSummary  CIMTSummaryArray.Next(
       uint        index      // Position of the record
       )

### Parameters

**index**  
[in] The position of the record in an array, starting with 0.

### Return Value

If successful, it returns a pointer to the summary position record object at the specified position in the array. Otherwise, it returns NULL.

### Note

The lifetime of the returned object is controlled by the current array object. Thus, when deleting an array object, the returned pointer will be invalid.
