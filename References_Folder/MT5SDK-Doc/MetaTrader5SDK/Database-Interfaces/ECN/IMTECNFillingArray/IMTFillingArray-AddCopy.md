[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNFillingArray](../IMTFillingArray.md) / IMTFillingArray AddCopy

[Previous](IMTFillingArray-Add.md) | [Next](IMTFillingArray-Delete.md)

# IMTECNFillingArray::AddCopy

Add a copy of a filling order object to the end of an array.

C++
    
    
    MTAPIRES  IMTECNFillingArray::AddCopy(
       const IMTECNFilling*        order   // order to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNFillingArray.AddCopy(
       CIMTECNFilling             order   // order to be added
       )

### Parameters

**order**  
[in]Filling order object.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

This method creates a copy of the 'order' object and places it at the end of the array.

Unlike [IMTECNFillingArray::Add(IMTECNFilling* order)](IMTFillingArray-Add.md), calling this method does not impose any additional conditions for the control of the 'order' object, but is more resource-intensive, since an additional object is created.

# IMTECNFillingArray::AddCopy

Add copies of filling order objects to the end of an array.

C++
    
    
    MTAPIRES  IMTECNFillingArray::AddCopy(
       const IMTECNFillingArray*   array   // array of orders to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNMatchingArray.AddCopy(
       CIMTECNFillingArray         array   // array of orders to be added
       )

### Parameters

**array**  
[in] An object of the order array.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

This method creates a copy of order objects belonging to the 'array' object, and inserts them at the end of the current array.
