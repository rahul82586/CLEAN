[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryMatchingArray](../IMTHistoryMatchingArray.md) / IMTHistoryMatchingArray Update

[Previous](IMTHistoryMatchingArray-Detach.md) | [Next](IMTHistoryMatchingArray-UpdateCopy.md)

# IMTECNHistoryMatchingArray::Update

Update a matching order at the specified array position.

C++
    
    
    MTAPIRES  IMTECNHistoryMatchingArray::Update(
       const UINT              pos,    // position
       IMTECNHistoryMatching*  order   // order object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryMatchingArray.Update(
       uint                    pos,    // position
       CIMTECNHistoryMatching  order   // order object
       )

### Parameters

**pos**  
[in] Order position in the array, starting with 0.

**order**  
[in]Matching order object.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The IMTECNHistoryMatchingArray::Update deletes the previous element ([IMTECNMatching::Release](../IMTECNMatching/IMTMatching-Release.md) call) and replaces it with a new one. After that, the lifetime of the new element is controlled by an array object. Thus, when deleting an array object (by IMTECNHistoryMatchingArray::Release call), the earlier inserted objects will be automatically deleted.

### Example
    
    
    //--- example
       IMTECNHistoryMatchingArray *array=api->ECNHistoryMatchingCreateArray();   
       IMTECNHistoryMatching      *order1=api->ECNHistoryMatchingCreate();
       IMTECNHistoryMatching      *order2=api->ECNHistoryMatchingCreate();
    //---
       array->Add(order1);
       array->Update(0,order2); // the first element (the order1 object) is replaced with order2
       //--- after that the order1 element will be released via Release, and order2 lifetime will be controlled by the array
