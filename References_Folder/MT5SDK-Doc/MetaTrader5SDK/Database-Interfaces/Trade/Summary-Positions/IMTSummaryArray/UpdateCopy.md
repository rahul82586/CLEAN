[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Summary Positions](../../Summary-Positions.md) / [IMTSummaryArray](../IMTSummaryArray.md) / UpdateCopy

[Previous](Update.md) | [Next](Shift.md)

# IMTSummaryArray::UpdateCopy

Modifies a summary position record at the specified position of an array by copying the parameters of the passed object of a summary position.

C++
    
    
    MTAPIRES  IMTSummaryArray::UpdateCopy(
       const UINT          pos,         // Position
       const IMTSummary*   summary      // The object of the summary position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSummaryArray.UpdateCopy(
       uint                pos,         // Position
       CIMTSummary         summary      // The object of the summary position
       )

### Parameters

**pos**  
[in] The index of a summary position in an array, starting with 0.

**order**  
[in] The object of the summary position.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method copies the parameters of the 'summary' object into a summary position object at the specified position of an array.
