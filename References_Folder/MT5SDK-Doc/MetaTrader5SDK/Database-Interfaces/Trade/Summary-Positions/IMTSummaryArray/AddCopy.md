[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Summary Positions](../../Summary-Positions.md) / [IMTSummaryArray](../IMTSummaryArray.md) / AddCopy

[Previous](Add.md) | [Next](Delete.md)

# IMTSummaryArray::AddCopy

Adds a copy of the object of the summary position record at the end of the array.

C++
    
    
    MTAPIRES  IMTSummaryArray::AddCopy(
       const IMTSummary*  summary      // The object of the summary position record
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSummaryArray.AddCopy(
       CIMTSummary        summary      // The object of the summary position record
       )

### Parameters

**summary**  
[in] The object of thesummary positionrecord.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method creates a copy of the 'summary' object and places it at the end of the array.

# IMTSummaryArray::AddCopy

Adds copies of objects of summary position records to an array.

C++
    
    
    MTAPIRES  IMTSummaryArray::AddCopy(
       const IMTSummaryArray*  array      // An object of summary position records array
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSummaryArray.AddCopy(
       CIMTSummaryArray        array      // An object of summary position records array
       )

### Parameters

**array**  
[in] An object ofsummary position records array.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method creates copies of summary position record objects belonging to the 'array' object, and inserts them at the end of the current array.
