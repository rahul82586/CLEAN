[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryFillingArray](../IMTHistoryFillingArray.md) / IMTHistoryFillingArray AddCopy

[Previous](IMTHistoryFillingArray-Add.md) | [Next](IMTHistoryFillingArray-Delete.md)

# IMTECNHistoryFillingArray::AddCopy

Add a copy of a filling order object to the end of an array.

C++
    
    
    MTAPIRES  IMTECNHistoryFillingArray::AddCopy(
       const IMTECNHistoryFilling*        order   // order to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNFillingArray.AddCopy(
       CIMTECNHistoryFilling              order   // order to be added
       )

### Parameters

**order**  
[in]Filling order object.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

This method creates a copy of the 'order' object and places it at the end of the array.

# IMTECNHistoryFillingArray::AddCopy

Add copies of filling order objects to the end of an array.

C++
    
    
    MTAPIRES  IMTECNHistoryFillingArray::AddCopy(
       const IMTECNHistoryFillingArray*   array   // array of orders to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryFillingArray.AddCopy(
       CIMTECNHistoryFillingArray         array   // array of orders to be added
       )

### Parameters

**array**  
[in] An object of the order array.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

This method creates a copy of order objects belonging to the 'array' object, and inserts them at the end of the current array.
