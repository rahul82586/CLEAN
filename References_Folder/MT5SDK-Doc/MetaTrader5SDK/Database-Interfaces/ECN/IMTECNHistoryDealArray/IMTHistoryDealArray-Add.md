[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryDealArray](../IMTHistoryDealArray.md) / IMTHistoryDealArray Add

[Previous](IMTHistoryDealArray-Clear.md) | [Next](IMTHistoryDealArray-AddCopy.md)

# IMTECNHistoryDealArray::Add

Add a deal object to the end of the array.

C++
    
    
    MTAPIRES  IMTECNHistoryDealArray::Add(
       IMTECNHistoryDeal*  deal   // deal to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNMatchingArray.Add(
       CIMTECNHistoryDeal  deal   // deal to be added
       )

### Parameters

**deal**  
[in]Deal object.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

This method places a pointer to a passed object at the end of an array. After a successful call of this method, the control over the life time of the deal object is passed to the array object. Thus, when deleting an array object (by a call of [IMTECNHistoryDealArray::Release](IMTHistoryDealArray-Release.md)), an earlier inserted object is automatically removed.

# IMTECNHistoryDealArray::Add

Add an object of the array of deals to the end of the array.

C++
    
    
    MTAPIRES  IMTECNHistoryDealArray::Add(
       IMTECNHistoryDealArray*  array   // array of deals to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryDealArray.Add(
       CIMTECNHistoryDealArray  array    // array of deals to be added
       )

### Parameters

**array**  
[in] An object of the array of deals.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

This method places the pointers stored in the 'array' object, at the end of the current array, and clears the 'array' object.

### Example
    
    
    //--- example
       IMTECNHistoryDealArray *array=api->ECNHistoryDealCreateArray();   
       IMTECNHistoryDeal      *deal =api->ECNHistoryDealCreate();
    //---
       array->Add(deal);   // after that the lifetime is controlled by the array
       array->Delete(0);   // delete the first element, after that a pointer in 'deal' becomes invalid ('Release' was called)
     
    //--- incorrect use example
       IMTECNHistoryDealArray *array=api->ECNHistoryDealCreateArray();   
       IMTECNHistoryDeal      *deal =api->ECNHistoryDealCreate();
    //---
       array->Add(deal);
       array->Add(deal); // in this case the array will contain two pointers to one and the same object!
       //--- an attempt to clear the array will lead to crash, because this will be an attempt to delete the object twice
