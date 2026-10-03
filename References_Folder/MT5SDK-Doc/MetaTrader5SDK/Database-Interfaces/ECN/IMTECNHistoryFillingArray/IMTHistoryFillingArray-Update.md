[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryFillingArray](../IMTHistoryFillingArray.md) / IMTHistoryFillingArray Update

[Previous](IMTHistoryFillingArray-Detach.md) | [Next](IMTHistoryFillingArray-UpdateCopy.md)

# IMTECNHistoryFillingArray::Update

Change the position of a filling order at the specified position of the array.

C++
    
    
    MTAPIRES  IMTECNHistoryFillingArray::Update(
       const UINT       pos,     // position
       IMTECNFilling*   order    // order object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryFillingArray.Update(
       uint             pos,    // position
       CIMTECNFilling   order   // order object
       )

### Parameters

**pos**  
[in] Order position in the array, starting with 0.

**order**  
[in]Filling order object.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The IMTECNHistoryFillingArray::Update method deletes the previous element ([IMTECNHistoryFilling::Release](../IMTECNHistoryFilling/IMTHistoryFilling-Release.md) call) and replaces it with a new one. After that, the lifetime of the new element is controlled by an array object. Thus, when deleting an array object (by IMTECNFillingArray::Release call), the earlier inserted objects will be automatically deleted.

### Example
    
    
    //--- example
      IMTECNHistoryFillingArray *array=api->ECNHistoryFillingCreateArray();  
       IMTECNHistoryFilling      *order1=api->ECNHistoryFillingCreate();
       IMTECNHistoryFilling      *order2=api->ECNHistoryFillingCreate();
    //---
       array->Add(order1);
       array->Update(0,order2); // the first element (the order1 object) is replaced with order2
       //--- after that the order1 element will be released via Release, and order2 lifetime will be controlled by the array
