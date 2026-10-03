[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Summary Positions](../../Summary-Positions.md) / [IMTSummaryArray](../IMTSummaryArray.md) / Add

[Previous](Clear.md) | [Next](AddCopy.md)

# IMTSummaryArray::Add

Adds an object of the summary position record at the end of the array.

C++
    
    
    MTAPIRES  IMTSummaryArray::Add(
       IMTSummary*  summary      // The object of the summary position record
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSummaryArray.Add(
       CIMTSummary  summary      // The object of the summary position record
       )

### Parameters

**summary**  
[in] The object of thesummary positionrecord.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method places a pointer to a passed object at the end of an array. After a successful call of this method, the control over the life time of the 'summary' object is passed to the array object. Thus, when deleting an array object (call of [IMTSummaryArray::Release](Release.md)), an earlier inserted object is automatically removed.

# IMTSummaryArray::Add

Adds an object of the array of summary position records at the end of the array.

C++
    
    
    MTAPIRES  IMTSummaryArray::Add(
       IMTSummaryArray*  array      // An object of summary position records array
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSummaryArray.Add(
       CIMTSummaryArray  array      // An object of summary position records array
       )

### Parameters

**array**  
[in] An object ofsummary position records array.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method places the pointers, which are in the array object, at the end of the current array and clears the array object.

Example:
    
    
    //--- Example
        IMTSummaryArray *array  =api->SummaryCreateArray();
        IMTSummary      *summary=api->SummaryCreate();
     //---
        array->Add(summary);// After that the lifetime is controlled by the array
        array->Delete(0);    // Delete the first element, after which the pointer in exposure becomes invalid (Release has been called)
     //--- An example of incorrect use
        IMTSummaryArray  *array  =api->SummaryCreateArray();
        IMTSummary       *summary=api->SummaryCreate();
     //---
        array->Add(summary); 
        array->Add(summary); // In this case the array contains two pointers to the same object!
        //--- Array clearing will cause crash, because two attempts will be made to delete the same object
