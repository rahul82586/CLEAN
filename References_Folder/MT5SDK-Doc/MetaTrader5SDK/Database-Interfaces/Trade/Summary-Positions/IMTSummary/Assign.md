[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Summary Positions](../../Summary-Positions.md) / [IMTSummary](../IMTSummary.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTSummary::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTSummary::Assign(
       const IMTSummary*  summary      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSummary.Assign(
       CIMTSummary        summary      // Source object
       )

### Parameters

**summary**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
