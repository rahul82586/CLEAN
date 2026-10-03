[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNMatchingArray](../IMTMatchingArray.md) / IMTMatchingArray Update

[Previous](IMTMatchingArray-Detach.md) | [Next](IMTMatchingArray-UpdateCopy.md)

# IMTECNMatchingArray::Update

Update a matching order at the specified array position.

C++
    
    
    MTAPIRES  IMTECNMatchingArray::Update(
       const UINT       pos,     // position
       IMTECNMatching*  order    // order object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNMatchingArray.Update(
       uint             pos,    // position
       CIMTECNMatching  order   // order object
       )

### Parameters

**pos**  
[in] Order position in the array, starting with 0.

**order**  
[in]Matching order object.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The IMTECNMatchingArray::Update method deletes the previous element ([IMTECNHistoryDealArray::Release](../IMTECNMatching/IMTMatching-Release.md) call) and replaces it with a new one. After that, the lifetime of the new element is controlled by an array object. Therefore, when you delete the array object (through IMTECNMatchingArray::Release call), the previously inserted object is also deleted.

### Example
    
    
    //--- example
      IMTECNMatchingArray *array=api->ECNMatchingCreateArray();  
       IMTECNMatching      *order1=api->ECNMatchingCreate();
       IMTECNMatching      *order2=api->ECNMatchingCreate();
    //---
       array->Add(order1);
       array->Update(0,order2); // the first element (the order1 object) is replaced with order2
       //--- after that the order1 element will be released via Release, and order2 lifetime will be controlled by the array
