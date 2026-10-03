[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Summary Positions](../../Summary-Positions.md) / [IMTSummaryArray](../IMTSummaryArray.md) / Clear

[Previous](Assign.md) | [Next](Add.md)

# IMTSummaryArray::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTSummaryArray::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSummaryArray.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
