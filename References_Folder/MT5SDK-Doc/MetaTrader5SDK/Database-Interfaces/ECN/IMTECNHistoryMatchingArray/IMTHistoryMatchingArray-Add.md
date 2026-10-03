[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryMatchingArray](../IMTHistoryMatchingArray.md) / IMTHistoryMatchingArray Add

[Previous](IMTHistoryMatchingArray-Clear.md) | [Next](IMTHistoryMatchingArray-AddCopy.md)

# IMTECNHistoryMatchingArray::Add

Add a matching order object to the end of the array.

C++
    
    
    MTAPIRES  IMTECNHistoryMatchingArray::Add(
       IMTECNHistoryMatching*  order  // order to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNMatchingArray.Add(
       CIMTECNHistoryMatching  order  // order to be added
       )

### Parameters

**order**  
[in]Matching order object.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

This method places a pointer to a passed object at the end of an array. After a successful call of this method, the control over the 'order' object lifetime is passed to the array object. Thus, when deleting an array object (by [IMTECNHistoryMatchingArray::Release](IMTHistoryMatchingArray-Release.md) call), the earlier inserted objects will be automatically deleted.

# IMTECNMatchingArray::Add

Add an object of an array of matching orders to the end of an array.

C++
    
    
    MTAPIRES  IMTECNHistoryMatchingArray::Add(
       IMTECNHistoryMatchingArray*  array   // array of orders to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryMatchingArray.Add(
       CIMTECNHistoryMatchingArray  array    // array of orders to be added
       )

### Parameters

**array**  
[in] An object of the order array.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

This method places the pointers stored in the 'array' object, at the end of the current array, and clears the 'array' object.

### Example
    
    
    //--- example
       IMTECNHistoryMatchingArray *array=api->ECNHistoryMatchingCreateArray();   
       IMTECNHistoryMatching      *order=api->ECNHistoryMatchingCreate();
    //---
       array->Add(order);  // after that the lifetime is controlled by the array
       array->Delete(0);   // delete the first element, after that a pointer in 'order' becomes invalid ('Release' was called)
     
    //--- incorrect use example
       IMTECNHistoryMatchingArray *array=api->ECNHistoryMatchingCreateArray();   
       IMTECNHistoryMatching      *order=api->ECNHistoryMatchingCreate();
    //---
       array->Add(order);
       array->Add(order); // in this case the array will contain two pointers to one and the same object!
       //--- an attempt to clear the array will lead to crash, because this will be an attempt to delete the object twice
