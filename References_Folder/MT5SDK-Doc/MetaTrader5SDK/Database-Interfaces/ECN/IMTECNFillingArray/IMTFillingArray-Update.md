[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNFillingArray](../IMTFillingArray.md) / IMTFillingArray Update

[Previous](IMTFillingArray-Detach.md) | [Next](IMTFillingArray-UpdateCopy.md)

# IMTECNFillingArray::Update

Change a filling order at the specified position of the array.

C++
    
    
    MTAPIRES  IMTECNFillingArray::Update(
       const UINT       pos,     // position
       IMTECNFilling*   order    // order object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNFillingArray.Update(
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

The IMTECNFillingArray::Update method deletes the previous element ([IMTECNFilling::Release](../IMTECNFilling/IMTFilling-Release.md) call) and replaces it with a new one. After that, the lifetime of the new element is controlled by an array object. Thus, when deleting an array object (by IMTECNFillingArray::Release call), the earlier inserted objects will be automatically deleted.

### Example
    
    
    //--- example
       IMTECNFillingArray *array=api->ECNFillingCreateArray();   
       IMTECNFilling      *order1=api->ECNFillingCreate();
       IMTECNFilling      *order2=api->ECNFillingCreate();
    //---
       array->Add(order1);
       array->Update(0,order2); // the first element (the order1 object) is replaced with order2
       //--- after that the order1 element will be released via Release, and order2 lifetime will be controlled by the array
