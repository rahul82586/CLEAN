[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryMatchingArray](../IMTHistoryMatchingArray.md) / IMTHistoryMatchingArray AddCopy

[Previous](IMTHistoryMatchingArray-Add.md) | [Next](IMTHistoryMatchingArray-Delete.md)

# IMTECNHistoryMatchingArray::AddCopy

Add a copy of a matching order object to the end of an array.

C++
    
    
    MTAPIRES  IMTECNHistoryMatchingArray::AddCopy(
       const IMTECNHistoryMatching*        order   // order to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryMatchingArray.AddCopy(
       CIMTECNHistoryMatching              order   // order to be added
       )

### Parameters

**order**  
[in]Matching order object.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

This method creates a copy of the 'order' object and places it at the end of the array.

# IMTECNHistoryMatchingArray::AddCopy

Add copies of the objects of matching orders to the array.

C++
    
    
    MTAPIRES  IMTECNHistoryMatchingArray::AddCopy(
       const IMTECNHistoryMatchingArray*  array   // array of orders to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryMatchingArray.AddCopy(
       CIMTECNHistoryMatchingArray        array   // array of orders to be added
       )

### Parameters

**array**  
[in] An object of the order array.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

This method creates a copy of order objects belonging to the 'array' object, and inserts them at the end of the current array.
