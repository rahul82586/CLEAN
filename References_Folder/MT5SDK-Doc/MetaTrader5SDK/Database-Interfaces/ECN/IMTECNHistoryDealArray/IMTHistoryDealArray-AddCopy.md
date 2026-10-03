[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryDealArray](../IMTHistoryDealArray.md) / IMTHistoryDealArray AddCopy

[Previous](IMTHistoryDealArray-Add.md) | [Next](IMTHistoryDealArray-Delete.md)

# IMTECNHistoryDealArray::AddCopy

Add a copy of a deal object to the end of an array.

C++
    
    
    MTAPIRES  IMTECNHistoryDealArray::AddCopy(
       const IMTECNHistoryDeal*        deal   // deal to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryMatchingArray.AddCopy(
       CIMTECNHistoryDeal              deal   // deal to be added
       )

### Parameters

**deal**  
[in]Deal object.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

This method creates a copy of the deal object and places it at the end of the array.

# IMTECNHistoryDealArray::AddCopy

Add copies of deal objects into an array.

C++
    
    
    MTAPIRES  IMTECNHistoryDealArray::AddCopy(
       const IMTECNHistoryDealArray*  array   // array of deals to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryDealArray.AddCopy(
       CIMTECNHistoryDealArray        array   // array of deals to be added
       )

### Parameters

**array**  
[in] An object of the array of deals.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

This method creates a copy of the objects of deals belonging to the array object, and inserts them at the end of the current array.
