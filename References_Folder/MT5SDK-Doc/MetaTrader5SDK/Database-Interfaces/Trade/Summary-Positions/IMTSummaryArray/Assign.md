[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Summary Positions](../../Summary-Positions.md) / [IMTSummaryArray](../IMTSummaryArray.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTSummaryArray::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTSummaryArray::Assign(
       const IMTSummaryArray*  array      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSummaryArray.Assign(
       CIMTSummaryArray        array      // Source object
       )

### Parameters

**array**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
