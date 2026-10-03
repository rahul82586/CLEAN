[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Summary Positions](../../Summary-Positions.md) / [IMTSummaryArray](../IMTSummaryArray.md) / Update

[Previous](Detach.md) | [Next](UpdateCopy.md)

# IMTSummaryArray::Update

Modifies a summary position record in the array.

C++
    
    
    MTAPIRES  IMTSummaryArray::Update(
       const UINT   pos,         // Position in the array
       IMTSummary*  summary      // The object of the summary position record
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSummaryArray.Update(
       uint         pos,         // Position in the array
       CIMTSummary  summary      // The object of the summary position record
       )

### Parameters

**pos**  
[in] The position of a record in an array, starting with 0.

**summary**  
[in] The object of the summary position record.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The IMTSummaryArray::Update method deletes the previous element (call of [IMTSummary::Release](../IMTSummary/Release.md)) and replaces it with a new one. After that, the lifetime of a new element is controlled by an array object. Thus, when deleting an array object (call of [IMTSummaryArray::Release](Release.md)), an earlier inserted object is automatically removed.

Example:
    
    
    //--- Example
        IMTSummaryArray *array   =api->SummaryCreateArray();
        IMTSummary      *summary1=api->SummaryCreate();
        IMTSummary      *summary2=api->SummaryCreate();
     //---
        array->Add(summary1);
        array->Update(0,summary2); // The first element (the summary1 object) is replaced with summary2
        //--- Aafter that the summary1 element will be released through Release, and the lifetime of summary2 will be controlled by the array
